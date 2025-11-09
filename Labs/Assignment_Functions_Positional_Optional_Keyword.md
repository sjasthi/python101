# Assignment: Functions - Positional, Keyword, and Optional Arguments
**Total Points: 25 | Due Date: [Add Date]**

## Learning Objectives
By completing this assignment, you will be able to:
- Define functions with positional arguments
- Use keyword arguments when calling functions
- Create functions with optional (default) parameters
- Understand the difference between these three types of arguments
- Write well-documented functions with proper parameter usage

## Understanding Function Arguments

### 1. Positional Arguments
Arguments that must be provided in the correct order.
```python
def greet(first_name, last_name):
    print(f"Hello, {first_name} {last_name}!")

greet("John", "Smith")  # Order matters!
```

### 2. Keyword Arguments
Arguments specified by name when calling the function (order doesn't matter).
```python
def greet(first_name, last_name):
    print(f"Hello, {first_name} {last_name}!")

greet(last_name="Smith", first_name="John")  # Order doesn't matter!
```

### 3. Optional Arguments (Default Parameters)
Arguments with default values - they don't have to be provided when calling the function.
```python
def greet(first_name, last_name, title="Mr."):
    print(f"Hello, {title} {first_name} {last_name}!")

greet("John", "Smith")           # Uses default title "Mr."
greet("Jane", "Doe", "Dr.")      # Uses provided title "Dr."
greet("John", "Smith", title="Prof.")  # Using keyword argument
```

---

## Programming Problems

### Problem 1: Student Report Card (5 points)

Write a function called `print_grade_report()` that takes **positional arguments** for a student's information.

**Function Requirements:**
- **Parameters** (all required, in this order):
  - `student_name` (str): The student's name
  - `subject` (str): The subject name
  - `score` (int): The test score (0-100)
  - `total_points` (int): Total possible points
- **Returns**: Nothing (just prints)
- **Output**: Print a formatted report

**Example Usage:**
```python
print_grade_report("Alice Johnson", "Math", 85, 100)
print_grade_report("Bob Smith", "Science", 92, 100)
```

**Expected Output:**
```
===== GRADE REPORT =====
Student: Alice Johnson
Subject: Math
Score: 85/100
Percentage: 85.0%
========================

===== GRADE REPORT =====
Student: Bob Smith
Subject: Science
Score: 92/100
Percentage: 92.0%
========================
```

**Grading Criteria:**
- Function has 4 positional parameters (1 pt)
- Calculates percentage correctly (1 pt)
- Formats output nicely (2 pts)
- Function works with different inputs (1 pt)

---

### Problem 2: Pizza Order (6 points)

Write a function called `order_pizza()` that can be called using **keyword arguments**.

**Function Requirements:**
- **Parameters** (all required):
  - `size` (str): "Small", "Medium", or "Large"
  - `toppings` (str): The toppings on the pizza
  - `quantity` (int): Number of pizzas
  - `customer_name` (str): Who is ordering
- **Returns**: A string with the complete order details
- The function should calculate the total cost:
  - Small: $8, Medium: $12, Large: $15

**Example Usage:**
```python
order1 = order_pizza(size="Large", toppings="Pepperoni", quantity=2, customer_name="Maria")
print(order1)

order2 = order_pizza(customer_name="John", quantity=1, size="Medium", toppings="Cheese")
print(order2)
```

**Expected Output:**
```
Order for Maria: 2 Large pizza(s) with Pepperoni. Total: $30
Order for John: 1 Medium pizza(s) with Cheese. Total: $12
```

**Grading Criteria:**
- Function has 4 parameters that can be used as keywords (1 pt)
- Correctly calculates price based on size (2 pts)
- Returns properly formatted string (2 pts)
- Function works with parameters in any order (1 pt)

---

### Problem 3: Create User Profile (7 points)

Write a function called `create_profile()` that uses **optional (default) parameters**.

**Function Requirements:**
- **Parameters**:
  - `username` (str): Required - the user's username
  - `age` (int): Optional - default is 13
  - `country` (str): Optional - default is "USA"
  - `hobby` (str): Optional - default is "Reading"
- **Returns**: A dictionary with the user's profile information
- The dictionary should have keys: "username", "age", "country", "hobby"

**Example Usage:**
```python
profile1 = create_profile("alex_123")
print(profile1)

profile2 = create_profile("sarah_m", 16)
print(profile2)

profile3 = create_profile("juan_99", 15, "Mexico", "Soccer")
print(profile3)

profile4 = create_profile("emma_k", hobby="Painting", age=14)
print(profile4)
```

**Expected Output:**
```
{'username': 'alex_123', 'age': 13, 'country': 'USA', 'hobby': 'Reading'}
{'username': 'sarah_m', 'age': 16, 'country': 'USA', 'hobby': 'Reading'}
{'username': 'juan_99', 'age': 15, 'country': 'Mexico', 'hobby': 'Soccer'}
{'username': 'emma_k', 'age': 14, 'country': 'USA', 'hobby': 'Painting'}
```

**Grading Criteria:**
- Has 1 required parameter and 3 optional parameters with defaults (2 pts)
- Returns a dictionary with correct keys (2 pts)
- Default values work correctly when not provided (2 pts)
- Function works with keyword arguments (1 pt)

---

### Problem 4: Calculate Shipping Cost (7 points)

Write a function called `calculate_shipping()` that combines **all three types** of arguments.

**Function Requirements:**
- **Parameters**:
  - `weight` (float): Required positional - weight in pounds
  - `distance` (int): Required positional - distance in miles
  - `express` (bool): Optional - default is False
  - `insurance` (bool): Optional - default is False
- **Returns**: The total shipping cost (float)
- **Calculation Rules**:
  - Base cost: $5
  - Weight cost: $1.50 per pound
  - Distance cost: $0.10 per mile
  - Express shipping: adds $10
  - Insurance: adds $5

**Example Usage:**
```python
cost1 = calculate_shipping(10, 100)
print(f"Cost 1: ${cost1:.2f}")

cost2 = calculate_shipping(5, 50, express=True)
print(f"Cost 2: ${cost2:.2f}")

cost3 = calculate_shipping(8, 200, insurance=True, express=True)
print(f"Cost 3: ${cost3:.2f}")
```

**Expected Output:**
```
Cost 1: $30.00
Cost 2: $32.50
Cost 3: $57.00
```

**Calculation Breakdown for Examples:**
- Cost 1: $5 + (10 × $1.50) + (100 × $0.10) = $5 + $15 + $10 = $30.00
- Cost 2: $5 + (5 × $1.50) + (50 × $0.10) + $10 = $5 + $7.50 + $5 + $10 = $32.50
- Cost 3: $5 + (8 × $1.50) + (200 × $0.10) + $10 + $5 = $5 + $12 + $20 + $10 + $5 = $57.00

**Grading Criteria:**
- Has 2 required positional parameters (1 pt)
- Has 2 optional parameters with defaults (1 pt)
- Correctly calculates base + weight + distance cost (2 pts)
- Correctly adds express and insurance when True (2 pts)
- Returns a float value (1 pt)

---

## Submission Requirements

Create a Python file named `assignment_functions.py` that includes:

1. **Header Comment** (Include at the top):
```python
# Assignment: Functions - Positional, Keyword, and Optional Arguments
# Name: [Your Name]
# Date: [Submission Date]
# Description: Practice with different types of function arguments
```

2. **All Four Functions** with clear comments explaining each parameter

3. **Test Section** at the bottom:
```python
# ========== TEST SECTION ==========
# Test all your functions here with the example calls

print("Problem 1: Student Report Card")
print_grade_report("Alice Johnson", "Math", 85, 100)
print()

print("Problem 2: Pizza Order")
order1 = order_pizza(size="Large", toppings="Pepperoni", quantity=2, customer_name="Maria")
print(order1)
print()

# Add tests for Problem 3 and 4...
```

## Grading Rubric

| Problem | Points | Requirements |
|---------|--------|--------------|
| Problem 1: Student Report Card | 5 | Positional arguments, correct output format |
| Problem 2: Pizza Order | 6 | Keyword arguments, price calculation, string return |
| Problem 3: User Profile | 7 | Optional parameters with defaults, dictionary return |
| Problem 4: Shipping Cost | 7 | Mixed argument types, complex calculation |
| **Total** | **25** | |

### Additional Deductions
- -2 points: Missing header comment
- -2 points: No test section or incomplete testing
- -3 points: Code doesn't run or has syntax errors
- -1 point: Poor code organization or missing comments

## Tips for Success

1. **Read the requirements carefully** - make sure you understand what type of arguments each function needs

2. **Test incrementally** - test each function as you write it, don't wait until the end

3. **Use descriptive variable names** - this makes your code easier to read and debug

4. **Add comments** - explain what each function does and what each parameter represents

5. **Check your calculations** - verify your math by hand for at least one example

6. **Default parameters must come last** - In Python, required parameters must come before optional ones:
   ```python
   # CORRECT
   def example(required1, required2, optional1=default)
   
   # WRONG
   def example(optional1=default, required1, required2)
   ```

## Common Mistakes to Avoid

❌ Mixing up the order of positional arguments  
❌ Forgetting to return a value when required  
❌ Not providing default values for optional parameters  
❌ Putting required parameters after optional ones  
❌ Not testing with different combinations of arguments  

## Testing Checklist

Before submitting, verify that:
- [ ] All four functions are implemented
- [ ] Each function has the correct number and type of parameters
- [ ] Problem 1 uses positional arguments correctly
- [ ] Problem 2 works with keyword arguments in any order
- [ ] Problem 3 has working default values
- [ ] Problem 4 combines all three argument types
- [ ] All calculations are correct
- [ ] Test section demonstrates all functions working
- [ ] Code runs without errors
- [ ] Header comment is complete

## Example Test Output

Your complete program should produce output similar to this when run:

```
Problem 1: Student Report Card
===== GRADE REPORT =====
Student: Alice Johnson
Subject: Math
Score: 85/100
Percentage: 85.0%
========================

Problem 2: Pizza Order
Order for Maria: 2 Large pizza(s) with Pepperoni. Total: $30

Problem 3: User Profile
{'username': 'alex_123', 'age': 13, 'country': 'USA', 'hobby': 'Reading'}

Problem 4: Shipping Cost
Cost 1: $30.00
```

---

**Remember**: Functions with clear, well-defined parameters make your code more flexible and reusable. Understanding when to use positional, keyword, and optional arguments is an essential programming skill!

Good luck! 🚀
