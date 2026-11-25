#!/usr/bin/env python3
"""Python 101 branding check.

Checks NEW or RENAMED files against the rules in BRANDING.md and exits
with status 1 if any file breaks them. Existing files are not checked
until they are renamed (see BRANDING.md, section 8).

Usage:
    python tools/check_branding.py --staged          # files staged for commit (pre-commit hook)
    python tools/check_branding.py --base <git-ref>  # files added since <git-ref> (GitHub Action)
    python tools/check_branding.py FILE [FILE ...]   # specific files (repo-relative paths)
"""

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Rules (keep in sync with BRANDING.md)
# ---------------------------------------------------------------------------

BRAND_TITLE_PREFIX = "Python 101 · "
BRAND_STRIP = "Learn and Help · Python 101"
TAGLINE = "Empowering Minds, Inspiring Generosity."
MD_HEADER_PREFIX = "# 🐍 Python 101 — "
MD_BYLINE = "*Learn and Help · www.learnandhelp.com*"
MD_FOOTER = "*Python 101 · Learn and Help · www.learnandhelp.com*"

# Allowed file types and their extensions (BRANDING.md, section 2)
TYPE_EXTENSIONS = {
    "slides": {"pdf", "pptx"},
    "notes": {"md", "html"},          # html only for backward compatibility; md preferred
    "one_pager": {"png"},
    "playbook": {"html"},
    "playbook_quiz": {"html"},
    "quiz": {"html"},
    "lab": {"md", "ipynb"},
    "concepts": {"ipynb"},
    "skeleton": {"ipynb"},
    "assignment": {"md", "ipynb"},
}

# Folder -> types allowed in it. Current folder names are listed next to the
# new lowercase ones so new files can be added before the summer rename.
FOLDER_TYPES = {
    "presentations": {"slides", "notes", "one_pager"},
    "playbooks": {"playbook"},
    "Play": {"playbook"},
    "quizzes": {"quiz", "playbook_quiz"},
    "Quizzes": {"quiz", "playbook_quiz"},
    "labs": {"lab"},
    "Labs": {"lab"},
    "notebooks": {"concepts", "skeleton"},
    "colab_notebooks": {"concepts", "skeleton"},
    "skeletons_programming_assignments": {"skeleton"},
    "assignments": {"assignment"},
}
PLANNER_FOLDERS = {"weekly_outlines", "Weekly_Outlines", "Syllabus"}
OUTLINE_FOLDERS = {"weekly_outlines", "Weekly_Outlines"}
FINAL_PROJECT_FOLDERS = {"final_project", "Final_Project"}
IMAGE_EXTENSIONS = {"png", "jpg", "jpeg", "gif", "svg", "webp"}

# Paths that are not course content and are never checked.
EXEMPT_PREFIXES = (".github/", ".githooks/", "tools/", "templates/", "data/")
EXEMPT_ROOT_FILES = {"README.md", "BRANDING.md", "LICENSE", ".gitignore", ".gitattributes"}

TYPES_RE = "|".join(sorted(TYPE_EXTENSIONS, key=len, reverse=True))
CONTENT_NAME_RE = re.compile(
    rf"^(?P<chapter>\d{{2}})_(?P<section>\d{{1,2}})_(?P<topic>[a-z0-9]+(?:_[a-z0-9]+)*?)_"
    rf"(?P<type>{TYPES_RE})(?P<solution>_solution)?\.(?P<ext>[a-z0-9]+)$"
)
OUTLINE_NAME_RE = re.compile(r"^week\d{1,2}_outline\.md$")
PLANNER_NAME_RE =re.compile(r"^weekly_planner_\d{4}_\d{2}\.(md|xlsx)$")
SNAKE_NAME_RE = re.compile(r"^[a-z0-9]+(?:_[a-z0-9]+)*\.[a-z0-9]+$")
VERSION_SUFFIX_RE = re.compile(r"_(v\d+|new|old|final|copy|draft)(?=[._])")

NAMING_HELP = "Pattern: <CC>_<S>_<topic>_<type>.<ext>, e.g. 07_6_lists_mixed_nested_2d_playbook_quiz.html (BRANDING.md, section 2)"


# ---------------------------------------------------------------------------
# Checks
# ---------------------------------------------------------------------------

def check_name(path: str) -> list[str]:
    """Return problems with the file's name and folder."""
    parts = path.split("/")
    name = parts[-1]
    folder = parts[0] if len(parts) > 1 else ""
    ext = name.rsplit(".", 1)[-1] if "." in name else ""
    problems = []

    if " " in path:
        problems.append("Path contains spaces. Use _ between words.")
    if name != name.lower():
        problems.append("File name has capital letters. Use all lowercase.")
    if name.lower().startswith(("python101_", "python_101_", "python_")):
        problems.append("Drop the 'python101_' / 'python_' prefix; the repo name already says Python 101.")
    if VERSION_SUFFIX_RE.search(name.lower()):
        problems.append("Remove version suffixes like _v2, _new, _final. Git keeps the history.")
    if problems:
        return problems

    if folder == "presentations" and len(parts) > 2 and ext in IMAGE_EXTENSIONS:
        # Images for a deck live in presentations/images/<CC>_<S>_<topic>/ (or legacy images_* folders).
        if not SNAKE_NAME_RE.match(name):
            problems.append("Image names must be lowercase words joined by _.")
        return problems

    if folder in PLANNER_FOLDERS and PLANNER_NAME_RE.match(name):
        return problems
    if folder == "Syllabus":
        return ["Syllabus/ holds only the planner: weekly_planner_<YYYY>_<YY>.md or .xlsx."]
    if folder in OUTLINE_FOLDERS:
        if not OUTLINE_NAME_RE.match(name):
            problems.append("Weekly outlines are named week<N>_outline.md, e.g. week7_outline.md; "
                            "the planner is weekly_planner_<YYYY>_<YY>.md.")
        return problems

    if folder in FOLDER_TYPES:
        m = CONTENT_NAME_RE.match(name)
        if not m:
            return [f"Name does not follow the pattern. {NAMING_HELP}"]
        ftype = m["type"]
        if ftype not in FOLDER_TYPES[folder]:
            allowed = ", ".join(sorted(FOLDER_TYPES[folder]))
            problems.append(f"Type '{ftype}' does not belong in {folder}/. Allowed here: {allowed}.")
        if m["ext"] not in TYPE_EXTENSIONS[ftype]:
            allowed = ", ".join(sorted(TYPE_EXTENSIONS[ftype]))
            problems.append(f"'.{m['ext']}' is not allowed for type '{ftype}'. Allowed: {allowed}.")
        return problems

    if folder in FINAL_PROJECT_FOLDERS:
        if not SNAKE_NAME_RE.match(name):
            problems.append("Final project files must be lowercase words joined by _.")
        return problems

    if folder == "":
        return [f"New files don't belong in the repo root. Put '{name}' in a course folder (BRANDING.md, section 3)."]

    known = sorted({"presentations", "playbooks", "quizzes", "labs", "notebooks", "assignments",
                    "weekly_outlines", "final_project", "data", "templates"})
    return [f"Unknown folder '{folder}/'. Use one of: {', '.join(known)} (BRANDING.md, section 3)."]


def check_html(text: str) -> list[str]:
    problems = []
    m = re.search(r"<title>(.*?)</title>", text, re.IGNORECASE | re.DOTALL)
    title = re.sub(r"\s+", " ", m.group(1)).strip().replace("&amp;", "&") if m else ""
    if not title:
        problems.append("Missing <title>.")
    elif not title.startswith(BRAND_TITLE_PREFIX) or " — " not in title:
        problems.append(f"<title> must look like 'Python 101 · 7.6 Topic — Playbook & Quiz'. Found: '{title}'.")
    elif re.search(r"\b(Week|Quiz)\s+\d+\s*:", title):
        problems.append("Don't put week or quiz numbers in the <title>; the weekly outline carries them.")
    if BRAND_STRIP not in text:
        problems.append(f"Missing the brand strip '{BRAND_STRIP}' above the page heading.")
    if TAGLINE not in text:
        problems.append(f"Missing the footer 'Learn and Help · Python 101 · {TAGLINE}'.")
    if "Segoe UI" not in text:
        problems.append("Use the brand font stack: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif.")
    if "fonts.googleapis.com" in text:
        problems.append("Don't load Google Fonts; use the brand font stack so pages work offline.")
    if not ("#667eea" in text.lower() and "#764ba2" in text.lower()):
        problems.append("Use the brand gradient #667eea → #764ba2 for the background and header.")
    return problems


def check_markdown_lines(lines: list[str]) -> list[str]:
    problems = []
    content = [ln.rstrip() for ln in lines if ln.strip()]
    if not content or not content[0].startswith(MD_HEADER_PREFIX):
        problems.append(f"First line must start with '{MD_HEADER_PREFIX}'.")
    if MD_BYLINE not in [ln.strip() for ln in content[:5]]:
        problems.append(f"Header must include the line '{MD_BYLINE}' (within the first few lines).")
    if not content or content[-1].strip() != MD_FOOTER:
        problems.append(f"Last line must be the footer '{MD_FOOTER}'.")
    return problems


def check_notebook(text: str) -> list[str]:
    try:
        cells = json.loads(text).get("cells", [])
    except json.JSONDecodeError:
        return ["Notebook is not valid JSON."]
    if not cells:
        return ["Notebook has no cells."]

    def source(cell):
        src = cell.get("source", "")
        return "".join(src) if isinstance(src, list) else src

    problems = []
    first, last = cells[0], cells[-1]
    if first.get("cell_type") != "markdown" or not source(first).lstrip().startswith(MD_HEADER_PREFIX):
        problems.append(f"First cell must be a Markdown cell starting with '{MD_HEADER_PREFIX}'.")
    elif MD_BYLINE not in source(first):
        problems.append(f"First cell must include the line '{MD_BYLINE}'.")
    if last.get("cell_type") != "markdown" or MD_FOOTER not in source(last):
        problems.append(f"Last cell must be a Markdown cell with the footer '{MD_FOOTER}'.")
    return problems


def check_content(path: str, repo_root: Path) -> list[str]:
    folder = path.split("/")[0] if "/" in path else ""
    if folder in FINAL_PROJECT_FOLDERS:
        return []  # final project files: name check only
    ext = path.rsplit(".", 1)[-1].lower()
    if ext not in {"html", "md", "ipynb"}:
        return []
    file = repo_root / path
    if not file.exists():
        return []
    text = file.read_text(encoding="utf-8", errors="replace")
    if ext == "html":
        return check_html(text)
    if ext == "md":
        return check_markdown_lines(text.splitlines())
    return check_notebook(text)


def check_file(path: str, repo_root: Path, renamed: bool = False) -> list[str]:
    """Check a file. Renamed files get the name check only: their contents
    predate this guide and are rebranded separately."""
    path = path.replace("\\", "/")
    if path in EXEMPT_ROOT_FILES or path.startswith(EXEMPT_PREFIXES) or "/." in "/" + path:
        return []
    problems = check_name(path)
    if not renamed:
        problems += check_content(path, repo_root)
    return problems


# ---------------------------------------------------------------------------
# Choosing which files to check
# ---------------------------------------------------------------------------

def git(*args: str) -> str:
    return subprocess.run(["git", *args], capture_output=True, text=True, encoding="utf-8", check=True).stdout


def parse_name_status(output: str) -> dict[str, bool]:
    """Parse `git diff --name-status -z` into {path: was_renamed} for added and renamed files."""
    fields = [f for f in output.split("\0") if f]
    result, i = {}, 0
    while i < len(fields):
        status = fields[i]
        if status.startswith(("R", "C")):
            result[fields[i + 2]] = True
            i += 3
        else:
            result[fields[i + 1]] = False
            i += 2
    return result


def new_files_staged() -> dict[str, bool]:
    return parse_name_status(git("diff", "--cached", "--name-status", "-M", "--diff-filter=AR", "-z"))


def new_files_since(base: str) -> dict[str, bool]:
    return parse_name_status(git("diff", "--name-status", "-M", "--diff-filter=AR", "-z", f"{base}...HEAD"))


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description="Check new files against BRANDING.md.")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--staged", action="store_true", help="check files staged for commit")
    group.add_argument("--base", help="check files added since this git ref")
    parser.add_argument("files", nargs="*", help="repo-relative paths to check")
    args = parser.parse_args()

    repo_root = Path(git("rev-parse", "--show-toplevel").strip())
    if args.staged:
        files = new_files_staged()
    elif args.base:
        files = new_files_since(args.base)
    else:
        files = {f: False for f in args.files}
    if not files:
        print("Branding check: no new files to check.")
        return 0

    failures = {}
    for f, renamed in files.items():
        problems = check_file(f, repo_root, renamed)
        if problems:
            failures[f] = problems

    checked = len(files)
    if not failures:
        print(f"✅ Branding check passed ({checked} new file{'s' if checked != 1 else ''}).")
        return 0

    print(f"❌ Branding check failed: {len(failures)} of {checked} new file(s) don't follow BRANDING.md.\n")
    for f, problems in failures.items():
        print(f"  {f}")
        for p in problems:
            print(f"    - {p}")
        print()
    print("Fix the files above (templates/ has on-brand starting points), then try again.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
