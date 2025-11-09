# Week 13: Functions - Comprehensive Review and Practice

## Overview
This week is dedicated to reviewing, consolidating, and practicing all the function concepts covered in Weeks 10-12. Through hands-on exercises, programming assignments, and collaborative problem-solving, students will strengthen their understanding and gain confidence in writing effective functions.

## Learning Objectives
By the end of this week, students will be able to:
- Synthesize all function concepts from Weeks 10-12
- Write well-structured functions with appropriate parameters
- Apply functions to solve real-world programming problems
- Debug function-related errors efficiently
- Choose the appropriate function design for different scenarios
- Complete comprehensive programming assignments independently

## Week Structure

### Day 1-2: Comprehensive Review
- Review all key concepts from Weeks 10-12
- Q&A session for clarification
- Group discussion on challenging topics
- Walk through complex examples

### Day 3-4: Hands-On Practice
- Guided coding exercises
- Pair programming activities
- Code review and feedback
- Debugging challenges

### Day 5: Programming Assignments
- Individual programming assignments
- Apply all learned concepts
- Build complete programs using functions
- Demonstrate mastery of function concepts

## Topics to Review

### From Week 10: Functions Introduction
✓ Defining function signatures  
✓ Implementing function bodies  
✓ Calling functions  
✓ Void vs value-returning functions  
✓ Built-in vs user-defined functions  
✓ Pass-by-value concept  

### From Week 11: Function Arguments
✓ Formal vs actual arguments  
✓ Positional arguments  
✓ Keyword arguments  
✓ Default parameter values  
✓ Mixing argument types  

### From Week 12: Advanced Concepts
✓ Variable scope (local vs global)  
✓ The LEGB rule  
✓ Functions returning multiple values  
✓ Variable arguments (*args)  
✓ Keyword variable arguments (**kwargs)  
✓ Combining different parameter types  

## Resources to Review

### All Presentations
📊 [Functions Basics](https://github.com/sjasthi/python101/blob/main/presentations/5_1_functions_basics.pdf)

📊 [Positional, Keyword, and Optional Arguments](https://github.com/sjasthi/python101/blob/main/presentations/5_2_functions_positional_keyword_optional_args.pdf)

📊 [Variable Args and Kwargs](https://github.com/sjasthi/python101/blob/main/presentations/5_3_functions_variable_args_and_variable_kwargs.pdf)

📊 [Functions and Variable Scope](https://github.com/sjasthi/python101/blob/main/presentations/5_4_functions_and_variable_scope.pdf)

### All Colab Notebooks
💻 [Functions Introduction - Concepts](https://github.com/sjasthi/python101/blob/main/colab_notebooks/ch5_1_concepts_functions_introduction.ipynb)

💻 [Functions: Variable Scope Concepts](https://github.com/sjasthi/python101/blob/main/colab_notebooks/ch5_2_concepts_functions_variable_scope.ipynb)

💻 [Functions Programming Assignments](https://github.com/sjasthi/python101/blob/main/colab_notebooks/ch5_skeleton_functions_programming_assignments.ipynb)

## Quick Reference Guide

### Function Design Checklist
- [ ] Clear, descriptive function name (verb for actions)
- [ ] Appropriate parameters (required, optional, *args, **kwargs)
- [ ] Proper indentation and syntax
- [ ] Docstring explaining purpose, parameters, and return value
- [ ] Return value (if needed) with correct type
- [ ] Error handling (if applicable)
- [ ] No global variables unless absolutely necessary

### Common Function Patterns

#### 1. Simple Calculator Function
```python
def add(a, b):
    """Add two numbers and return the result."""
    return a + b
```

#### 2. Function with Default Values
```python
def greet(name, greeting="Hello", punctuation="!"):
    """Greet someone with customizable message."""
    return f"{greeting} {name}{punctuation}"
```

#### 3. Function with *args
```python
def find_max(*numbers):
    """Find maximum value from any number of arguments."""
    if not numbers:
        return None
    return max(numbers)
```

#### 4. Function with **kwargs
```python
def build_query(**filters):
    """Build a query string from keyword arguments."""
    conditions = [f"{key}={value}" for key, value in filters.items()]
    return " AND ".join(conditions)
```

#### 5. Function Returning Multiple Values
```python
def analyze_scores(*scores):
    """Return min, max, and average of scores."""
    if not scores:
        return None, None, None
    return min(scores), max(scores), sum(scores) / len(scores)
```

#### 6. Function with Mixed Parameters
```python
def create_report(title, *sections, author="Unknown", **metadata):
    """Create a report with flexible structure."""
    report = f"Title: {title}\n"
    report += f"Author: {author}\n"
    report += f"Sections: {', '.join(sections)}\n"
    for key, value in metadata.items():
        report += f"{key}: {value}\n"
    return report
```

## Practice Problem Categories

### Category 1: Basic Function Design
- Write functions to perform calculations
- Create utility functions for common tasks
- Build simple data processing functions

### Category 2: Working with Arguments
- Functions with multiple parameter types
- Using default values effectively
- Variable number of arguments

### Category 3: Scope and Variables
- Practice with local and global scope
- Nested functions
- Modifying variables correctly

### Category 4: Multiple Return Values
- Functions that compute multiple results
- Unpacking return values
- Using tuples and named tuples

### Category 5: Real-World Applications
- Data validation functions
- String manipulation utilities
- Mathematical computations
- List processing functions

## Sample Practice Exercises

### Exercise 1: Grade Calculator
Create a comprehensive grade calculator with the following features:
- Function to calculate letter grade from percentage
- Function to compute GPA from multiple grades
- Function to determine honor roll status
- Use appropriate parameter types and return values

### Exercise 2: Text Analyzer
Build a text analysis toolkit:
- Function to count words, sentences, paragraphs
- Function to find most common words (*args)
- Function to return multiple statistics
- Use proper scope for helper variables

### Exercise 3: Shopping Cart System
Design functions for a shopping cart:
- Add items with variable arguments
- Calculate total with optional tax rate
- Apply discount codes (**kwargs)
- Return itemized breakdown

### Exercise 4: Data Formatter
Create formatting utilities:
- Format phone numbers, dates, currency
- Handle variable number of inputs
- Use keyword arguments for format options
- Return formatted strings

### Exercise 5: Game Score Tracker
Build a scoring system:
- Track scores for multiple players (*args)
- Calculate statistics (min, max, average, median)
- Determine winner and rankings
- Return multiple values (winner, stats, rankings)

## Programming Assignments

Complete the comprehensive programming assignments in the Colab notebook:
💻 [Functions Programming Assignments](https://github.com/sjasthi/python101/blob/main/colab_notebooks/ch5_skeleton_functions_programming_assignments.ipynb)

### Assignment Guidelines
1. **Read carefully:** Understand what each function should do
2. **Plan first:** Sketch out the logic before coding
3. **Write docstrings:** Document your functions properly
4. **Test thoroughly:** Try different inputs, including edge cases
5. **Refactor:** Improve your code for readability and efficiency
6. **Comment:** Explain complex logic with inline comments

### Testing Your Functions
```python
# Always test your functions with various inputs
def test_function():
    # Normal cases
    assert calculate_area(5, 10) == 50
    
    # Edge cases
    assert calculate_area(0, 10) == 0
    
    # Different types
    assert calculate_area(5.5, 2) == 11.0
    
    print("All tests passed!")

test_function()
```

## Debugging Checklist

When your function doesn't work:
- [ ] Check function name spelling
- [ ] Verify parameter count and order
- [ ] Ensure proper indentation
- [ ] Look for return statement (if needed)
- [ ] Check for scope issues (local vs global)
- [ ] Verify argument types match expectations
- [ ] Test with simple inputs first
- [ ] Use print statements to trace execution
- [ ] Check for typos in variable names

## Common Mistakes to Avoid

1. **Forgetting to return a value**
   ```python
   # ❌ Wrong:
   def add(a, b):
       result = a + b
   
   # ✅ Correct:
   def add(a, b):
       return a + b
   ```

2. **Modifying global variables without 'global' keyword**
   ```python
   # ❌ Wrong:
   counter = 0
   def increment():
       counter += 1  # Error!
   
   # ✅ Correct:
   def increment():
       global counter
       counter += 1
   ```

3. **Positional after keyword arguments**
   ```python
   # ❌ Wrong:
   function(keyword=value, positional_value)
   
   # ✅ Correct:
   function(positional_value, keyword=value)
   ```

4. **Not handling empty *args**
   ```python
   # ❌ Wrong:
   def average(*numbers):
       return sum(numbers) / len(numbers)  # Crashes if empty!
   
   # ✅ Correct:
   def average(*numbers):
       if not numbers:
           return 0
       return sum(numbers) / len(numbers)
   ```

## Best Practices Summary

### Function Design
- **One purpose per function:** Each function should do one thing well
- **Clear naming:** Use descriptive verb-based names
- **Reasonable length:** Keep functions under 20-30 lines when possible
- **Avoid side effects:** Functions shouldn't unexpectedly modify global state

### Parameters
- **Required first, optional last:** Logical parameter ordering
- **Sensible defaults:** Choose default values that work in most cases
- **Document parameters:** Explain what each parameter does
- **Validate inputs:** Check for invalid values when necessary

### Documentation
```python
def calculate_bmi(weight, height, unit="metric"):
    """
    Calculate Body Mass Index.
    
    Parameters:
        weight (float): Weight in kg (metric) or lbs (imperial)
        height (float): Height in meters (metric) or inches (imperial)
        unit (str): "metric" or "imperial" (default: "metric")
    
    Returns:
        float: Calculated BMI value
    
    Example:
        >>> calculate_bmi(70, 1.75)
        22.86
    """
    if unit == "imperial":
        return (weight / (height ** 2)) * 703
    return weight / (height ** 2)
```

## Assessment Criteria

Students will be evaluated on:
- **Correctness:** Functions produce expected results
- **Code Quality:** Clean, readable, well-organized code
- **Documentation:** Clear docstrings and comments
- **Error Handling:** Appropriate handling of edge cases
- **Efficiency:** Reasonable approach to problem-solving
- **Testing:** Thorough testing with various inputs

## Moving Forward

After completing this review week, you should feel confident:
- Writing functions for any purpose
- Choosing appropriate parameter types
- Managing variable scope correctly
- Debugging function-related issues
- Following Python best practices for functions

### Next Steps
- Apply functions to all future Python programs
- Create reusable function libraries
- Explore lambda functions and functional programming
- Learn about decorators and advanced function concepts

## Final Tips

1. **Practice daily:** Write at least one function every day
2. **Read code:** Study how others write functions
3. **Refactor:** Constantly improve your existing functions
4. **Ask questions:** Don't hesitate to seek clarification
5. **Collaborate:** Review code with peers for learning
6. **Build projects:** Apply functions in complete programs

---

## Congratulations!

You've completed four weeks of intensive function learning! Functions are the building blocks of well-organized, reusable code. The skills you've developed here will be essential for all your future programming endeavors.

**Remember:** Great programmers are great function writers. Keep practicing, keep improving, and keep coding! 🚀

---

**Important:** Complete all programming assignments in the Colab notebook before moving to the next chapter. Your mastery of functions will significantly impact your success in advanced Python topics.
