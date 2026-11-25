#!/usr/bin/env python3
"""Rename files listed in tools/rename_map.csv and fix every link to them.

Usage:
    python tools/apply_renames.py --dry-run   # show what would change
    python tools/apply_renames.py             # rename with `git mv` and rewrite links

Links are rewritten in every tracked .md, .html, .ipynb, .txt and .py file
(both full paths like Quizzes/old.html and bare file names like old.html).
Links outside the repo (Google Classroom, bookmarks) can't be fixed here;
use rename_map.csv to update them by hand.
"""

import csv
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from check_branding import check_name  # noqa: E402

TEXT_EXTENSIONS = {".md", ".html", ".ipynb", ".txt", ".py"}
SKIP = {"tools/rename_map.csv", "BRANDING.md"}


def git(*args: str) -> str:
    return subprocess.run(["git", *args], capture_output=True, text=True, encoding="utf-8", check=True).stdout


def load_map(path: Path) -> list[tuple[str, str]]:
    with path.open(encoding="utf-8", newline="") as f:
        return [(r["old_path"].strip(), r["new_path"].strip()) for r in csv.DictReader(f)]


def build_replacements(pairs: list[tuple[str, str]]) -> dict[str, str]:
    repl = {}
    basenames = {}
    for old, new in pairs:
        repl[old] = new
        repl[old.replace(" ", "%20")] = new
        basenames.setdefault(old.rsplit("/", 1)[-1], set()).add(new.rsplit("/", 1)[-1])
    for old_base, new_bases in basenames.items():
        if len(new_bases) == 1:  # only rewrite bare names that map unambiguously
            new_base = new_bases.pop()
            repl.setdefault(old_base, new_base)
            repl.setdefault(old_base.replace(" ", "%20"), new_base)
    return repl


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    dry_run = "--dry-run" in sys.argv
    root = Path(git("rev-parse", "--show-toplevel").strip())
    pairs = load_map(root / "tools" / "rename_map.csv")
    tracked = set(git("ls-files", "-z").split("\0"))

    # Validate the whole map before touching anything.
    errors = []
    news = [n for _, n in pairs]
    for old, new in pairs:
        if old not in tracked:
            errors.append(f"not a tracked file: {old}")
        if (root / new).exists() and old.lower() != new.lower():
            errors.append(f"target already exists: {new}")
        for p in check_name(new):
            errors.append(f"{new}: {p}")
    errors += [f"two files renamed to {n}" for n in set(news) if news.count(n) > 1]
    if errors:
        print("Rename map has problems; nothing was changed:")
        print("\n".join(f"  - {e}" for e in errors))
        return 1

    repl = build_replacements(pairs)
    keys = sorted(repl, key=len, reverse=True)
    pattern = re.compile(r"(?<![\w.%-])(" + "|".join(map(re.escape, keys)) + r")(?![\w-])")

    # 1. Rename.
    for old, new in pairs:
        if dry_run:
            print(f"rename  {old}  ->  {new}")
        else:
            (root / new).parent.mkdir(parents=True, exist_ok=True)
            git("mv", old, new)

    # 2. Rewrite links (in the files' new locations).
    files = sorted((tracked - {o for o, _ in pairs}) | set(news))
    changed = 0
    for rel in files:
        if rel in SKIP or Path(rel).suffix.lower() not in TEXT_EXTENSIONS:
            continue
        src = root / (rel if not dry_run else next((o for o, n in pairs if n == rel), rel))
        if not src.exists():
            continue
        text = src.read_text(encoding="utf-8", errors="surrogateescape")
        new_text, n = pattern.subn(lambda m: repl[m.group(1)], text)
        if n:
            changed += 1
            print(f"links   {rel}: {n} updated")
            if not dry_run:
                with open(root / rel, "w", encoding="utf-8", errors="surrogateescape", newline="") as f:
                    f.write(new_text)

    verb = "would be" if dry_run else "were"
    print(f"\n{len(pairs)} files {verb} renamed; links {verb} updated in {changed} files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
