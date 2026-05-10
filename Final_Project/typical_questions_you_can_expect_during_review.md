# 🐍 Python 101 Auto Grader — Industry Demo Questions

**Learn and Help Program · [www.learnandhelp.com](https://www.learnandhelp.com)**

These questions are organized by topic area. Industry experts may ask any of these during your project demo.
Be ready to walk through your code, explain your design choices, and think through edge cases on the spot.

---

## 📌 Category 1 — Requirements Understanding

1. **Walk me through what your program does from start to finish — pretend I have never seen it before.**
   *(Can you explain the big picture in 60 seconds?)*

2. **Why does the scores CSV have a 3-row header instead of a normal 1-row header? What does each of those three rows represent?**

3. **Your spec says "do not hardcode the course name." Why is that important? What would break if you hardcoded it?**

4. **The project requires two output files — one per student and one for the instructor. Who is the intended audience for each, and how did that shape what you put in each report?**

5. **What happens if a student is present in the scores file but is missing in the emails file? Does your program crash, skip the student, or handle it gracefully?**

---

## 🏗️ Category 2 — Design and Architecture

6. **You were asked to organize your notebook into 7 cells with specific functions. Why is it better to split code into functions rather than writing one giant block of code?**

7. **How does your `parse_scores` function hand off data to your `build_student_html` function? What data structure do you use to pass student information between them?**

8. **You use email address as the key to match students between the two CSV files. Why email and not name? What could go wrong if you matched by name instead?**

9. **Walk me through how you derive assignment names, due dates, and max points at runtime from the file. Show me the exact lines of code that do this.**

10. **If dictionaries were not allowed in this project, how would you solve the student-to-parent matching problem using only lists?**

---

## 🔍 Category 3 — Code Walkthrough

11. **Can you explain this specific code block?**
    ```python
    total_possible = sum(a["max_pts"] for a in assignments if a["max_pts"])
    ```
    *(What does `if a["max_pts"]` guard against? What happens if you remove it?)*

12. **Can you explain what this line does and why the `or 0` is there?**
    ```python
    earned = sum(s["scores"].get(a["col"]) or 0 for a in assignments if a["max_pts"])
    ```

13. **In your HTML template, you have this conditional:**
    ```python
    p2_row = ""
    if p2 or p2_email:
        p2_row = f"<p>..."
    ```
    Why do you check `p2 or p2_email` instead of just `p2`?

14. **Show me the part of your code that builds the red-highlighted rows for missing assignments. How does your code decide whether a row should be red?**

15. **How does your program compute the class average in the instructor overview? Walk me through the calculation step by step.**

---

## ⚠️ Category 4 — Edge Cases and Error Handling

16. **What happens if both first name and last name are blank for a student? Does your program crash or produce a reasonable output?**

17. **What happens if a student's score cell is blank — how do you detect that, and how does it affect the percentage calculation?**

18. **Some assignments in the scores file may have no due date. How does your code handle a blank due date without crashing or printing the word "None"?**

19. **What happens if the scores file has an assignment with no max points listed? Could that cause a division-by-zero error? How do you prevent it?**

20. **What if the emails file has a student listed that does not appear in the scores file at all? Does your program do anything with that record?**

---

## 🧪 Category 5 — Testing

21. **How did you test your `parse_scores` function? Did you test it with a small hand-crafted CSV before using the real file?**

22. **How did you test the edge case where a student has no Parent 2? Did you create a test case for that, or did you rely on the real data to cover it?**

23. **If I change the number of assignments in the scores file from 10 to 20, does your program still work correctly without any code changes? How do you know?**

---

## 🧠 Category 6 — Computational Thinking

24. **Your program reads the CSV file once and processes all students from that data. What would be the downside of opening and re-reading the file inside a loop for every student?**

25. **Imagine your program grows from 30 students to 300 students next year. Do you think your program would still work? What parts might slow down or break, and how would you improve them?**

---

*Python 101 · Learn and Help Program · www.learnandhelp.com*
