# Week 10: Functions - Introduction

## Overview
This week introduces the fundamental concepts of functions in Python, including how to define, implement, and call functions. Students will learn the difference between void and value-returning functions, as well as understand the distinction between built-in and user-defined functions.

## Learning Objectives
By the end of this week, students will be able to:
- Define and explain what a function is in Python
- Write function signatures (definitions) with proper syntax
- Implement function bodies with appropriate logic
- Call functions and pass arguments correctly
- Differentiate between void-returning and value-returning functions
- Identify built-in vs user-defined functions
- Understand the concept of pass-by-value in Python

## Topics Covered

### 1. Functions: Introduction
- What are functions and why do we use them?
- Benefits of using functions (reusability, modularity, organization)
- Real-world analogies for functions

### 2. Defining Functions (Function Signature)
- The `def` keyword
- Function naming conventions
- Parameter lists
- Syntax: `def function_name(parameters):`

### 3. Implementing Functions
- Writing the function body
- Indentation rules
- Adding logic and operations inside functions
- Docstrings and documentation

### 4. Calling Functions
- Function invocation syntax
- Passing arguments to functions
- Understanding function execution flow
- Where and when to call functions

### 5. Void-Returning Functions
- Functions that perform actions but don't return values
- Using `print()` inside void functions
- Understanding `None` as an implicit return value
- Use cases for void functions

### 6. Value-Returning Functions
- The `return` statement
- Functions that compute and return results
- Single vs multiple return statements
- Capturing return values in variables

### 7. Built-in vs User-Defined Functions
- Python's built-in functions (print, len, sum, etc.)
- Creating custom functions for specific tasks
- When to use built-in vs when to create your own

### 8. Pass-By-Value: Functions Get a Copy
- How Python passes arguments to functions
- Understanding that functions work with copies of data
- Immutable vs mutable objects in function parameters
- Scope preview: what happens to variables inside functions

## Resources

### Presentation
📊 [Functions Basics Presentation](https://github.com/sjasthi/python101/blob/main/presentations/5_1_functions_basics.pdf)

### Colab Notebook
💻 [Functions Introduction - Concepts and Practice](https://github.com/sjasthi/python101/blob/main/colab_notebooks/ch5_1_concepts_functions_introduction.ipynb)

## Key Concepts to Remember

1. **Function Definition Template:**
   ```python
   def function_name(parameter1, parameter2):
       # function body
       # perform operations
       return result  # optional
   ```

2. **Void Function Example:**
   ```python
   def greet_student(name):
       print(f"Hello, {name}!")
   ```

3. **Value-Returning Function Example:**
   ```python
   def calculate_area(length, width):
       area = length * width
       return area
   ```

## Activities and Practice
- Work through the Colab notebook exercises
- Define simple functions for everyday calculations
- Practice calling functions with different arguments
- Convert previous code snippets into reusable functions

## Assessment
Students should be able to:
- Write a function signature correctly
- Implement a simple function body
- Call a function and use its return value
- Explain the difference between void and value-returning functions

## What is due today?
- Quiz 10 - Please see Week 10 folder in google classroom
- Lab 10 - Please see Week 10 folder in google classroom
  
## Next Week Preview
Week 11 will explore different types of function arguments: formal vs actual arguments, positional arguments, keyword arguments, and default values.

---

**Note:** Make sure to review the presentation and complete all exercises in the Colab notebook before moving to Week 11.
