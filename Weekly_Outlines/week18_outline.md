# Week 18: List Unpacking and Slicing

**Course:** Python 101  
**Program:** Learn and Help  
**Instructor:** Siva R Jasthi  
**Institution:** Metropolitan State University

---

## 📚 Topics Covered

- List Unpacking
- List Slicing with `[start:stop:step]`
- Negative Indexing
- Common Slicing Patterns

---

## 📖 Learning Materials

### Presentations

**Markdown Presentation:**  
https://github.com/sjasthi/python101/blob/main/presentations/7_4_python_lists_unpacking_and_slicing.md

**PDF Presentation:**  
https://github.com/sjasthi/python101/blob/main/presentations/7_4_python_lists_Unpacking_and_Slicing.pdf

### Google Colab Notebooks

**Concepts Notebook:**  
https://github.com/sjasthi/python101/blob/main/colab_notebooks/ch7_concepts_list_intro_1.ipynb

**Exercises Skeleton:**  
https://github.com/sjasthi/python101/blob/main/colab_notebooks/ch7_skeleton_lists_exercises.ipynb

### Interactive Learning

**Playbook and Quiz:**  
https://github.com/sjasthi/python101/blob/main/Quizzes/python_lists_unpacking_and_slicing_playbook_and_quiz.html

---

## 🎯 Learning Objectives

By the end of this week, students will be able to:

1. Unpack lists into multiple variables using tuple unpacking syntax
2. Use the `*` operator to capture remaining elements during unpacking
3. Slice lists using `[start:stop:step]` notation
4. Apply negative indexing to access elements from the end of lists
5. Use common slicing patterns: `[:-1]`, `[1:]`, and `[::-1]`
6. Slice strings using the same techniques as lists

---

## ✅ Assignments

### 1. Complete Interactive Playbook
- Work through all code examples in the Unpacking tab
- Work through all code examples in the Slicing tab
- Complete the 10-question quiz
- Take a screenshot of your quiz results
- Submit screenshot to Google Classroom

### 2. Explore Exercises Notebook
- Open the skeleton exercises notebook in Google Colab
- Review the programming exercises

---

## 🔑 Key Concepts

### List Unpacking
```python
colors = ['red', 'blue', 'green']
a, b, c = colors  # Unpacking
first, *rest = colors  # Using * for leftovers
```

### List Slicing
```python
nums = [10, 20, 30, 40, 50]
nums[1:4]    # [20, 30, 40]
nums[:-1]    # Remove last element
nums[1:]     # Remove first element
nums[::-1]   # Reverse the list
```

---

## 💡 Tips for Success

- Practice with the interactive playbook before attempting exercises
- Pay attention to the "stop" index being "up to but not including"
- Remember: negative step reverses direction
- Test your understanding with the quiz before submitting

---


**Learn and Help:** www.learnandhelp.com
