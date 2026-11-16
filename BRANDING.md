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

---

## 1. Decisions to approve

| # | Decision | Proposal | Why |
|---|---|---|---|
| 1 | How files are numbered | By **topic** (chapter + section, e.g. `07_6`), not by week | Week numbers shift every year with holidays; topic numbers already appear in the weekly planner and never change |
| 2 | Visual style for HTML pages | The **purple gradient** style (Segoe UI font) | About 22 of the 37 HTML pages already use it, including the newest quizzes |
| 3 | Tagline | **"Empowering Minds, Inspiring Generosity."** | Already used in the footer of the newest quizzes |
| 4 | When existing files are renamed | Once, **during the summer break**, with a script that also fixes every link | GitHub does not redirect renamed files, so links in outlines and Google Classroom would break mid-year |

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
| `notes` | Lecture notes in Markdown | `.md` | `presentations/` |
| `playbook` | Interactive page for exploring, no graded quiz | `.html` | `playbooks/` |
| `playbook_quiz` | Interactive page **with** a graded quiz | `.html` | `quizzes/` |
| `quiz` | Quiz only | `.html` / `.pdf` | `quizzes/` |
| `lab` | In-class lab | `.ipynb` / `.md` / `.html` | `labs/` |
| `concepts` | Colab notebook that teaches the topic | `.ipynb` | `notebooks/` |
| `skeleton` | Starter notebook for programming exercises | `.ipynb` | `notebooks/` |
| `assignment` | Graded programming assignment | `.ipynb` / `.md` | `assignments/` |

### Examples (current name → new name)

| Current | New |
|---|---|
| `Quizzes/python101_lists_mixed_nested_2d_playbook_and_quiz.html` | `quizzes/07_6_lists_mixed_nested_2d_playbook_quiz.html` |
| `Quizzes/functions_intro_interactive_play_and_quiz.html` | `quizzes/05_1_functions_intro_playbook_quiz.html` |
| `Labs/Lab1_Typing_and_Running_Python_Code.ipynb` | `labs/01_0_typing_and_running_code_lab.ipynb` |
| `Labs/lab20_mixed_nested_2d_lists.ipynb` | `labs/07_6_lists_mixed_nested_2d_lab.ipynb` |
| `Labs/pet_shelter_solution.py` | `labs/10_0_oop_pet_shelter_lab_solution.py` |
| `presentations/8_1_More_About_Strings.pdf` | `presentations/08_1_more_about_strings_slides.pdf` |
| `presentations/7_6_python_mixed_and_nested_lists.md` | `presentations/07_6_lists_mixed_nested_notes.md` |
| `colab_notebooks/ch5_1_concepts_functions_introduction.ipynb` | `notebooks/05_1_functions_intro_concepts.ipynb` |
| `skeletons_programming_assignments/ch7_skeleton_lists_exercises.ipynb` | `notebooks/07_0_lists_skeleton.ipynb` |
| `Play/python_oop_playbook.html` | `playbooks/10_0_oop_playbook.html` |

### Items without a chapter

| Item | Pattern | Example |
|---|---|---|
| Weekly outline | `week_<WW>_outline.md` (two digits) | `week_01_outline.md`, `week_20_outline.md` |
| Weekly planner | `weekly_planner_<YYYY>_<YY>.md` | `weekly_planner_2026_27.md` |
| Course-wide item | `00_0_<topic>_<type>` | `00_0_colab_basics_slides.pdf`, `00_0_comprehensive_quiz.html` |
| Final project | Lives in `final_project/`, no chapter number | `final_project/auto_grader_design_slides.pdf` |
| Images for a deck | Folder named after the deck's topic | `presentations/images/07_6_lists_mixed_nested/` |

---

## 3. Folders

All folder names are lowercase.

| Folder | Holds | Replaces |
|---|---|---|
| `presentations/` | `slides`, `notes`, images | `presentations/` |
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

For weekly outlines, the title is `Week <N> Outline` (no zero padding in the heading itself: `Week 7 Outline`).

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
| 2 | Now | Add an automatic check that flags non-conforming file names, titles and footers whenever something is checked in. |
| 3 | Now | Remove clutter (`foo.txt` placeholders, duplicate notebooks, `week7_outline_v2.md`). |
| 4 | Summer break | Rename existing files and folders in one go with a script that also rewrites every link in the outlines. Update links in Google Classroom at the same time. |
