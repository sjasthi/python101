# Week 17: Advanced List Operations - Map, Filter, Reduce & Traversals

## 📚 Course Information
- **Course**: Python 101
- **Week**: 17
- **Topic**: Advanced List Operations, Functional Programming, and List/String Traversals
- **Prerequisites**: Understanding of lists, basic functions, lambda functions

---

## 🎯 Learning Objectives

By the end of this week, students will be able to:

1. **Apply functional programming concepts** using `map()`, `filter()`, and `reduce()` functions
2. **Master negative indexing** to access elements from the end of sequences
3. **Use membership operators** (`in` and `not in`) for data validation and searching
4. **Implement various list traversal techniques** including enumerate, range, and while loops
5. **Convert between lists and strings** using `split()` and `join()` methods
6. **Traverse strings** character by character using multiple approaches
7. **Combine multiple concepts** to solve complex programming problems

---

## 📖 Topics Covered

### 1. Map, Filter, and Reduce Functions
- **Map Function**
  - Syntax and usage: `map(function, iterable)`
  - Transforming list elements
  - Using lambda functions with map
  - Practical applications (converting data types, calculations)

- **Filter Function**
  - Syntax and usage: `filter(function, iterable)`
  - Selecting elements based on conditions
  - Using lambda functions with filter
  - Data filtering and validation

- **Reduce Function**
  - Importing from functools module
  - Syntax and usage: `reduce(function, iterable)`
  - Accumulating values (sum, product, maximum)
  - Combining elements into single values

- **Combining Map, Filter, and Reduce**
  - Chaining operations
  - Building data pipelines
  - Real-world problem solving

### 2. Negative Indexing
- Understanding positive vs. negative indices
- Accessing elements from the end of sequences
- Using negative indices with slicing
- Practical applications (file extensions, last elements)

### 3. Membership Operators
- **The `in` operator**
  - Checking if element exists in sequence
  - Using with lists, strings, and dictionaries
  
- **The `not in` operator**
  - Checking for absence of elements
  - Input validation scenarios
  
- **Practical Applications**
  - User input validation
  - Search functionality
  - Access control and permissions

### 4. List Traversal Methods
- **Method 1**: Direct access with for loop
  - `for item in list:`
  - When to use: Only need values
  
- **Method 2**: Using range and index
  - `for i in range(len(list)):`
  - When to use: Need index positions
  
- **Method 3**: Using enumerate (recommended)
  - `for index, value in enumerate(list):`
  - When to use: Need both index and value
  - Custom start indices
  
- **Method 4**: While loops
  - Manual index control
  - Conditional traversal
  
- **Advanced Patterns**
  - Reverse traversal
  - Skipping elements (step)
  - Parallel traversal with zip()

### 5. Lists and Strings
- **String to List Conversion**
  - Using `split()` method
  - Splitting on different delimiters
  - Converting to character lists
  
- **List to String Conversion**
  - Using `join()` method
  - Different separators
  - Formatting output
  
- **String Traversal**
  - Character-by-character iteration
  - Using enumerate with strings
  - String manipulation techniques
  
- **Practical Applications**
  - Palindrome checking
  - Vowel counting
  - Text processing
  - Removing duplicates

---

## 📅 Weekly Schedule

### **Day 1: Introduction to Map, Filter, and Reduce**
- **Lecture Topics**:
  - Introduction to functional programming concepts
  - The `map()` function - transforming data
  - Practical examples and use cases
  
- **Materials**:
  - Presentation: [7_2_and_7_3_python_lists_map_filter_reduce_plus.md](https://github.com/sjasthi/python101/blob/main/presentations/7_2_and_7_3_python_lists_map_filter_reduce_plus.md)
  - Colab Notebook: [ch7_concepts_list_intro_1.ipynb](https://github.com/sjasthi/python101/blob/main/colab_notebooks/ch7_concepts_list_intro_1.ipynb)
  
- **Activities**:
  - Work through map examples
  - Create simple lambda functions
  - Transform lists of numbers and strings

### **Day 2: Filter, Reduce, and Combinations**
- **Lecture Topics**:
  - The `filter()` function - selecting data
  - The `reduce()` function - combining data
  - Importing from functools
  - Chaining map, filter, and reduce operations
  
- **Materials**:
  - Continue with presentation
  - Interactive Playbook: [lists_map_filter_reduce_traversals_playbook_and_quiz.html](https://github.com/sjasthi/python101/blob/main/Quizzes/lists_map_filter_reduce_traversals_playbook_and_quiz.html)
  
- **Activities**:
  - Filter even/odd numbers
  - Calculate sum and product using reduce
  - Build a data pipeline combining all three functions

### **Day 3: Negative Indexing and Membership Operators**
- **Lecture Topics**:
  - Understanding negative indices (-1, -2, -3, etc.)
  - Visual representation of indexing
  - Membership operators: `in` and `not in`
  - Practical applications and validation
  
- **Materials**:
  - Interactive Playbook (Negative Indexing & Membership tabs)
  - Colab Notebook examples
  
- **Activities**:
  - Access elements from end of lists
  - Use negative slicing
  - Validate user input with membership operators
  - Check for substrings in text

### **Day 4: List Traversals and Best Practices**
- **Lecture Topics**:
  - Four methods of list traversal
  - When to use each method
  - The `enumerate()` function
  - Advanced traversal patterns (reverse, skip, parallel)
  
- **Materials**:
  - Interactive Playbook (List Traversals tab)
  - Comparison table of methods
  
- **Activities**:
  - Practice all four traversal methods
  - Use enumerate with custom start
  - Reverse traverse a list
  - Traverse two lists simultaneously with zip()

### **Day 5: Lists, Strings, and Lab Work**
- **Lecture Topics**:
  - Converting between lists and strings
  - String traversal techniques
  - Text processing applications
  - Review of all week's concepts
  
- **Materials**:
  - Interactive Playbook (Lists & Strings tab)
  - Lab Assignment: [python101_map_filter_reduce_list_traversals.ipynb](https://github.com/sjasthi/python101/blob/main/Labs/python101_map_filter_reduce_list_traversals.ipynb)
  
- **Activities**:
  - Use split() and join() methods
  - Create a palindrome checker
  - Count vowels in text
  - Begin lab assignment
  - Complete interactive quiz

---

## 📝 Assignments & Assessments

### **Interactive Playbook & Quiz** (Due: End of Day 5)
- **Description**: Complete the interactive playbook with live code examples
- **Location**: [lists_map_filter_reduce_traversals_playbook_and_quiz.html](https://github.com/sjasthi/python101/blob/main/Quizzes/lists_map_filter_reduce_traversals_playbook_and_quiz.html)
- **Requirements**:
  - Work through all 5 concept tabs
  - Run and experiment with all code examples
  - Complete the 10-question quiz
  - **Submit**: Screenshot of final quiz score to Google Classroom
- **Points**: 20 points
- **Topics Tested**:
  - Map, filter, reduce functions
  - Negative indexing
  - Membership operators
  - List traversal methods
  - String/list conversions

### **Lab Assignment** (Due: End of Week 17)
- **Description**: Hands-on programming exercises
- **Location**: [python101_map_filter_reduce_list_traversals.ipynb](https://github.com/sjasthi/python101/blob/main/Labs/python101_map_filter_reduce_list_traversals.ipynb)
- **Format**: Jupyter Notebook with guided exercises
- **Submit**: Completed notebook to Google Classroom
- **Points**: 50 points

### **Programming Assignment 6** (Due: 1 week after Week 17)
- **Description**: Comprehensive assignment combining all concepts
- **Location**: [python101_lists_intro_assignment_6.md](https://github.com/sjasthi/python101/blob/main/Labs/python101_lists_intro_assignment_6.md)
- **Submit**: Python file (.py) or Jupyter Notebook (.ipynb) to Google Classroom
- **Points**: 100 points
- **Grading Criteria**:
  - Correct implementation of map, filter, reduce
  - Proper use of list traversals
  - Code readability and comments
  - Testing and validation

---

## 🎓 Tips for Success

### **For Understanding Map, Filter, and Reduce:**
1. **Start with lambda functions** - Make sure you're comfortable with lambda syntax
2. **Always convert to list** - Remember `map()` and `filter()` return iterators, use `list()` to see results
3. **Think step by step** - Break complex operations into separate map, filter, reduce steps
4. **Import reduce** - Don't forget `from functools import reduce`

### **For Mastering Indexing:**
1. **Draw it out** - Create visual diagrams showing positive and negative indices
2. **Remember -1** - The last element is always at index -1, second-to-last is -2, etc.
3. **Practice slicing** - Use negative indices in slicing operations: `list[-3:]`

### **For List Traversals:**
1. **Use enumerate when possible** - It's the most Pythonic way to get both index and value
2. **Choose the right method** - Pick the simplest method that gives you what you need
3. **Start counting at 1** - Use `enumerate(list, start=1)` for human-readable numbering

### **For Strings and Lists:**
1. **Remember immutability** - Strings cannot be changed, lists can
2. **Know your separators** - Use appropriate separators in `split()` and `join()`
3. **Test edge cases** - What happens with empty strings or single characters?

### **General Study Tips:**
- ✅ Work through the interactive playbook examples
- ✅ Modify the example code and see what happens
- ✅ Practice writing your own lambda functions
- ✅ Complete all lab exercises before attempting the assignment
- ✅ Use enumerate whenever you need both index and value
- ✅ Draw diagrams for negative indexing until it becomes second nature

---

## 🔗 All Resources

### **Presentation Materials**
- [Main Presentation](https://github.com/sjasthi/python101/blob/main/presentations/7_2_and_7_3_python_lists_map_filter_reduce_plus.md)

### **Interactive Learning**
- [Interactive Playbook & Quiz](https://github.com/sjasthi/python101/blob/main/Quizzes/lists_map_filter_reduce_traversals_playbook_and_quiz.html)
- [Colab Notebook](https://github.com/sjasthi/python101/blob/main/colab_notebooks/ch7_concepts_list_intro_1.ipynb)

### **Assignments**
- [Lab Assignment](https://github.com/sjasthi/python101/blob/main/Labs/python101_map_filter_reduce_list_traversals.ipynb)
- [Programming Assignment 6](https://github.com/sjasthi/python101/blob/main/Labs/python101_lists_intro_assignment_6.md)

### **Additional Resources**
- Python Documentation: [Built-in Functions](https://docs.python.org/3/library/functions.html)
- Python Documentation: [functools.reduce](https://docs.python.org/3/library/functools.html#functools.reduce)

---

## 🤔 Key Concepts to Remember

### **Map, Filter, Reduce Comparison**

| Function | Purpose | Returns | Example |
|----------|---------|---------|---------|
| `map(f, list)` | Transform each element | Iterator | `map(lambda x: x*2, [1,2,3])` → `[2,4,6]` |
| `filter(f, list)` | Select elements by condition | Iterator | `filter(lambda x: x>0, [-1,2,3])` → `[2,3]` |
| `reduce(f, list)` | Combine into single value | Single value | `reduce(lambda x,y: x+y, [1,2,3])` → `6` |

### **Indexing Quick Reference**

```python
my_list = ['A', 'B', 'C', 'D', 'E']
# Positive:  0    1    2    3    4
# Negative: -5   -4   -3   -2   -1

my_list[0]   # 'A' (first)
my_list[-1]  # 'E' (last)
my_list[-2]  # 'D' (second-to-last)
```

### **Traversal Method Selection**

```python
# Only need values? Use direct iteration
for fruit in fruits:
    print(fruit)

# Need indices? Use enumerate (best!)
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

# Need manual control? Use range
for i in range(len(fruits)):
    fruits[i] = fruits[i].upper()
```

### **String ↔ List Conversion**

```python
# String → List of words
sentence = "Hello world"
words = sentence.split()  # ['Hello', 'world']

# String → List of characters
word = "Python"
chars = list(word)  # ['P', 'y', 't', 'h', 'o', 'n']

# List → String
words = ['Python', 'is', 'fun']
sentence = ' '.join(words)  # 'Python is fun'
```

---

## ❓ Common Questions & Troubleshooting

**Q: Why do I need to use `list()` with map and filter?**  
A: `map()` and `filter()` return iterator objects, not lists. Use `list()` to convert them to see the actual values.

**Q: I'm getting "reduce is not defined" error. Why?**  
A: You need to import it first: `from functools import reduce`

**Q: When should I use enumerate vs. range?**  
A: Use `enumerate()` when you need both index and value. It's more Pythonic and readable.

**Q: Can I use negative indices with strings?**  
A: Yes! Strings support all the same indexing and slicing operations as lists.

**Q: What's the difference between split() and split(',')?**  
A: `split()` with no arguments splits on whitespace. `split(',')` splits on commas.

**Q: Can I modify a string using indexing like a list?**  
A: No, strings are immutable. You must create a new string instead.


---

## 🎯 Learning Outcomes Review

After completing Week 17, you should be able to answer these questions:

1. How do map, filter, and reduce differ from each other?
2. When would you use negative indexing in real code?
3. What are the practical uses of membership operators?
4. Which list traversal method is best for different scenarios?
5. How do you convert between strings and lists?
6. What's the best way to process text character by character?
7. How can you combine these concepts to solve complex problems?

---

**Good luck with Week 17! Remember to experiment, ask questions, and practice regularly! 🚀**
