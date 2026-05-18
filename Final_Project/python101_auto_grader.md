# 🐍 Python 101 — Final Project: Python 101 Auto Grader

**Learn and Help Program  ·  [www.learnandhelp.com](https://www.learnandhelp.com)**

---

## 📌 Project Overview

You are building a **real-world Python program** that reads student grade data exported from Google Classroom and automatically generates HTML progress reports — one for each student and one for the instructor.

Parents can receive their child's individual report. Instructors can use the all-scores overview to track the whole class at a glance.

> 💡 This is exactly the kind of program that teachers, schools, and companies use every day. You are building something real!

---

## 🛠️ Environment — Google Colab

You will write and run your program in **Google Colab** using a Jupyter Notebook (`.ipynb` file).

### Setting Up Your Notebook

1. Open [colab.research.google.com](https://colab.research.google.com) and create a new notebook
2. Rename it: `python101_auto_grader.ipynb`
3. Upload both input CSV files to Colab using the **Files panel** on the left sidebar (click the 📁 folder icon → upload icon)
4. After uploading, the files will be available at:
   * `/content/python_101_scores.csv`
   * `/content/python_101_emails.csv`

> ⚠️ **Note:** Files uploaded to Colab are temporary. If your session disconnects, you will need to re-upload them before running again. This is normal — just re-upload and re-run.

---

## 📂 Input Files

Your program reads **two CSV files**. CSV stands for *Comma-Separated Values* — a plain text file where each row is one record and columns are separated by commas.

Open the files in the Colab Files panel (right-click → Open) to see what they look like before you start coding.

---

### File 1 — `python_101_scores.csv`

This file has a **special 3-row header** before the student data begins:

| Row # | What it contains |
| --- | --- |
| **Row 1** | Column names — the first 3 columns are `Last Name`, `First Name`, `Email Account`. Every column after that is an **assignment name**. |
| **Row 2** | Due dates — the first 3 values are label text, then the **due date** for each assignment. Some assignments may have no due date (blank). |
| **Row 3** | Max points — the first 3 values are label text, then the **maximum possible points** for each assignment. |
| **Row 4 onward** | One row per student — Last Name, First Name, Email, then their **score** for each assignment. |

```
Example structure (simplified to 3 assignments):

Row 1:  Last Name  | First Name | Email       | Lab 1 | Quiz 1 | Assignment 1
Row 2:  Date       |            |             | 7-Sep | 7-Sep  | 14-Sep
Row 3:  Points     |            |             | 10    | 7      | 25
Row 4:  Johnson    | Ali        | ali@...     | 10    | 6      |           ← blank = missing!
Row 5:  Smith      | Sam        | sam@...     | 8     | 7      | 20
```

> ⚠️ **Blank score = missing assignment.** Some cells will be empty — this means the student did not submit that assignment. Treat blank as **0** in score calculations, and flag it as **missing** in the report.

> ⚠️ **Other edge cases to handle:**
>
> * Some students may have a blank last name
> * Some assignments may have no due date (blank)
> * Some scores may be decimal numbers like `9.5`

---

### File 2 — `python_101_emails.csv`

This file has one row per student. Use the **student email** to match records between the two files.

| Column | Description |
| --- | --- |
| `Last Name` | Student last name |
| `First Name` | Student first name |
| `Email Account` | Student email — **use this to link the two files** |
| `Parent1 Last Name` |  |
| `Parent1 First Name` |  |
| `Parent1 Email` |  |
| `Parent2 Last Name` | May be blank — not every student registers a second parent |
| `Parent2 First Name` |  |
| `Parent2 Email` |  |

---

## 🗂️ Data Structures — What Your Program Builds

Before you start writing functions, it helps to understand **what data structures your program will create** from those CSV files. There are three main ones. Read this section carefully — understanding these will make the rest of the project much easier.

---

### 1. `assignments_list` — A List of Dictionaries

After reading the first three rows of the scores file, you will build a **list** where each item is a **dictionary** representing one assignment.

**Each assignment dictionary has three keys:**

| Key | Type | Example value |
| --- | --- | --- |
| `"assignment_name"` | string | `"Lab 1"` |
| `"due_date"` | string | `"7-Sep-25"` (or `""` if blank) |
| `"max_points"` | int | `10` |

**What it looks like in Python:**

```python
assignments_list = [
    {"assignment_name": "Lab 1",  "due_date": "7-Sep-25",  "max_points": 10},
    {"assignment_name": "Quiz 1", "due_date": "7-Sep-25",  "max_points": 7},
    {"assignment_name": "Assignment 1", "due_date": "14-Sep-25", "max_points": 25},
    # ... one entry per assignment column in the CSV
]
```

> 💡 **How to read a value from it:** `assignments_list[0]["assignment_name"]` gives you `"Lab 1"`.

---

### 2. `students_list` — A List of Dictionaries (with a nested dictionary!)

After reading rows 4 and beyond from the scores file, you will build a **list** where each item is a **dictionary** representing one student.

**Each student dictionary has four keys:**

| Key | Type | Example value |
| --- | --- | --- |
| `"last"` | string | `"Johnson"` |
| `"first"` | string | `"Ali"` |
| `"email"` | string | `"ali.johnson@learnandhelp.com"` |
| `"scores"` | **dictionary** | `{"Lab 1": 10, "Quiz 1": 6, "Assignment 1": None}` |

The `"scores"` value is itself a **dictionary** that maps each assignment name to the student's score. A score of `None` means the assignment was not submitted (the cell was blank in the CSV).

**What it looks like in Python:**

```python
students_list = [
    {
        "last":  "Johnson",
        "first": "Ali",
        "email": "ali.johnson@learnandhelp.com",
        "scores": {
            "Lab 1":        10,
            "Quiz 1":       6,
            "Assignment 1": None   # ← blank in CSV = not submitted
        }
    },
    {
        "last":  "Smith",
        "first": "Sam",
        "email": "sam.smith@learnandhelp.com",
        "scores": {
            "Lab 1":        8,
            "Quiz 1":       7,
            "Assignment 1": 20
        }
    }
]
```

> 💡 **How to get Ali's score on Lab 1:** `students_list[0]["scores"]["Lab 1"]` → `10`
>
> 💡 **How to get Ali's score on Assignment 1:** `students_list[0]["scores"]["Assignment 1"]` → `None` (missing!)
>
> 💡 **Tip for missing scores:** Use `.get("Lab 1")` instead of `["Lab 1"]` — it safely returns `None` if the key doesn't exist.

---

### 3. `email_lookup_tbl` — A Dictionary of Dictionaries

After reading the emails file, you will build a **dictionary** keyed by **student email**. This lets you quickly look up parent info for any student.

**Each value is a dictionary with four keys:**

| Key | Type | Example value |
| --- | --- | --- |
| `"p1_name"` | string | `"Robert Johnson"` |
| `"p1_email"` | string | `"r.johnson@email.com"` |
| `"p2_name"` | string | `"Maria Johnson"` (or `""` if no Parent 2) |
| `"p2_email"` | string | `"m.johnson@email.com"` (or `""` if no Parent 2) |

**What it looks like in Python:**

```python
email_lookup_tbl = {
    "ali.johnson@learnandhelp.com": {
        "p1_name":  "Robert Johnson",
        "p1_email": "r.johnson@email.com",
        "p2_name":  "Maria Johnson",
        "p2_email": "m.johnson@email.com"
    },
    "sam.smith@learnandhelp.com": {
        "p1_name":  "David Smith",
        "p1_email": "d.smith@email.com",
        "p2_name":  "",      # ← no Parent 2 on file
        "p2_email": ""
    }
}
```

> 💡 **How to look up Ali's parents in Step 6:**
> ```python
> parents = email_lookup_tbl.get("ali.johnson@learnandhelp.com", {})
> # parents is now {"p1_name": "Robert Johnson", ...}
> ```
> Passing `{}` as the default means if the email isn't found, you get an empty dictionary — no crash!

---

### How the Three Data Structures Connect

```
CSV Files
   │
   ├── python_101_scores.csv ──► process_scores()
   │                                │
   │                                ├── assignments_list  (used in Steps 4, 5, 6)
   │                                └── students_list     (used in Steps 4, 5, 6)
   │
   └── python_101_emails.csv ──► parse_emails()
                                     │
                                     └── email_lookup_tbl (used in Step 6)
                                              │
                                              └── for each student, look up parents
                                                  and pass them into build_student_html()
```

---

## 📤 Output Files

Your program must produce **two types** of HTML files and save them to `/content/`.

---

### Output 1 — Individual Student Report

**Filename format:** `python101_firstname_lastname.html`
*(e.g., `python101_ali_johnson.html`)*

One file per student. Each file must show:

* Program name: **Learn and Help**
* Course name
* Student name and email
* Parent 1 name and email
* Parent 2 name and email *(skip this row entirely if Parent 2 is not on file)*
* A **table of all assignments** with columns: Assignment Name · Due Date · Score · Max Points
* Any row where the score is **missing (None) must be highlighted in red**
* A **totals row** at the bottom: total points earned, total points possible, percentage

---

### Output 2 — Instructor Overview

**Filename:** `python101_all_scores.html`

One file for the instructor. It must show:

* Summary stats: total students, number of assignments, total points possible, class average
* A **table with one row per student** showing: Name · Email · Points Earned · Total Possible · Percentage · Missing Count
* Rows for students who have **any missing assignments** must be highlighted in red

---

## 📐 Notebook Structure — 7 Coding Cells

Organize your notebook into exactly **7 cells**. Here is what each cell should do:

---

### Cell 1 — Define Constants

**What to put here:** Define the input filenames and the course name as variables at the top of your notebook. This makes them easy to find and change in one place.

```python
#@title Step 1: Define constants

INPUT_SCORES_FILE_NAME = "python_101_scores.csv"
INPUT_EMAILS_FILE_NAME = "python_101_emails.csv"
COURSE_NAME            = "Python 101"

print("Score File  : ", INPUT_SCORES_FILE_NAME)
print("Email File  : ", INPUT_EMAILS_FILE_NAME)
print("Course Name : ", COURSE_NAME)
```

> ✏️ **Your task:** No coding required here — just run this cell so the constants are available to all other cells.

---

### Cell 2 — Parse the Scores CSV (`process_scores`)

**What to put here:** Define a function called `process_scores(filename)` that reads the scores CSV and returns two things: `assignments_list` and `students_list`.

**Step-by-step plan:**
1. Open the file and read all lines into a list called `scores_lines`
2. **Line 1 (index 0):** Split by comma, skip the first 3 tokens → these are your `assignment_names`
3. **Line 2 (index 1):** Split by comma, skip the first 3 tokens → these are your `due_dates`
4. **Line 3 (index 2):** Split by comma, skip the first 3 tokens → convert each to `int` → these are your `max_points`
5. **Build `assignments_list`:** Loop using `range(len(assignment_names))` and build a dictionary for each assignment with keys `"assignment_name"`, `"due_date"`, `"max_points"`. Make sure to `.strip()` the name and due date to remove extra spaces.
6. **Lines 4+ (index 3 onward):** These are student rows. For each line:
   - Split by comma
   - Get `last` (token 0), `first` (token 1), `email` (token 2) — `.strip()` each one
   - Get the score tokens (everything from index 3 onward)
   - Build `scores_dict`: loop through `assignment_names`, use the stripped name as the key, convert the score to `float` if not blank, otherwise use `None`
   - Build `student_dict` with keys `"last"`, `"first"`, `"email"`, `"scores"`
   - Append to `students_list`
7. Return `assignments_list, students_list`

> ⚠️ **Important:** Use `float(score_str)` when converting scores — not `int()` — because some scores may be decimals like `9.5`. A blank score cell should become `None`.

> ⚠️ **Important:** Use `.strip()` on assignment name keys in `scores_dict` so they exactly match the keys in `assignments_list`. If one is `"Lab 1"` and the other is `"Lab 1 "` (with a trailing space), the lookup will fail.

---

### Cell 3 — Parse the Emails CSV (`parse_emails`)

**What to put here:** Define a function called `parse_emails(filename)` that reads the emails CSV and returns `email_lookup_tbl` — a dictionary keyed by student email.

**Step-by-step plan:**
1. Open the file and read all lines
2. Skip the first line (it's the header row)
3. For each remaining line:
   - Split by comma
   - Get `student_email` from token index 2 (`.strip()` it)
   - Build a dictionary with keys `"p1_name"`, `"p1_email"`, `"p2_name"`, `"p2_email"` from the remaining tokens (`.strip()` each one)
   - Add it to `email_lookup_tbl` with `student_email` as the key
4. Return `email_lookup_tbl`

> 💡 **Tip:** Parent 1 info is at token indices 3–5. Parent 2 info is at indices 6–8. Combine first and last name with a space for `p1_name` and `p2_name`.

---

### Cell 4 — Build Student HTML Report (`build_student_html`)

**What to put here:** Define a function called `build_student_html(student, assignments, parents, course_name)` that takes one student's data and returns a complete HTML string.

**Arguments it receives:**
- `student` — one student dictionary from `students_list` (has keys `"first"`, `"last"`, `"email"`, `"scores"`)
- `assignments` — the full `assignments_list` (each item has `"assignment_name"`, `"due_date"`, `"max_points"`)
- `parents` — one entry from `email_lookup_tbl` (has keys `"p1_name"`, `"p1_email"`, `"p2_name"`, `"p2_email"`)
- `course_name` — the `COURSE_NAME` constant from Cell 1

**Step-by-step plan:**
1. Extract `first`, `last`, `email` from `student`
2. Calculate `total_possible` by summing `a["max_points"]` for all assignments
3. Calculate `earned` by summing each score — use `student["scores"].get(a["assignment_name"]) or 0` (this treats `None` as 0)
4. Calculate `percentage` from `earned / total_possible * 100`
5. Count `missing_count` — how many scores are `None`
6. Get parent info using `.get()` with safe defaults (e.g. `parents.get("p1_name", "Not on file")`)
7. Build the assignment table rows in a loop — for each assignment, look up the score, decide if it's missing, format the display, and add a red CSS class if missing
8. Assemble and return the full HTML string using an f-string

> 💡 **Tip for formatting scores:** Check `if score == int(score)` to display `10.0` as `"10"` and `9.5` as `"9.5"`.

See the **HTML Template A** section below for the complete starter code.

---

### Cell 5 — Build Instructor HTML Report (`build_instructor_html`)

**What to put here:** Define a function called `build_instructor_html(students, assignments, course_name)` that takes the full class data and returns a complete HTML string.

**Arguments it receives:**
- `students` — the full `students_list`
- `assignments` — the full `assignments_list`
- `course_name` — the `COURSE_NAME` constant from Cell 1

**Step-by-step plan:**
1. Calculate `total_possible` by summing all `max_points`
2. Loop through all students. For each student:
   - Calculate their `earned` points and `percentage`
   - Count their `missing_count`
   - Format a table row — highlight red if they have missing work
3. Calculate class-level stats: number of students, number of assignments, class average
4. Count how many students have at least one missing assignment
5. Assemble and return the full HTML string

See the **HTML Template B** section below for the complete starter code.

---

### Cell 6 — Run Everything (`main`)

**What to put here:** Define a function called `main()` that calls all the functions above in the right order and writes the HTML files to disk. Then call `main()` at the bottom of the cell.

**Step-by-step plan:**
1. Create a written_files list to keep track off all the files generated
2. Call `process_scores(INPUT_SCORES_FILE_NAME)` → get `assignments` and `students`
3. Call `parse_emails(INPUT_EMAILS_FILE_NAME)` → get `email_lookup`
4. Loop through every student:
   - Look up their parents: `parents = email_lookup.get(student["email"], {})`
   - Call `build_student_html(student, assignments, parents, COURSE_NAME)` to get the HTML string
   - Build the output filename: `"python101_" + first + "_" + last + ".html"` (lowercase, underscores)
   - Write the HTML string to `/content/<filename>` using `open()` + `.write()`
   - Append the output filename to written_files list
5. Call `build_instructor_html(students, assignments, COURSE_NAME)` and write it to `/content/python101_all_scores.html`. Append the output filename to written_files list
6. Return the list of all written filepaths (return written_files)

> 💡 **Why pass `{}` as the default in `.get(email, {})`?** If a student's email is not found in the email file, you get an empty dictionary. Then inside `build_student_html`, the `.get("p1_name", "Not on file")` calls handle it gracefully — no crash.

---

### Cell 7 — Download Output Files

**What to put here:** Use the Colab `files` library to trigger a download of every HTML file that was written in Cell 6. This cell uses a special Colab library — you don't need to change it.

```python
# Step 7 - Download all output HTML files
# Run this cell AFTER Cell 6 finishes.
# Tip: Colab may ask you to allow multiple downloads — click Allow.

from google.colab import files

print("Downloading", len(all_html_files), "file(s)...\n")

for filepath in sorted(all_html_files):
    display_name = filepath.split("/")[-1]
    print("  Downloading:", display_name)
    files.download(filepath)

print("\nAll downloads triggered!")
```

> ✏️ **Your task:** No coding required here — this cell uses `all_html_files`, the list returned by `main()` in Cell 6. Just run it after Cell 6 finishes.

---

## 🎨 HTML Starter Templates

> 📌 You do **not** need to design the HTML yourself. The templates below are provided as a starting point.
> Your job is to **fill them in with real data from the CSV files**.
> Focus on the Python — getting the right data into the right place.
>
> **Key reminder:** The templates use the data structure keys we defined earlier:
> - `a["assignment_name"]`, `a["due_date"]`, `a["max_points"]` for assignments
> - `student["first"]`, `student["last"]`, `student["email"]`, `student["scores"]` for students
> - `parents["p1_name"]`, `parents["p1_email"]`, etc. for parent info

---

### Template A — Individual Student Report

```python
def build_student_html(student, assignments, parents, course_name):
    """Return an HTML string for one student's progress report."""

    # --- Student identity ---
    first     = student["first"]
    last      = student["last"]
    full_name = f"{first} {last}".strip()
    email     = student["email"]

    # --- Score calculations ---
    total_possible = sum(a["max_points"] for a in assignments)

    # None scores count as 0 in the total
    earned = sum(
        student["scores"].get(a["assignment_name"]) or 0
        for a in assignments
    )
    percentage    = (earned / total_possible * 100) if total_possible else 0
    missing_count = sum(
        1 for a in assignments
        if student["scores"].get(a["assignment_name"]) is None
    )

    # --- Parent info ---
    p1_name  = parents.get("p1_name",  "Not on file")
    p1_email = parents.get("p1_email", "")
    p2_name  = parents.get("p2_name",  "")
    p2_email = parents.get("p2_email", "")

    # Only show Parent 2 row if there is data for them
    if p2_name or p2_email:
        p2_row = f"<p><strong>Parent 2:</strong> {p2_name} &nbsp; {p2_email}</p>"
    else:
        p2_row = ""

    # Missing badge
    if missing_count > 0:
        missing_badge = f'<span class="badge-warn">Missing: {missing_count}</span>'
    else:
        missing_badge = '<span class="badge-ok">None</span>'

    # --- Build assignment table rows ---
    rows_html = ""
    for a in assignments:
        score      = student["scores"].get(a["assignment_name"])   # float or None
        max_pts    = a["max_points"]
        due_date   = a["due_date"] if a["due_date"] else "--"
        is_missing = (score is None)

        # Format score for display
        if is_missing:
            score_display = "MISSING"
        elif score == int(score):
            score_display = str(int(score))    # show 10.0 as "10"
        else:
            score_display = str(score)         # show 9.5 as "9.5"

        # Format max points for display
        max_display = str(int(max_pts)) if max_pts == int(max_pts) else str(max_pts)

        # Red row for missing assignments
        row_class = 'class="missing-row"' if is_missing else ""

        rows_html += f"""
        <tr {row_class}>
          <td>{a["assignment_name"]}</td>
          <td>{due_date}</td>
          <td>{score_display}</td>
          <td>{max_display}</td>
        </tr>"""

    # Format totals
    earned_str = str(int(earned)) if earned == int(earned) else str(round(earned, 1))
    pct_str    = str(round(percentage, 1))

    # --- Assemble the full HTML page ---
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{course_name} — {full_name}</title>
  <style>
    body             {{ font-family: Arial, sans-serif; padding: 30px; max-width: 900px; margin: auto; background: #fafafa; }}
    h1               {{ color: #2c3e50; margin-bottom: 2px; }}
    .subtitle        {{ color: #555; margin-top: 4px; font-size: 15px; }}
    h2               {{ color: #444; font-size: 16px; margin-top: 28px; }}
    .info-box        {{ background: #f4f6f8; padding: 16px 20px; border-radius: 8px; border-left: 4px solid #2c3e50; margin-bottom: 24px; }}
    .info-box p      {{ margin: 6px 0; font-size: 14px; }}
    .badge-ok        {{ background: #27ae60; color: white; padding: 2px 10px; border-radius: 10px; font-size: 13px; }}
    .badge-warn      {{ background: #e74c3c; color: white; padding: 2px 10px; border-radius: 10px; font-size: 13px; }}
    table            {{ width: 100%; border-collapse: collapse; font-size: 13px; margin-top: 6px; }}
    th               {{ background: #2c3e50; color: white; padding: 10px 12px; text-align: left; }}
    td               {{ padding: 8px 12px; border-bottom: 1px solid #e0e0e0; }}
    tr:hover td      {{ background: #f0f4f8; }}
    .missing-row td  {{ background: #fff0f0; color: #c0392b; font-weight: bold; }}
    .total-row       {{ background: #eaf4fb; font-weight: bold; }}
    .total-row td    {{ border-top: 2px solid #2c3e50; }}
    .footer          {{ margin-top: 40px; font-size: 12px; color: #aaa; text-align: center; border-top: 1px solid #eee; padding-top: 14px; }}
    a                {{ color: #2980b9; }}
  </style>
</head>
<body>
  <h1>Learn and Help</h1>
  <p class="subtitle"><strong>Course:</strong> {course_name}</p>

  <div class="info-box">
    <p><strong>Student Name:</strong> {full_name}</p>
    <p><strong>Student Email:</strong> <a href="mailto:{email}">{email}</a></p>
    <p><strong>Parent 1:</strong> {p1_name} &nbsp; <a href="mailto:{p1_email}">{p1_email}</a></p>
    {p2_row}
    <p><strong>Missing Assignments:</strong> {missing_badge}</p>
  </div>

  <h2>Assignment Status</h2>
  <table>
    <thead>
      <tr>
        <th>Assignment</th>
        <th>Due Date</th>
        <th>Score</th>
        <th>Max Points</th>
      </tr>
    </thead>
    <tbody>
      {rows_html}
      <tr class="total-row">
        <td colspan="2">TOTAL</td>
        <td>{earned_str} pts</td>
        <td>{int(total_possible)} pts &nbsp; | &nbsp; {pct_str}%</td>
      </tr>
    </tbody>
  </table>

  <div class="footer">
    Learn and Help Program · <a href="https://www.learnandhelp.com">www.learnandhelp.com</a>
  </div>
</body>
</html>"""

    return html
```

---

### Template B — Instructor Overview

```python
def build_instructor_html(students, assignments, course_name):
    """Return an HTML string for the instructor overview report."""

    # Total points possible
    total_possible = sum(a["max_points"] for a in assignments)

    # --- Build one table row per student ---
    rows_html         = ""
    all_earned_scores = []

    for student in students:
        full_name = f"{student['first']} {student['last']}".strip()

        # Points earned — None counts as 0
        earned = sum(
            student["scores"].get(a["assignment_name"]) or 0
            for a in assignments
        )
        all_earned_scores.append(earned)

        percentage    = (earned / total_possible * 100) if total_possible else 0
        missing_count = sum(
            1 for a in assignments
            if student["scores"].get(a["assignment_name"]) is None
        )

        # Red row for any student with missing work
        row_class = 'class="missing-row"' if missing_count > 0 else ""

        if missing_count > 0:
            missing_cell = f'<span class="badge-warn">Missing: {missing_count}</span>'
        else:
            missing_cell = '<span class="badge-ok">0</span>'

        earned_str = str(int(earned)) if earned == int(earned) else str(round(earned, 1))
        pct_str    = str(round(percentage, 1))

        rows_html += f"""
        <tr {row_class}>
          <td>{full_name}</td>
          <td>{student["email"]}</td>
          <td>{earned_str}</td>
          <td>{int(total_possible)}</td>
          <td>{pct_str}%</td>
          <td>{missing_cell}</td>
        </tr>"""

    # --- Class-level summary stats ---
    num_students          = len(students)
    num_assignments       = len(assignments)
    class_avg             = sum(all_earned_scores) / num_students if num_students else 0
    class_avg_pct         = (class_avg / total_possible * 100) if total_possible else 0
    students_with_missing = sum(
        1 for s in students
        if any(s["scores"].get(a["assignment_name"]) is None for a in assignments)
    )

    avg_str     = str(round(class_avg, 1))
    avg_pct_str = str(round(class_avg_pct, 1))

    # --- Assemble the full HTML page ---
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{course_name} — Instructor Overview</title>
  <style>
    body            {{ font-family: Arial, sans-serif; padding: 30px; max-width: 1100px; margin: auto; background: #fafafa; }}
    h1              {{ color: #2c3e50; margin-bottom: 2px; }}
    .subtitle       {{ color: #555; margin-top: 4px; font-size: 15px; }}
    .stats          {{ display: flex; gap: 16px; flex-wrap: wrap; margin: 24px 0; }}
    .stat-card      {{ background: #f4f6f8; border-left: 4px solid #2c3e50; border-radius: 8px; padding: 14px 20px; min-width: 160px; }}
    .stat-card .label {{ font-size: 12px; color: #888; text-transform: uppercase; }}
    .stat-card .value {{ font-size: 24px; font-weight: bold; color: #2c3e50; }}
    .badge-ok       {{ background: #27ae60; color: white; padding: 2px 10px; border-radius: 10px; font-size: 13px; }}
    .badge-warn     {{ background: #e74c3c; color: white; padding: 2px 10px; border-radius: 10px; font-size: 13px; }}
    table           {{ width: 100%; border-collapse: collapse; font-size: 13px; margin-top: 6px; }}
    th              {{ background: #2c3e50; color: white; padding: 10px 12px; text-align: left; }}
    td              {{ padding: 8px 12px; border-bottom: 1px solid #e0e0e0; }}
    tr:hover td     {{ background: #f0f4f8; }}
    .missing-row td {{ background: #fff0f0; color: #c0392b; font-weight: bold; }}
    .footer         {{ margin-top: 40px; font-size: 12px; color: #aaa; text-align: center; border-top: 1px solid #eee; padding-top: 14px; }}
    a               {{ color: #2980b9; }}
  </style>
</head>
<body>
  <h1>Learn and Help</h1>
  <p class="subtitle"><strong>Course:</strong> {course_name} &nbsp;|&nbsp; Instructor Overview</p>

  <div class="stats">
    <div class="stat-card">
      <div class="label">Students</div>
      <div class="value">{num_students}</div>
    </div>
    <div class="stat-card">
      <div class="label">Assignments</div>
      <div class="value">{num_assignments}</div>
    </div>
    <div class="stat-card">
      <div class="label">Max Points</div>
      <div class="value">{int(total_possible)}</div>
    </div>
    <div class="stat-card">
      <div class="label">Class Avg</div>
      <div class="value">{avg_str} ({avg_pct_str}%)</div>
    </div>
    <div class="stat-card">
      <div class="label">With Missing</div>
      <div class="value">{students_with_missing}</div>
    </div>
  </div>

  <table>
    <thead>
      <tr>
        <th>Student Name</th>
        <th>Email</th>
        <th>Points Earned</th>
        <th>Points Possible</th>
        <th>Grade %</th>
        <th>Missing</th>
      </tr>
    </thead>
    <tbody>
      {rows_html}
    </tbody>
  </table>

  <div class="footer">
    Learn and Help Program · <a href="https://www.learnandhelp.com">www.learnandhelp.com</a>
  </div>
</body>
</html>"""

    return html
```

---

## ✅ Requirements Checklist

Check each box before you submit:

### Python Requirements *(this is what you are graded on)*

* Reads `python_101_scores.csv` correctly — parses the 3-row header to get assignment names, due dates, and max points
* Builds `assignments_list` correctly — each item is a dictionary with keys `"assignment_name"`, `"due_date"`, `"max_points"`
* Builds `students_list` correctly — each item is a dictionary with keys `"first"`, `"last"`, `"email"`, `"scores"`
* Scores are stored as `float` (or `None` for blank) — not as raw strings
* Reads `python_101_emails.csv` and builds `email_lookup_tbl` keyed by student email
* Matches parent info to students using the email address
* Treats `None` scores as 0 in calculations and marks them as "MISSING" in the report
* Handles a blank last name without crashing
* Handles a missing Parent 2 without crashing
* Handles decimal scores like `9.5` without crashing
* Generates one HTML file per student saved to `/content/`
* Generates the instructor overview HTML saved to `/content/`
* Uses **functions** — your code is broken into logical functions, not one giant block
* Uses **meaningful variable names** and the correct key names (`"assignment_name"`, `"due_date"`, `"max_points"`, `"first"`, `"last"`)
* Includes **comments** explaining what each section does

### Output Requirements

* Individual report shows student info, parent info, and the assignment table
* Missing assignments are visually highlighted in red in all reports
* Instructor overview includes summary stat cards and a table of all students
* All HTML files open correctly in a browser

---

## 📊 Grading Rubric

| Category | Points |
| --- | --- |
| Correctly reads and parses `scores.csv` — 3-row header, assignment names, due dates, max points | 15 |
| Builds correct `assignments_list` and `students_list` data structures with proper keys | 10 |
| Correctly reads and parses `emails.csv` and matches parent info to students by email | 10 |
| Generates correct individual HTML report for every student | 20 |
| Missing assignments are treated as 0 in calculations AND flagged visually | 10 |
| Handles edge cases without crashing: blank last name, no Parent 2, blank scores, decimal scores | 10 |
| Generates correct instructor overview HTML with summary stats | 15 |
| Code uses functions, meaningful variable names, correct key names, and comments | 10 |
| **Total** | **100** |

---

## 📁 What to Submit

Upload **one file** to Google Classroom under the Final Project assignment:

* **`python101_auto_grader.ipynb`** — your completed Colab notebook

> Make sure all cells have been run before you submit. Your instructor will run your notebook to verify it works.

---

*Python 101 · Learn and Help Program · [www.learnandhelp.com](https://www.learnandhelp.com)*
