# Week 11: Function Arguments - Positional, Keyword, and Optional Arguments

## Overview
This week builds upon Week 10's introduction to functions by diving deeper into how arguments are passed to functions. Students will learn about formal vs actual arguments, positional arguments, keyword arguments, and how to use default values to make functions more flexible.

## Learning Objectives
By the end of this week, students will be able to:
- Distinguish between formal and actual arguments
- Use positional arguments correctly in function calls
- Apply keyword arguments for clarity and flexibility
- Define and use default parameter values
- Mix different argument types appropriately
- Write more flexible and user-friendly functions

## Topics Covered

### 1. Formal vs Actual Arguments
- **Formal Arguments (Parameters):** Variables defined in the function signature
- **Actual Arguments:** Values passed when calling the function
- Understanding the mapping between formal and actual arguments
- Terminology: parameters vs arguments

### 2. Positional Arguments
- Arguments passed in a specific order
- Position matters: matching formal parameters by order
- Most common way to pass arguments
- Examples and best practices
- When positional arguments work best

### 3. Keyword Arguments
- Arguments passed with explicit parameter names
- Order doesn't matter when using keywords
- Syntax: `function_name(param1=value1, param2=value2)`
- Improved code readability
- Benefits of using keyword arguments

### 4. Optional Arguments (Default Values)
- Defining parameters with default values
- Making arguments optional
- Syntax: `def function_name(param1, param2=default_value):`
- Rules: required parameters come before optional ones
- Overriding default values
- Creating flexible functions with sensible defaults

### 5. Mixing Argument Types
- Combining positional and keyword arguments
- Order rules: positional first, then keyword
- Best practices for readable function calls
- Common pitfalls to avoid

## Resources

### Presentation
📊 [Functions: Positional, Keyword, and Optional Arguments](https://github.com/sjasthi/python101/blob/main/presentations/5_2_functions_positional_keyword_optional_args.pdf)

### Colab Notebooks
💻 [Functions Introduction - Concepts and Practice](https://github.com/sjasthi/python101/blob/main/colab_notebooks/ch5_1_concepts_functions_introduction.ipynb)

💻 [Functions Programming Assignments](https://github.com/sjasthi/python101/blob/main/colab_notebooks/ch5_skeleton_functions_programming_assignments.ipynb)

### Interactive Playbook
🎮 [Play with Positional, Keyword and Optional Arguments](https://github.com/sjasthi/python101/blob/main/Quizzes/functions_positional_keyword_optional_arguments_interactive_playbook.html)

### Quiz 11 (10 points; due today)
📝 Take the Quiz and submit the screenshot of your final score  
[Quiz 11 - Functions: Positional, Keyword, and Optional Arguments](https://github.com/sjasthi/python101/blob/main/Quizzes/functions_positional_keyword_optional_arguments_interactive_playbook.html)

### Lab 11 (10 points; due 22 Nov)
🔬 [Lab 11 - Function Arguments Experimentation](https://github.com/sjasthi/python101/blob/main/Labs/python101_lab11_functions_positional_keyword_optional_arguments.ipynb)

## Key Concepts to Remember

### 1. Formal vs Actual Arguments
```python
def greet(name, age):  # name and age are FORMAL arguments (parameters)
    print(f"Hello {name}, you are {age} years old")

greet("Alice", 15)  # "Alice" and 15 are ACTUAL arguments
```

### 2. Positional Arguments
```python
def calculate_rectangle_area(length, width):
    return length * width

# Position matters!
area = calculate_rectangle_area(10, 5)  # length=10, width=5
```

### 3. Keyword Arguments
```python
# Using keywords - order doesn't matter
area = calculate_rectangle_area(width=5, length=10)
area = calculate_rectangle_area(length=10, width=5)  # Same result
```

### 4. Default Values
```python
def create_student_profile(name, grade, gpa=4.0, clubs="None"):
    return f"{name} is in grade {grade}, GPA: {gpa}, Clubs: {clubs}"

# Can call with or without optional arguments
profile1 = create_student_profile("Bob", 10)
profile2 = create_student_profile("Alice", 11, 3.8, "Robotics")
profile3 = create_student_profile("Charlie", 9, clubs="Chess")
```

### 5. Mixing Arguments
```python
def book_info(title, author, year=2024, genre="Fiction"):
    return f"{title} by {author} ({year}) - {genre}"

# Valid combinations:
book1 = book_info("Python Fun", "John Doe")
book2 = book_info("Data Science", "Jane Smith", 2023)
book3 = book_info("AI Basics", "Bob Jones", genre="Non-Fiction")
book4 = book_info("ML Guide", "Alice Lee", year=2023, genre="Technical")
```

## Common Mistakes to Avoid

1. **Positional arguments after keyword arguments:**
   ```python
   # ❌ WRONG:
   calculate_rectangle_area(length=10, 5)
   
   # ✅ CORRECT:
   calculate_rectangle_area(10, width=5)
   ```

2. **Default parameters before required parameters:**
   ```python
   # ❌ WRONG:
   def greet(message="Hello", name):
       pass
   
   # ✅ CORRECT:
   def greet(name, message="Hello"):
       pass
   ```

3. **Wrong number of arguments:**
   ```python
   def add(a, b):
       return a + b
   
   # ❌ WRONG:
   result = add(5)  # Missing one argument
   
   # ✅ CORRECT:
   result = add(5, 3)
   ```
## Next Week Preview
Week 12 will cover variable scope (local vs global), functions returning multiple values, and handling variable numbers of arguments (*args and **kwargs).

---

**Note:** Complete all notebook exercises and experiment with different argument combinations to build confidence with function parameters.
