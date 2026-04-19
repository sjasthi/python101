# 🐍 Python 101 — Final Project: Student Progress Report Generator

**Learn and Help Program &nbsp;·&nbsp; [www.learnandhelp.com](https://www.learnandhelp.com)**

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
2. Rename it: `python101_progress_report.ipynb`
3. Upload both input CSV files to Colab using the **Files panel** on the left sidebar (click the 📁 folder icon → upload icon)
4. After uploading, the files will be available at:
   - `/content/python_101_scores.csv`
   - `/content/python_101_emails.csv`

> ⚠️ **Note:** Files uploaded to Colab are temporary. If your session disconnects, you will need to re-upload them before running again. This is normal — just re-upload and re-run.

### Downloading Your Output Files

After your program runs and creates the HTML files, you can download them from the Files panel:

```python
# Run this cell AFTER your program finishes to download all HTML files
from google.colab import files
import glob

for filepath in glob.glob('/content/*.html'):
    files.download(filepath)
```

---

## 📂 Input Files

Your program reads **two CSV files**. CSV stands for *Comma-Separated Values* — a plain text file where each row is one record and columns are separated by commas.

Open the files in the Colab Files panel (right-click → Open) to see what they look like before you start coding.

---

### File 1 — `python_101_scores.csv`

This file has a **special 3-row header** before the student data begins:

| Row # | What it contains |
|-------|-----------------|
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
> - Some students may have a blank last name
> - Some assignments may have no due date (blank)

---

### File 2 — `python_101_emails.csv`

This file has one row per student. Use the **student email** to match records between the two files.

| Column | Description |
|--------|-------------|
| `Last Name` | Student last name |
| `First Name` | Student first name |
| `Email Account` | Student email — **use this to link the two files** |
| `Parent1 Last Name` | |
| `Parent1 First Name` | |
| `Parent1 Email` | |
| `Parent2 Last Name` | May be blank — not every student registers a second parent |
| `Parent2 First Name` | |
| `Parent2 Email` | |

---

## 📤 Output Files

Your program must produce **two types** of HTML files and save them to `/content/`.

---

### Output 1 — Individual Student Report

**Filename format:** `python101_firstname_lastname.html`
*(e.g., `python101_ali_johnson.html`)*

One file per student. Each file must show:

- Program name: **Learn and Help**
- Course name *(derived from the scores filename at runtime — do not hardcode it)*
- Student name
- Student email
- Parent 1 name and email
- Parent 2 name and email *(skip this row entirely if Parent 2 is not on file)*
- A **table of all assignments** with columns: Assignment Name · Due Date · Score · Max Points · Status
- Any row where the score is **blank (missing) must be highlighted in red**
- A **totals row** at the bottom: total points earned, total points possible, percentage

---

### Output 2 — Instructor Overview

**Filename:** `python101_all_scores.html`

One file for the instructor. It must show:

- Summary stats: total students, number of assignments, total points possible, class average
- A **table with one row per student** showing: Name · Email · Points Earned · Total Possible · Percentage · Missing Assignment Count
- Rows for students who have **any missing assignments** must be highlighted in red

---

## ✅ Requirements Checklist

Check each box before you submit:

### Python Requirements *(this is what you are graded on)*

- [ ] Reads `python_101_scores.csv` correctly — parses the 3-row header to get assignment names, due dates, and max points
- [ ] Reads `python_101_emails.csv` correctly and builds a lookup by student email
- [ ] Matches parent info to students using the email address
- [ ] Treats blank score cells as 0 in calculations and marks them as "missing"
- [ ] Handles a blank last name without crashing
- [ ] Handles a missing Parent 2 without crashing
- [ ] Derives the course name from the filename at runtime — **do not hardcode "Python 101"**
- [ ] Derives assignment names, due dates, and max points from the file at runtime — **do not hardcode any of these**
- [ ] Generates one HTML file per student saved to `/content/`
- [ ] Generates the instructor overview HTML saved to `/content/`
- [ ] Uses **functions** — your code is broken into logical functions, not one giant block
- [ ] Uses **meaningful variable names**
- [ ] Includes **comments** explaining what each section does

### Output Requirements

- [ ] Individual report shows student info, parent info, and the assignment table
- [ ] Missing assignments are visually highlighted in red in all reports
- [ ] Instructor overview includes a summary and a table of all students
- [ ] All HTML files open correctly in a browser

---

## 📐 Suggested Program Structure

Organize your notebook into these cells. Each cell should have a heading comment:

```
Cell 1:  # Step 1 — Import libraries

Cell 2:  # Step 2 — Parse the scores CSV
         def parse_scores(filename): ...

Cell 3:  # Step 3 — Parse the emails CSV
         def parse_emails(filename): ...

Cell 4:  # Step 4 — Build individual student HTML
         def build_student_html(student, assignments, parents): ...

Cell 5:  # Step 5 — Build instructor overview HTML
         def build_instructor_html(students, assignments): ...

Cell 6:  # Step 6 — Run everything / write files

Cell 7:  # Step 7 — Download output files
```

---

## 💡 Python Hints

### Reading the scores CSV

```python
import csv

def parse_scores(filename):
    with open(filename, newline='', encoding='utf-8-sig') as f:
        rows = list(csv.reader(f))

    # The first 3 columns are student info, the rest are assignments
    META_COLS = 3

    header_row = rows[0]   # assignment names
    date_row   = rows[1]   # due dates
    points_row = rows[2]   # max points

    # Build a list of assignment dictionaries
    assignments = []
    for col in range(META_COLS, len(header_row)):
        name    = header_row[col].strip()
        due     = date_row[col].strip()   if col < len(date_row)   else ""
        pts_str = points_row[col].strip() if col < len(points_row) else ""

        try:
            max_pts = float(pts_str) if pts_str else None
        except ValueError:
            max_pts = None

        assignments.append({"name": name, "due": due, "max_pts": max_pts, "col": col})

    # Build a list of student dictionaries
    students = []
    for row in rows[3:]:              # student rows start at index 3
        if not any(row):              # skip completely empty rows
            continue
        last  = row[0].strip() if len(row) > 0 else ""
        first = row[1].strip() if len(row) > 1 else ""
        email = row[2].strip() if len(row) > 2 else ""

        scores = {}
        for a in assignments:
            col     = a["col"]
            raw     = row[col].strip() if col < len(row) else ""
            if raw == "":
                scores[col] = None          # missing
            else:
                try:
                    scores[col] = float(raw)
                except ValueError:
                    scores[col] = None

        students.append({
            "last": last, "first": first, "email": email, "scores": scores
        })

    return assignments, students
```

---

### Reading the emails CSV

```python
def parse_emails(filename):
    email_map = {}    # { student_email: { parent info } }

    with open(filename, newline='', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            key = row["Email Account"].strip()
            if not key:
                continue

            p1_name  = (row["Parent1 First Name"] + " " + row["Parent1 Last Name"]).strip()
            p1_email = row["Parent1 Email"].strip()
            p2_name  = (row["Parent2 First Name"] + " " + row["Parent2 Last Name"]).strip()
            p2_email = row["Parent2 Email"].strip()

            email_map[key] = {
                "p1_name":  p1_name,
                "p1_email": p1_email,
                "p2_name":  p2_name,
                "p2_email": p2_email,
            }

    return email_map
```

---

### Building a safe output filename

```python
import re

def make_filename(first, last):
    combined = f"{first}_{last}".strip("_").lower()
    combined = re.sub(r'[^a-z0-9]', '_', combined)   # replace special chars with _
    combined = re.sub(r'_+', '_', combined)           # collapse multiple underscores
    return f"python101_{combined}.html"

# Example:
# make_filename("Ali", "Johnson")    → "python101_ali_johnson.html"
# make_filename("Sam", "")          → "python101_sam.html"
```

---

### Deriving the course name from the filename

```python
import re
from pathlib import Path

def get_course_name(filepath):
    stem = Path(filepath).stem               # "python_101_scores"
    stem = re.sub(r'_scores$', '', stem)     # "python_101"
    return stem.replace('_', ' ').title()    # "Python 101"

# Example:
# get_course_name("/content/python_101_scores.csv")  → "Python 101"
```

---

### Writing an HTML file

```python
def write_file(filepath, html_content):
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html_content)
```

---

## 🎨 HTML Starter Templates

> 📌 You do **not** need to design the HTML yourself. The templates below are provided as a starting point.
> Your job is to **fill them in with real data from the CSV files using Python f-strings**.
> Focus on the Python — getting the right data into the right place.

---

### Template A — Individual Student Report

Study this template. Notice how Python variables (like `student_name`, `earned`, `pct`) are inserted inside `{ }` in the f-string.

```python
def build_student_html(student, assignments, parents, course_name):
    first      = student["first"]
    last       = student["last"]
    full_name  = f"{first} {last}".strip()
    email      = student["email"]

    # Calculate totals
    total_possible = sum(a["max_pts"] for a in assignments if a["max_pts"])
    earned = sum(
        student["scores"].get(a["col"]) or 0
        for a in assignments if a["max_pts"]
    )
    pct = (earned / total_possible * 100) if total_possible else 0
    missing_count = sum(1 for a in assignments if student["scores"].get(a["col"]) is None)

    # Parent info
    p1 = parents.get("p1_name", "Not on file")
    p1_email = parents.get("p1_email", "")
    p2 = parents.get("p2_name", "")
    p2_email = parents.get("p2_email", "")

    # Build the assignment table rows
    rows_html = ""
    for a in assignments:
        col      = a["col"]
        score    = student["scores"].get(col)
        max_pts  = a["max_pts"] or 0
        is_miss  = score is None
        display  = "Missing" if is_miss else str(score)
        max_disp = str(int(max_pts)) if max_pts == int(max_pts) else str(max_pts)

        # Red background for missing rows
        row_style = 'style="background:#fff0f0"' if is_miss else ""

        rows_html += f"""
        <tr {row_style}>
          <td>{a["name"]}</td>
          <td>{a["due"] if a["due"] else "—"}</td>
          <td>{"⚠ " + display if is_miss else display}</td>
          <td>{max_disp}</td>
        </tr>"""

    # Only show Parent 2 row if they exist
    p2_row = ""
    if p2 or p2_email:
        p2_row = f"<p><strong>Parent 2:</strong> {p2} &nbsp; {p2_email}</p>"

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>{course_name} — {full_name}</title>
  <style>
    body      {{ font-family: Arial, sans-serif; padding: 30px; max-width: 800px; margin: auto; }}
    h1        {{ color: #2c3e50; }}
    h2        {{ color: #555; font-size: 16px; margin-top: 28px; }}
    .info     {{ background: #f4f6f8; padding: 16px; border-radius: 8px; margin-bottom: 20px; }}
    table     {{ width: 100%; border-collapse: collapse; margin-top: 10px; }}
    th        {{ background: #2c3e50; color: white; padding: 10px; text-align: left; }}
    td        {{ padding: 9px 10px; border-bottom: 1px solid #ddd; }}
    .missing  {{ background: #fff0f0; color: #c0392b; font-weight: bold; }}
    .total-row{{ background: #eaf4fb; font-weight: bold; }}
    .footer   {{ margin-top: 40px; font-size: 12px; color: #aaa; text-align: center; }}
  </style>
</head>
<body>

  <h1>🐍 Learn and Help</h1>
  <p><strong>Course:</strong> {course_name}</p>

  <div class="info">
    <p><strong>Student Name:</strong> {full_name}</p>
    <p><strong>Student Email:</strong> {email}</p>
    <p><strong>Parent 1:</strong> {p1} &nbsp; {p1_email}</p>
    {p2_row}
    <p><strong>Missing Assignments:</strong> {missing_count}</p>
  </div>

  <h2>📋 Assignment Status</h2>
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
        <td>{earned:.1f}</td>
        <td>{total_possible:.0f} &nbsp; ({pct:.1f}%)</td>
      </tr>
    </tbody>
  </table>

  <div class="footer">
    Learn and Help Program · www.learnandhelp.com
  </div>

</body>
</html>"""

    return html
```

---

### Template B — Instructor Overview

```python
def build_instructor_html(students, assignments, course_name):
    total_possible = sum(a["max_pts"] for a in assignments if a["max_pts"])

    # Build one row per student
    rows_html = ""
    for s in students:
        full_name = f"{s['first']} {s['last']}".strip()
        earned = sum(s["scores"].get(a["col"]) or 0 for a in assignments if a["max_pts"])
        pct    = (earned / total_possible * 100) if total_possible else 0
        miss   = sum(1 for a in assignments if s["scores"].get(a["col"]) is None)

        # Red row if any assignments are missing
        row_style = 'style="background:#fff0f0"' if miss > 0 else ""

        rows_html += f"""
        <tr {row_style}>
          <td>{full_name}</td>
          <td>{s["email"]}</td>
          <td>{earned:.1f}</td>
          <td>{total_possible:.0f}</td>
          <td>{pct:.1f}%</td>
          <td>{"⚠ " + str(miss) if miss > 0 else "✅ 0"}</td>
        </tr>"""

    # Class average
    avg = sum(
        sum(s["scores"].get(a["col"]) or 0 for a in assignments if a["max_pts"])
        for s in students
    ) / len(students) if students else 0
    avg_pct = (avg / total_possible * 100) if total_possible else 0

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>{course_name} — Instructor Overview</title>
  <style>
    body    {{ font-family: Arial, sans-serif; padding: 30px; max-width: 960px; margin: auto; }}
    h1      {{ color: #2c3e50; }}
    .stats  {{ background: #f4f6f8; padding: 16px; border-radius: 8px; margin-bottom: 20px; }}
    table   {{ width: 100%; border-collapse: collapse; margin-top: 10px; }}
    th      {{ background: #2c3e50; color: white; padding: 10px; text-align: left; }}
    td      {{ padding: 9px 10px; border-bottom: 1px solid #ddd; }}
    .footer {{ margin-top: 40px; font-size: 12px; color: #aaa; text-align: center; }}
  </style>
</head>
<body>

  <h1>🐍 Learn and Help — {course_name}</h1>
  <h2>Instructor Overview</h2>

  <div class="stats">
    <p><strong>Total Students:</strong> {len(students)}</p>
    <p><strong>Total Assignments:</strong> {len(assignments)}</p>
    <p><strong>Points Possible:</strong> {total_possible:.0f}</p>
    <p><strong>Class Average:</strong> {avg:.1f} pts &nbsp; ({avg_pct:.1f}%)</p>
  </div>

  <table>
    <thead>
      <tr>
        <th>Student Name</th>
        <th>Email</th>
        <th>Points Earned</th>
        <th>Points Possible</th>
        <th>Percentage</th>
        <th>Missing</th>
      </tr>
    </thead>
    <tbody>
      {rows_html}
    </tbody>
  </table>

  <div class="footer">
    Learn and Help Program · www.learnandhelp.com
  </div>

</body>
</html>"""

    return html
```

---

## 📊 Grading Rubric

| Category | Points |
|----------|--------|
| Correctly reads and parses `scores.csv` — 3-row header, assignment names, due dates, max points | 15 |
| Correctly reads and parses `emails.csv` and matches parent info to students by email | 10 |
| Generates correct individual HTML report for every student | 20 |
| Missing assignments are treated as 0 in calculations AND flagged visually | 10 |
| Handles edge cases without crashing: blank last name, no Parent 2, blank scores | 10 |
| Generates correct instructor overview HTML | 15 |
| No hardcoded values — course name, assignment names, counts all come from the files | 10 |
| Code uses functions, meaningful variable names, and comments | 10 |
| **Total** | **100** |

---

## 📁 What to Submit

Upload **one file** to Google Classroom under the Final Project assignment:

- **`python101_progress_report.ipynb`** — your completed Colab notebook

> Make sure all cells have been run before you submit, so the output HTML files appear in the Files panel. Your instructor will run your notebook to verify it works.

---

*Python 101 · Learn and Help Program · [www.learnandhelp.com](https://www.learnandhelp.com)*
