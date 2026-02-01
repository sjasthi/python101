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


  
- **Materials**:
  - Presentation: [7_2_and_7_3_python_lists_map_filter_reduce_plus.md](https://github.com/sjasthi/python101/blob/main/presentations/7_2_and_7_3_python_lists_map_filter_reduce_plus.md)
  - Colab Notebook: [ch7_concepts_list_intro_1.ipynb](https://github.com/sjasthi/python101/blob/main/colab_notebooks/ch7_concepts_list_intro_1.ipynb)
  
  
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


## 🔗 All Resources

### **Presentation Materials**
- [Main Presentation](https://github.com/sjasthi/python101/blob/main/presentations/7_2_and_7_3_python_lists_map_filter_reduce_plus.md)

### **Interactive Learning**
- [Interactive Playbook & Quiz](https://github.com/sjasthi/python101/blob/main/Quizzes/lists_map_filter_reduce_traversals_playbook_and_quiz.html)
- [Colab Notebook](https://github.com/sjasthi/python101/blob/main/colab_notebooks/ch7_concepts_list_intro_1.ipynb)

### **Lab Assignment** 
- **Description**: Hands-on programming exercises
- **Location**: [python101_map_filter_reduce_list_traversals.ipynb](https://github.com/sjasthi/python101/blob/main/Labs/python101_map_filter_reduce_list_traversals.ipynb)

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
