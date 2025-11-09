# Lab 10: Math Quiz Game with Functions
**Total Points: 10 | Time: 20 minutes**

## Learning Objectives
By completing this lab, you will be able to:
- Define and call functions in Python
- Use return values from functions
- Practice using the `random` module

## Problem Description
Create a simple Math Quiz Game that gives 5 addition problems. The program will:
1. Generate random addition problems
2. Check if the student's answer is correct
3. Keep track of the score
4. Display the final results

### Sample Output
```
Problem 1: What is 247 + 129?
Your answer: 376
Correct!

Problem 2: What is 183 + 94?
Your answer: 270
Incorrect. The correct answer is 277.

... (3 more problems)

Quiz Complete!
You got 3 out of 5 correct.
Your score: 60%
```

## Requirements

### You Must Create TWO Functions:

#### 1. `create_problem()` - 5 points
- **Purpose**: Generate two random numbers for addition
- **Parameters**: None
- **Returns**: Two integers (num1, num2) between 1 and 100
- **Hints**: 
  - Use `random.randint(1, 100)` to generate each number
  - Remember to return BOTH numbers
  - You can return two values like this: `return value1, value2`

#### 2. `check_answer(user_answer, correct_answer)` - 3 points
- **Purpose**: Check if the answer is correct
- **Parameters**:
  - `user_answer` (int): The answer from the user
  - `correct_answer` (int): The correct answer
- **Returns**: `True` if correct, `False` if incorrect
- **Hints**:
  - Use an if statement to compare the two parameters
  - Return True when they match
  - Return False when they don't match

### Main Program (2 points)

Write the main program that:
1. Uses a **for loop** to run 5 quiz problems
2. Calls `create_problem()` to get two numbers
3. Asks the user for their answer
4. Calls `check_answer()` to check if it's correct
5. Prints "Correct!" or "Incorrect. The correct answer is [answer]."
6. Keeps track of the score (how many correct)
7. At the end, prints the total score and percentage

## Code Template

```python
import random

def create_problem():
    # Generate two random numbers between 1 and 100
    # Return both numbers
    pass

def check_answer(user_answer, correct_answer):
    # Compare user_answer with correct_answer
    # Return True if correct, False if incorrect
    pass

# Main program starts here
score = 0

for i in range(5):
    # Call create_problem() to get num1 and num2
    # Calculate the correct_answer
    # Ask the user for their answer
    # Call check_answer() to check if correct
    # If correct, add 1 to score and print "Correct!"
    # If incorrect, print the correct answer
    pass

# Print final results
print("\nQuiz Complete!")
print(f"You got {score} out of 5 correct.")
print(f"Your score: {score * 20}%")
```

## Grading Rubric

| Component | Points | Criteria |
|-----------|--------|----------|
| `create_problem()` | 5 | Creates two random numbers (1-100) and returns them correctly |
| `check_answer()` | 3 | Takes two parameters, compares them, returns True/False |
| Main Program | 2 | Uses both functions correctly, tracks score, displays results |
| **Total** | **10** | |

### Deductions
- -1 point: Program doesn't run or has errors
- -0.5 points: Missing `import random`
- -0.5 points: Doesn't show final score or percentage

## Step-by-Step Guide

**Step 1:** Import random at the top
```python
import random
```

**Step 2:** Write `create_problem()` function
- Generate num1 using `random.randint(1, 100)`
- Generate num2 using `random.randint(1, 100)`
- Return both numbers: `return num1, num2`

**Step 3:** Write `check_answer()` function
- Use an if statement to compare the two parameters
- Return True if they match
- Return False if they don't match

**Step 4:** Write the main program
- Create a variable `score = 0` before the loop
- Use `for i in range(5):` to loop 5 times
- Inside the loop:
  - Call your function: `num1, num2 = create_problem()`
  - Calculate: `correct_answer = num1 + num2`
  - Ask for input: `user_answer = int(input(f"Problem {i+1}: What is {num1} + {num2}? "))`
  - Check: `if check_answer(user_answer, correct_answer):`
  - Print appropriate message
  - Update score if correct

**Step 5:** Print final results
- Show total correct out of 5
- Show percentage (score * 20)

## Testing Checklist

- [ ] My program runs without errors
- [ ] `create_problem()` returns two different random numbers each time
- [ ] `check_answer()` correctly identifies right and wrong answers
- [ ] The score increases when I get answers correct
- [ ] The final score and percentage are displayed correctly
- [ ] I tested with all correct answers (should get 100%)
- [ ] I tested with all wrong answers (should get 0%)

## Submission

1. Save your file as `lab10_functions.py`
2. Add your name in a comment at the top
3. Test your program completely
4. Submit to Google Classroom

---

**Key Concepts:**
- Functions can **return** values using the `return` keyword
- You can return multiple values: `return num1, num2`
- Functions make code reusable - you can call them many times!

Good luck! 🎯
