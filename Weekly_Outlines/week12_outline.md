# Week 12: Variable Scope and Advanced Function Concepts

## Overview
This week explores advanced function concepts including variable scope, functions returning multiple values, and handling variable numbers of arguments. Students will learn how Python manages variables in different contexts and how to create more powerful and flexible functions.

## Learning Objectives
By the end of this week, students will be able to:
- Understand and apply the concept of variable scope
- Distinguish between local and global variables
- Use the `global` keyword appropriately
- Write functions that return multiple values
- Create functions with variable numbers of arguments (*args)
- Use keyword variable arguments (**kwargs)
- Explain the LEGB rule for variable lookup

## Topics Covered

### 1. Scope of Variables
- What is scope?
- Why scope matters in programming
- Understanding where variables are accessible
- Scope lifetime: when variables are created and destroyed
- The LEGB Rule: Local, Enclosing, Global, Built-in

### 2. Local vs Global Variables
- **Local Variables:** Defined inside functions
- **Global Variables:** Defined outside functions
- Accessing global variables from functions
- Modifying global variables with the `global` keyword
- Best practices: when to use local vs global
- Avoiding common scope-related bugs

### 3. Functions Returning Multiple Values
- Returning tuples from functions
- Unpacking multiple return values
- Syntax and use cases
- Practical examples with multiple returns
- Named tuples for clarity

### 4. Variable Number of Arguments (*args)
- The `*args` syntax
- Accepting any number of positional arguments
- How *args works (creates a tuple)
- Use cases for variable arguments
- Combining regular parameters with *args

### 5. Variable Keyword Arguments (**kwargs)
- The `**kwargs` syntax
- Accepting any number of keyword arguments
- How **kwargs works (creates a dictionary)
- Accessing kwargs values
- Combining parameters, *args, and **kwargs

## Resources

### Presentations
📊 [Functions: Variable Args and Kwargs](https://github.com/sjasthi/python101/blob/main/presentations/5_3_functions_variable_args_and_variable_kwargs.pdf)

📊 [Functions and Variable Scope](https://github.com/sjasthi/python101/blob/main/presentations/5_4_functions_and_variable_scope.pdf)

### Colab Notebooks
💻 [Functions: Variable Scope Concepts](https://github.com/sjasthi/python101/blob/main/colab_notebooks/ch5_2_concepts_functions_variable_scope.ipynb)

💻 [Functions Programming Assignments](https://github.com/sjasthi/python101/blob/main/colab_notebooks/ch5_skeleton_functions_programming_assignments.ipynb)

### Quizzes
🎯 [Variable Scope Interactive Quiz](https://github.com/sjasthi/python101/blob/main/Quizzes/functions_variable_scope_quiz.html)
- **Instructions:** Review the 6 Variable Scope Rules on the first page, complete all 12 quiz questions, and submit a screenshot of your final score to Google Classroom.

## Key Concepts to Remember

### 1. Local vs Global Variables
```python
# Global variable
total_students = 100

def add_student():
    # Local variable (only exists inside this function)
    new_student = "Alice"
    print(new_student)
    print(total_students)  # Can READ global variable

def modify_total():
    global total_students  # Need 'global' keyword to MODIFY
    total_students += 1

add_student()
modify_total()
```

### 2. Variable Scope Example
```python
x = "global"

def outer():
    x = "enclosing"
    
    def inner():
        x = "local"
        print(x)  # Prints "local"
    
    inner()
    print(x)  # Prints "enclosing"

outer()
print(x)  # Prints "global"
```

### 3. Functions Returning Multiple Values
```python
def get_student_info():
    name = "Alice"
    grade = 10
    gpa = 3.8
    return name, grade, gpa  # Returns a tuple

# Unpack the return values
student_name, student_grade, student_gpa = get_student_info()

# Or capture as a tuple
student_info = get_student_info()
print(student_info[0])  # Access by index
```

### 4. Variable Number of Arguments (*args)
```python
def calculate_average(*numbers):
    """Calculate average of any number of values"""
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

# Can call with any number of arguments
avg1 = calculate_average(85, 90, 78)
avg2 = calculate_average(95, 88, 92, 87, 90)
avg3 = calculate_average(100)
```

### 5. Combining Parameters and *args
```python
def create_team(team_name, *players):
    """Create a team with a name and any number of players"""
    print(f"Team: {team_name}")
    print(f"Players: {', '.join(players)}")

create_team("Robotics", "Alice", "Bob", "Charlie")
create_team("Chess Club", "David", "Emma")
```

### 6. Variable Keyword Arguments (**kwargs)
```python
def create_profile(**info):
    """Create a profile with any number of key-value pairs"""
    for key, value in info.items():
        print(f"{key}: {value}")

create_profile(name="Alice", age=15, grade=10, gpa=3.9)
create_profile(name="Bob", school="Central High", sport="Basketball")
```

### 7. Combining All Argument Types
```python
def super_function(required, *args, optional="default", **kwargs):
    """
    required: required positional argument
    *args: variable positional arguments
    optional: optional argument with default
    **kwargs: variable keyword arguments
    """
    print(f"Required: {required}")
    print(f"Args: {args}")
    print(f"Optional: {optional}")
    print(f"Kwargs: {kwargs}")

super_function(1, 2, 3, optional="custom", key1="value1", key2="value2")
```

## The LEGB Rule

Python searches for variables in this order:
1. **L**ocal: Variables defined inside the current function
2. **E**nclosing: Variables in enclosing function scopes
3. **G**lobal: Variables defined at the module level
4. **B**uilt-in: Python's built-in names (print, len, etc.)

```python
x = "global x"

def outer():
    x = "enclosing x"
    
    def inner():
        # Python searches: Local → Enclosing → Global → Built-in
        print(x)  # Finds "enclosing x"
    
    inner()

outer()
```

## Common Scope Pitfalls

### 1. UnboundLocalError
```python
counter = 0

def increment():
    counter = counter + 1  # ❌ ERROR!
    # Python sees assignment, assumes counter is local
    # But you're trying to read it before assigning

# ✅ CORRECT:
def increment():
    global counter
    counter = counter + 1
```

### 2. Mutable Default Arguments
```python
# ❌ DANGER:
def add_item(item, list=[]):
    list.append(item)
    return list

# The default list persists across calls!
print(add_item(1))  # [1]
print(add_item(2))  # [1, 2] - Not what you expected!

# ✅ CORRECT:
def add_item(item, list=None):
    if list is None:
        list = []
    list.append(item)
    return list
```

## Practice Exercises

### Exercise 1: Temperature Converter
Create a function that returns both Fahrenheit and Kelvin from Celsius.

### Exercise 2: Flexible Calculator
Write a function that can add any number of values together using *args.

### Exercise 3: Student Database
Create a function using **kwargs to build student records with flexible fields.

### Exercise 4: Scope Challenge
Write nested functions to demonstrate local, enclosing, and global scope.

### Exercise 5: Grade Statistics
Create a function that takes any number of grades and returns min, max, and average.

## Best Practices

1. **Minimize Global Variables:** Use function parameters and return values instead
2. **Use Local Variables:** Keep variables local when possible for better code organization
3. **Be Cautious with `global`:** Only use when necessary; it can make code harder to debug
4. **Document *args and **kwargs:** Clearly explain what types of arguments are expected
5. **Return Multiple Values:** Use tuple unpacking for cleaner code when returning multiple values

## Activities
- Complete all scope exercises in the Colab notebooks
- **Complete the Variable Scope Interactive Quiz and submit screenshot to Google Classroom**
- Debug scope-related errors in sample code
- Write functions using *args and **kwargs
- Practice returning multiple values from functions
- Trace variable scope in complex nested functions

## Assessment
Students should be able to:
- Explain the difference between local and global scope
- Use the `global` keyword correctly
- Write functions that return multiple values
- Create functions with *args and **kwargs
- Apply the LEGB rule to determine variable accessibility
- Debug common scope-related errors

## Next Week Preview
Week 13 will be a comprehensive review and hands-on practice session covering all function concepts from Weeks 10-12, with programming assignments to solidify your understanding.

---

**Note:** Variable scope and advanced argument handling are crucial concepts. Take time to work through all the examples and ensure you understand how Python resolves variable names and manages function arguments.
