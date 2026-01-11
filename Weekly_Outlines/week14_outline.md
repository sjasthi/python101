# Week 14: File Input/Output (File I/O) in Python

## 📚 Overview
This week, we'll learn how to work with files in Python! You'll discover how to open files, read their contents in different ways, and properly close them using the `with` statement. File I/O is a crucial skill that allows your programs to store and retrieve data permanently.

---

## 🎯 Learning Objectives
By the end of this week, you will be able to:
- Understand what file I/O is and why it's important
- Open and close files properly using the `with` statement
- Read entire file contents using `read()`
- Read specific number of characters using `read(n)`
- Read one line at a time using `readline()`
- Read all lines into a list using `readlines()`
- Explain the advantages of using the `with` statement
- Choose the appropriate file reading method for different scenarios

---

## 📖 Topics Covered

### 1. Introduction to File I/O
- What is File I/O?
- Why do we need to work with files?
- File paths and file objects
- Opening and closing files

### 2. The `with` Statement
- Syntax: `with open(filename, mode) as file_object:`
- Why use `with`? (Automatic file closing, cleaner code)
- Context managers explained simply

### 3. Reading Files: Four Methods

#### Method 1: `read()` - Read Entire File
- Reads the entire file as one string
- Best for: Small files you want to process as a whole
- Watch out for: Large files can use lots of memory

#### Method 2: `read(n)` - Read N Characters
- Reads exactly `n` characters from the file
- Best for: Reading files in chunks, processing large files
- Useful for: Controlling memory usage

#### Method 3: `readline()` - Read One Line
- Reads one line at a time (including the newline character)
- Best for: Processing files line by line
- Useful with loops to read through entire file

#### Method 4: `readlines()` - Read All Lines into a List
- Reads entire file and returns a list of lines
- Best for: When you need to work with lines as a list
- Each line is a separate element (strings with `\n`)

### 4. Best Practices
- Always use the `with` statement
- Choose the right reading method for your task
- Be mindful of file size and memory
- Handle file not found situations

---

## 📚 Resources

### Core Materials
- **Presentation**: [File I/O Basics](https://github.com/sjasthi/python101/blob/main/presentations/6_1_File_IO_basics.pdf)
  - Complete overview of file operations
  - Visual examples and syntax
  - Best practices and common pitfalls

- **Interactive Notebook**: [File I/O Concepts](https://github.com/sjasthi/python101/blob/main/colab_notebooks/ch6_1_concepts_files_and_exceptions.ipynb)
  - Hands-on code examples
  - Practice exercises
  - Interactive demonstrations

### Practice & Assessment
- **Quiz 14**: [File I/O Playbook Quiz](https://github.com/sjasthi/python101/blob/main/Quizzes/python_file_io_playbook_quiz.html)
  - Test your understanding
  - Multiple choice and coding questions

- **Lab 14**: [File Reading Practice](https://github.com/sjasthi/python101/blob/main/Labs/python101_lab14_file_reading.ipynb)
  - Hands-on file reading exercises
  - Real-world scenarios
  - Auto-graded assignments

---

## 🎓 Class Flow

### Part 1: Introduction (15 minutes)
1. **Hook**: Show examples of programs that use files (saving game progress, reading configuration files, analyzing data from text files)
2. **Discussion**: Why can't we just use variables to store everything?
3. **Quick Demo**: Open a simple text file and display its contents

### Part 2: The `with` Statement (20 minutes)
1. **Explanation**: Why we need to close files and how `with` helps
2. **Live Coding**: 
   - Show the old way (open/close)
   - Show the modern way (with statement)
3. **Practice**: Students try opening a file using `with`

### Part 3: Four Reading Methods (40 minutes)

#### `read()` - 10 minutes
- **Demo**: Read entire file and print
- **Use Case**: Reading a short story or configuration file
- **Practice Exercise**: Read a simple text file

#### `read(n)` - 10 minutes
- **Demo**: Read 50 characters at a time
- **Use Case**: Processing large files in chunks
- **Practice Exercise**: Read first 100 characters of a file

#### `readline()` - 10 minutes
- **Demo**: Read file line by line using a loop
- **Use Case**: Processing log files, CSV files
- **Practice Exercise**: Print each line with line numbers

#### `readlines()` - 10 minutes
- **Demo**: Read all lines into a list and manipulate
- **Use Case**: Need to access lines by index or reverse order
- **Practice Exercise**: Read lines and reverse the order

### Part 4: Comparison & Best Practices (15 minutes)
1. **Comparison Chart**: When to use each method
2. **Common Mistakes**: Not using `with`, choosing wrong method
3. **Q&A Session**

---

## 💻 Hands-On Activities

### Activity 1: Reading a Poem
Read a poem from a text file and display it nicely formatted.

### Activity 2: Line Counter
Write a program that counts the number of lines in a file.

### Activity 3: Word Search
Read a file and find how many times a specific word appears.

### Activity 4: First N Lines
Create a program that reads and displays the first N lines of a file (like the `head` command).

---

## 📝 Assignments

### Quiz 14: File I/O Playbook Quiz
- **Link**: [python_file_io_playbook_quiz.html](https://github.com/sjasthi/python101/blob/main/Quizzes/python_file_io_playbook_quiz.html)
- **Topics**: All file reading methods, `with` statement, best practices
- **Time**: 20-30 minutes
- **Due**: End of week

### Lab 14: File Reading Practice
- **Link**: [python101_lab14_file_reading.ipynb](https://github.com/sjasthi/python101/blob/main/Labs/python101_lab14_file_reading.ipynb)
- **Description**: Hands-on exercises with various file reading scenarios
- **Skills Practiced**: 
  - Using all four reading methods
  - Choosing appropriate method for different tasks
  - File handling with `with` statement
  - Processing file contents
- **Auto-graded**: Yes
- **Due**: End of week

---

## 🔍 Quick Reference

### Basic Syntax

```python
# Read entire file
with open('filename.txt', 'r') as file:
    content = file.read()
    print(content)

# Read n characters
with open('filename.txt', 'r') as file:
    chunk = file.read(100)  # Read first 100 characters
    print(chunk)

# Read one line
with open('filename.txt', 'r') as file:
    line = file.readline()
    print(line)

# Read all lines into a list
with open('filename.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())  # .strip() removes the \n

# Read line by line (memory efficient)
with open('filename.txt', 'r') as file:
    for line in file:
        print(line.strip())
```

### When to Use Which Method?

| Method | Use When | Pros | Cons |
|--------|----------|------|------|
| `read()` | File is small, need entire content | Simple, gets everything | Uses lots of memory for large files |
| `read(n)` | Processing large files in chunks | Memory efficient | Need loop to read entire file |
| `readline()` | Processing one line at a time | Memory efficient, line-by-line control | Need loop for entire file |
| `readlines()` | Need all lines as a list | Easy to work with as list | Uses memory to store all lines |
| `for line in file` | Processing large files line by line | Most memory efficient | Can only iterate once |

---

## 🔮 Looking Ahead: Week 15

Next week, we'll explore error handling in Python!

### Preview Topics:
- **Types of Errors**:
  - Syntax Errors (code structure problems)
  - Logical Errors (code runs but gives wrong results)
  - Runtime Errors (errors that happen while program is running)

- **Exception Handling**:
  - What are exceptions?
  - `try-except` blocks
  - Handling file errors gracefully
  - Why error handling is important

**Connection to This Week**: You'll learn how to handle situations like "file not found" or "permission denied" when working with files!

---

## 💡 Key Takeaways

1. **Always use `with` statement** - It automatically closes files for you
2. **Choose the right method** - Consider file size and what you need to do
3. **Files are read sequentially** - Once you read, the file pointer moves forward
4. **`\n` is a newline character** - You might need to strip it when processing lines
5. **File I/O is powerful** - It allows programs to persist data beyond program execution

---

## ❓ Discussion Questions

1. Why is it important to close files after opening them?
2. What happens if you try to read a very large file using `read()`?
3. When would you use `readline()` instead of `readlines()`?
4. How does the `with` statement make our code safer?
5. Can you think of real-world programs that need to read files?

---

## 🏆 Success Criteria

You've mastered this week's content when you can:
- ✅ Explain the purpose of the `with` statement
- ✅ Write code to read a file using all four methods
- ✅ Choose the appropriate reading method for different scenarios
- ✅ Understand the differences between each reading method
- ✅ Handle basic file operations without errors
- ✅ Process file contents (counting lines, searching words, etc.)

---

**Happy Coding! 🎉**

Remember: File I/O opens up a whole new world of possibilities for your programs. You can now create programs that save and load data, process text files, analyze logs, and much more!
