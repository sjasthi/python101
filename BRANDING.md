# Python 101 — Branding & Naming Guide

**Status:** Draft for approval · **Applies to:** everything in this repo (labs, quizzes, playbooks, presentations, notebooks, assignments, weekly outlines)

This guide makes every Python 101 file look like it came from the same class. It covers:

1. [Decisions to approve](#1-decisions-to-approve)
2. [File naming](#2-file-naming)
3. [Folders](#3-folders)
4. [Titles, headers and footers](#4-titles-headers-and-footers)
5. [Colours and fonts](#5-colours-and-fonts)
6. [Word list](#6-word-list)
7. [Templates](#7-templates)
8. [Rolling it out](#8-rolling-it-out)
9. [Automatic checks](#9-automatic-checks)

---

## 1. Decisions to approve

| # | Decision | Proposal | Why |
|---|---|---|---|
| 1 | How files are numbered | By **topic** (chapter + section, e.g. `07_6`), not by week | Week numbers shift every year with holidays; topic numbers already appear in the weekly planner and never change |
| 2 | Visual style for HTML pages | The **purple gradient** style (Segoe UI font) | About 22 of the 37 HTML pages already use it, including the newest quizzes |
| 3 | Tagline | **"Empowering Minds, Inspiring Generosity."** | Already used in the footer of the newest quizzes |
| 4 | When existing files are renamed | **Now**, in one go, with a script that also fixes every link inside the repo. Folder names stay as they are for now | Old links in Google Classroom break and must be updated by hand from `tools/rename_map.csv` (GitHub does not redirect renamed files) |

---

## 2. File naming

### The pattern

```
<CC>_<S>_<topic>_<type>.<ext>
```

| Part | Rule | Example |
|---|---|---|
| `CC` | Chapter, always **two digits** so files sort in order | `02`, `07`, `11` |
| `S` | Section within the chapter (use `0` for a whole-chapter item) | `6` |
| `topic` | Short lowercase description, words joined by `_` | `lists_mixed_nested_2d` |
| `type` | One word from the type list below | `playbook_quiz` |
| `ext` | Lowercase file extension | `.html` |

**General rules**

- All lowercase. Words joined with `_`. No spaces, no capitals, no `-`, no `&`.
- No `python101_` or `python_` prefix: the repo name already says Python 101.
- No version suffixes (`_v2`, `_new`, `_final`). Git keeps the history.
- A solution file is the same name with `_solution` added at the end.

### Types

| Type | What it is | Ext | Folder |
|---|---|---|---|
| `slides` | Lecture deck | `.pdf` / `.pptx` | `presentations/` |
| `notes` | Lecture notes | `.md` (preferred) / `.html` (allowed for backward compatibility) | `presentations/` |
| `one_pager` | One-page visual summary of a topic | `.png` | `presentations/` |
| `playbook` | Interactive page for exploring, no graded quiz | `.html` | `playbooks/` |
| `playbook_quiz` | Interactive page **with** a graded quiz | `.html` | `quizzes/` |
| `quiz` | Quiz only | `.html` | `quizzes/` |
| `lab` | In-class lab | `.md` / `.ipynb` | `labs/` |
| `concepts` | Colab notebook that teaches the topic | `.ipynb` | `notebooks/` |
| `skeleton` | Starter notebook for programming exercises | `.ipynb` | `notebooks/` |
| `assignment` | Graded programming assignment | `.md` / `.ipynb` | `assignments/` |

### Examples (current name → new name)

| Current | New |
|---|---|
| `Quizzes/python101_lists_mixed_nested_2d_playbook_and_quiz.html` | `quizzes/07_6_lists_mixed_nested_2d_playbook_quiz.html` |
| `Quizzes/functions_intro_interactive_play_and_quiz.html` | `quizzes/05_1_functions_intro_playbook_quiz.html` |
| `Labs/Lab1_Typing_and_Running_Python_Code.ipynb` | `labs/01_0_typing_and_running_code_lab.ipynb` |
| `Labs/lab20_mixed_nested_2d_lists.ipynb` | `labs/07_6_lists_mixed_nested_2d_lab.ipynb` |
| `Labs/pet_shelter_lab.html` | `labs/10_0_oop_pet_shelter_lab.ipynb` (labs are `.md` or `.ipynb`) |
| `Quizzes/python101_WWPP_comprehensive_quiz.pdf` | `quizzes/00_0_what_would_python_print_quiz.html` (quizzes are `.html` only) |
| `presentations/8_1_More_About_Strings.pdf` | `presentations/08_1_more_about_strings_slides.pdf` |
| `presentations/7_6_python_mixed_and_nested_lists.md` | `presentations/07_6_lists_mixed_nested_notes.md` |
| `colab_notebooks/ch5_1_concepts_functions_introduction.ipynb` | `notebooks/05_1_functions_intro_concepts.ipynb` |
| `skeletons_programming_assignments/ch7_skeleton_lists_exercises.ipynb` | `notebooks/07_0_lists_skeleton.ipynb` |
| `Play/python_oop_playbook.html` | `playbooks/10_0_oop_playbook.html` |

### Items without a chapter

| Item | Pattern | Example |
|---|---|---|
| Weekly outline | `week<N>_outline.md` (unchanged from today) | `week1_outline.md`, `week20_outline.md` |
| Weekly planner | `weekly_planner_<YYYY>_<YY>.md` | `weekly_planner_2026_27.md` |
| Course-wide item | `00_0_<topic>_<type>` | `00_0_colab_basics_slides.pdf`, `00_0_comprehensive_quiz.html` |
| Final project | Lives in `final_project/`, no chapter number | `final_project/auto_grader_design_slides.pdf` |
| Images for a deck | Folder named after the deck's topic | `presentations/images/07_6_lists_mixed_nested/` |

---

## 3. Folders

All folder names are lowercase.

| Folder | Holds | Replaces |
|---|---|---|
| `presentations/` | `slides`, `notes`, `one_pager`, images for decks | `presentations/` |
| `playbooks/` | `playbook` | `Play/` |
| `quizzes/` | `quiz`, `playbook_quiz` | `Quizzes/` |
| `labs/` | `lab`, `lab_solution` | `Labs/` |
| `notebooks/` | `concepts`, `skeleton` | `colab_notebooks/`, `skeletons_programming_assignments/` (these hold duplicate copies today) |
| `assignments/` | `assignment` | `assignments/` |
| `weekly_outlines/` | Weekly outlines and the planner | `Weekly_Outlines/`, `Syllabus/` |
| `final_project/` | Final project material | `Final_Project/` |
| `data/` | Data files used by labs and assignments | `data/` |
| `templates/` | Starter files for new content | *(new)* |

Placeholder files such as `foo.txt` are not needed and should be removed.

---

## 4. Titles, headers and footers

### Brand name

Always write it as **Python 101**: capital P, a space, no hyphen. Not "python101", "Python101" or "python_101". The organisation is **Learn and Help**: not "LearnAndHelp" or "Learn & Help". (Lowercase `python101` is fine in file and folder names.)

### HTML pages (quizzes, playbooks, HTML labs)

| Element | Format | Example |
|---|---|---|
| Browser tab `<title>` | `Python 101 · <CC.S> <Topic> — <Type>` | `Python 101 · 7.6 Mixed & Nested Lists — Playbook & Quiz` |
| Brand strip (small caps above the heading) | `Learn and Help · Python 101` | |
| Page heading `<h1>` | Topic only | `Mixed & Nested Lists` |
| Subtitle | One short sentence about what students will do | `Build lists inside lists and walk through rows and columns.` |
| Footer | `Learn and Help · Python 101 · Empowering Minds, Inspiring Generosity.` | |

**Type labels** for the title: `Playbook`, `Playbook & Quiz`, `Quiz`, `Lab`.

Avoid putting week numbers ("Week 10:") or quiz numbers ("Quiz 15:") in the title. Those change every year. The weekly outline says which week and which quiz number each page is.

### Markdown (weekly outlines, notes, labs, assignments)

Every Markdown file starts with this header:

```markdown
# 🐍 Python 101 — <Document title>
**Topic: <CC.S> <Topic name>**
*Learn and Help · www.learnandhelp.com*

---
```

and ends with this footer:

```markdown
---

*Python 101 · Learn and Help · www.learnandhelp.com*
```

For weekly outlines, the title is `Week <N> Outline`, e.g. `# 🐍 Python 101 — Week 7 Outline`.

### Notebooks (`.ipynb`)

The first cell is a Markdown cell using the same header as Markdown files. The last cell is a Markdown cell with the footer.

### Slides

- Title slide: topic as the main title, `Python 101 · <CC.S>` as the subtitle, and "Learn and Help" in the footer.
- Each content slide shows "Python 101 · Learn and Help" in its footer.

---

## 5. Colours and fonts

These apply to HTML pages. Slides should use the same primary colours.

### Colours

| Name | Hex | Used for |
|---|---|---|
| Brand gradient | `#667eea` → `#764ba2` (135°) | Page background, header, active tabs, table headings |
| Heading purple | `#4a3f8f` | `h2` and `h3` headings |
| Accent purple | `#553c9a` | Inline code in tables, highlighted words |
| Body text | `#2d3748` | Paragraph text |
| Muted text | `#4a5568` | Lead paragraphs, hints |
| Surface | `#ffffff` | Main content card |
| Soft surface | `#f7f7fb` | Tab bar, expandable sections |
| Border | `#e2e8f0` | Dividers |
| Code background | `#2d3748` | Code blocks |
| Code text | `#e2e8f0` | Text inside code blocks |
| Success | `#48bb78` (text on light: `#22543d`, background: `#c6f6d5`) | Correct answers, Run button, progress bar |
| Error | `#e53e3e` (text on light: `#742a2a`, background: `#fed7d7`) | Wrong answers, error tips |
| Info | text `#3c366b`, background `#ebf4ff` | "Try it" and info tips |
| Focus ring | `#ed8936` | Keyboard focus outline (3px) |

Don't add new colours for the main layout. Small accent gradients for cards and step labels are fine, as long as the header, tabs and background use the brand gradient.

### Fonts

| Use | Font stack |
|---|---|
| All text | `'Segoe UI', Tahoma, Geneva, Verdana, sans-serif` |
| Code | `'Courier New', Consolas, monospace` |

Don't load fonts from Google Fonts or elsewhere. The stacks above are already installed on student machines, and the pages keep working offline.

### Layout

- One white card, at most `960px` wide, centred, with a `20px` corner radius and a soft shadow.
- Header first, then the tab bar (when there is more than one section), then the content, then the footer.
- The page must be readable at phone width without sideways scrolling.

---

## 6. Word list

Use these words consistently, in file names, titles and outlines.

| Use | Not | Meaning |
|---|---|---|
| **Playbook** | play, interactive guide, interactive playbook, practice | An interactive HTML page for exploring a topic |
| **Playbook & Quiz** (title) / `playbook_quiz` (file) | playbook_and_quiz, play_and_quiz, playbook quiz | A playbook with a graded quiz at the end |
| **Quiz** | test, check (for weekly quizzes) | Graded weekly questions |
| **Final Test** | final exam, final quiz | The end-of-year test |
| **Lab** | exercise, practice lab | In-class guided practice, submitted for points |
| **Assignment** | homework, programming assignment, PA | Graded take-home programming work |
| **Skeleton** | starter, template (for students) | Notebook with function stubs for students to complete |
| **Concepts** | lecture notebook | Colab notebook that teaches a topic |
| **Slides** | presentation, PPT, deck | Lecture slides |
| **Notes** | lecture notes, summary | Markdown version of a lecture |
| **Weekly Outline** | week plan, week summary | The one-page plan for a class week |
| **One Pager** (title) / `one_pager` (file) | cheat sheet, summary card, infographic | A one-page `.png` visual summary of a topic |
| **Weekly Planner** | syllabus, schedule | The full-year schedule |
| **Help Session** | office hours, homework help | Wednesday support session |

---

## 7. Templates

New content starts from these files:

| Template | Use for |
|---|---|
| [`templates/playbook_quiz_template.html`](templates/playbook_quiz_template.html) | Any new playbook, quiz, or playbook & quiz |
| [`templates/weekly_outline_template.md`](templates/weekly_outline_template.md) | Any new weekly outline |

How to use them:

1. Copy the template.
2. Rename the copy using the naming pattern in section 2.
3. Replace everything marked `{{LIKE_THIS}}`.

---

## 8. Rolling it out

| Step | When | What |
|---|---|---|
| 1 | Now | Approve this guide. New files follow it from then on. |
| 2 | Now | Automatic checks reject new files that break this guide (see section 9). New files go in the **current** folders (`Quizzes/`, `Labs/`, `Play/`…). |
| 3 | Done | Existing files renamed with `tools/apply_renames.py`; links inside the repo were rewritten. The full old → new list is in `tools/rename_map.csv`. |
| 4 | Now | Update Google Classroom links using `tools/rename_map.csv`. |
| 5 | Later | Rebrand the contents of existing files (titles, headers, footers, colours); rename folders to lowercase; merge the duplicate notebooks in `colab_notebooks/` and `skeletons_programming_assignments/`; remove `week7_outline_v2.md`. |

---

## 9. Automatic checks

Every **new** file is fully checked against this guide. A **renamed** file gets the name check only, because its contents are rebranded separately (section 8, step 5).

### What is checked

| File | Checks |
|---|---|
| Every new file | Lowercase name with `_` between words, no spaces, no `python101_` prefix, no `_v2`/`_final` suffixes, right folder for its type, right extension for its type |
| Weekly outlines | Named `week<N>_outline.md` |
| HTML pages | `<title>` starts with `Python 101 · ` and has no week or quiz number; brand strip; footer with tagline; brand font; brand gradient; no Google Fonts |
| Markdown files | Standard header (first lines) and footer (last line) |
| Notebooks | First cell has the standard header; last cell has the footer |

Not checked: `data/`, `templates/`, `tools/`, `.github/`, `README.md`, `BRANDING.md`, `LICENSE`. Final project files get the name check only.

### Where it runs

| Layer | When | What happens to a non-conforming file |
|---|---|---|
| **Commit hook** (`.githooks/pre-commit`) | On `git commit`, on your own machine | The commit is refused, with a list of what to fix |
| **GitHub Action** (`.github/workflows/branding-check.yml`) | On every push and pull request | The check turns red on GitHub. With branch protection on (below), the change can't be merged into `main` |

**One-time setup for each person who clones the repo** (turns on the commit hook):

```
git config core.hooksPath .githooks
```

**One-time setup for the repo owner** (makes GitHub reject non-conforming changes):

1. Go to **Settings → Branches → Add branch protection rule** for `main`.
2. Tick **Require a pull request before merging**.
3. Tick **Require status checks to pass before merging** and select **Branding check**.

**Run the check yourself on any file:**

```
python tools/check_branding.py Quizzes/07_6_lists_mixed_nested_2d_playbook_quiz.html
```
