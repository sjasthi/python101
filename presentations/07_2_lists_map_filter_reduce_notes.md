# Python 101: Lists - Map, Filter, Reduce

## 🎯 What We'll Learn Today

This week, we're diving deeper into **lists**! You already know the basics, and now we'll learn powerful techniques to work with lists like a pro:

- **Map**: Transform every item in a list
- **Filter**: Pick only the items you want
- **Reduce**: Combine all items into one result
- **Negative Indexing**: Access items from the end
- **Membership Operators**: Check if items are in a list
- **Traversals**: Different ways to loop through lists
- **Lists & Strings**: How strings and lists are related

---

## 📝 Quick Review: What is a List?

A **list** is like a backpack where you can store multiple items in order.

```python
video_games = ["Minecraft", "Roblox", "Fortnite", "Among Us"]
test_scores = [85, 92, 78, 95, 88]
mixed_bag = ["pizza", 42, True, 3.14]
```

---

## 🗺️ Part 1: Map - Transform Every Item

### What is Map?

**Map** means applying the same operation to every item in a list to create a **new list**.

Think of it like this: You have a list of numbers, and you want to double each one. Instead of doing it manually, you "map" a doubling operation across all items!

### Example 1: Doubling Numbers

```python
# Original list
points = [10, 20, 30, 40, 50]

# Using a for loop (the old way)
doubled_points = []
for point in points:
    doubled_points.append(point * 2)

print(doubled_points)  # [20, 40, 60, 80, 100]
```

### Example 2: Converting Temperatures

Let's convert Celsius temperatures to Fahrenheit!

```python
# Formula: F = C * 9/5 + 32
celsius_temps = [0, 10, 20, 30, 40]

fahrenheit_temps = []
for temp in celsius_temps:
    fahrenheit = temp * 9/5 + 32
    fahrenheit_temps.append(fahrenheit)

print(fahrenheit_temps)  # [32.0, 50.0, 68.0, 86.0, 104.0]
```

### Example 3: Adding Exclamation Marks

```python
# Make every message more exciting!
messages = ["Good job", "Amazing work", "Keep it up", "Fantastic"]

excited_messages = []
for message in messages:
    excited_messages.append(message + "!")

print(excited_messages)
# ['Good job!', 'Amazing work!', 'Keep it up!', 'Fantastic!']
```

### 🎮 Practice: Map

1. You have a list of player levels `[5, 12, 8, 20, 15]`. Add 3 levels to each player (they all got a bonus!). Create a new list with the updated levels.

2. You have a list of words `["cat", "dog", "bird", "fish"]`. Create a new list where each word is in UPPERCASE.

3. You have prices in dollars `[10, 25, 50, 100]`. Apply a 20% discount to each price (multiply by 0.8) and create a new list.

---

## 🔍 Part 2: Filter - Pick What You Want

### What is Filter?

**Filter** means selecting only the items that meet a certain condition. The new list will be **shorter** (or the same length) than the original.

Think of it like this: You have a list of numbers, and you only want the even ones. You "filter out" the odd numbers!

### Example 1: Filtering Even Numbers

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = []
for num in numbers:
    if num % 2 == 0:  # Check if even
        even_numbers.append(num)

print(even_numbers)  # [2, 4, 6, 8, 10]
```

### Example 2: Filtering Passing Grades

```python
test_scores = [45, 78, 92, 55, 88, 62, 95, 40]

passing_scores = []
for score in test_scores:
    if score >= 60:  # 60 or higher is passing
        passing_scores.append(score)

print(passing_scores)  # [78, 92, 88, 62, 95]
print(f"Students passed: {len(passing_scores)} out of {len(test_scores)}")
```

### Example 3: Filtering Long Words

```python
words = ["hi", "hello", "hey", "goodbye", "sup", "greetings"]

long_words = []
for word in words:
    if len(word) > 4:  # More than 4 letters
        long_words.append(word)

print(long_words)  # ['hello', 'goodbye', 'greetings']
```

### 🎮 Practice: Filter

1. You have temperatures `[72, 85, 90, 68, 95, 78, 88]`. Filter to get only temperatures above 80°F (hot days!).

2. You have a list of ages `[10, 15, 12, 18, 13, 20, 11]`. Filter to get only ages between 12 and 17 (middle/high school age).

3. You have video game names `["Minecraft", "Roblox", "Among Us", "Valorant", "Fall Guys"]`. Filter to get only games with 8 or more letters in their name.

---

## ➕ Part 3: Reduce - Combine to One Value

### What is Reduce?

**Reduce** means combining all items in a list to get a **single result**. Common examples: sum, maximum, minimum, average, product.

### Example 1: Sum (Total)

```python
scores = [10, 25, 15, 30, 20]

total = 0
for score in scores:
    total = total + score  # Or: total += score

print(f"Total score: {total}")  # 100
```

### Example 2: Maximum Value

```python
high_scores = [450, 890, 720, 1050, 680]

max_score = high_scores[0]  # Start with first value
for score in high_scores:
    if score > max_score:
        max_score = score

print(f"Highest score: {max_score}")  # 1050
```

### Example 3: Minimum Value

```python
temperatures = [72, 68, 75, 65, 70, 62, 69]

min_temp = temperatures[0]  # Start with first value
for temp in temperatures:
    if temp < min_temp:
        min_temp = temp

print(f"Coldest temperature: {min_temp}°F")  # 62
```

### Example 4: Average

```python
quiz_grades = [85, 90, 78, 92, 88]

# Step 1: Find the sum
total = 0
for grade in quiz_grades:
    total += grade

# Step 2: Divide by count
average = total / len(quiz_grades)

print(f"Average grade: {average}")  # 86.6
```

### Example 5: Product (Multiply All)

```python
numbers = [2, 3, 4, 5]

product = 1  # Start with 1 (not 0!)
for num in numbers:
    product *= num

print(f"Product: {product}")  # 120 (2 * 3 * 4 * 5)
```

### 🎯 Built-in Functions for Reduce

Python has built-in functions for common reduce operations:

```python
numbers = [10, 25, 15, 30, 20]

print(sum(numbers))    # 100 - Total
print(max(numbers))    # 30 - Maximum
print(min(numbers))    # 10 - Minimum
print(len(numbers))    # 5 - Count
```

### 🎮 Practice: Reduce

1. You have collected coins in a game: `[50, 75, 100, 25, 150]`. Find the total coins collected.

2. You have daily steps: `[8000, 12000, 6500, 10000, 9500, 11000, 7500]`. Find the average daily steps.

3. You have prices: `[12.99, 8.50, 25.00, 15.75]`. Find both the most expensive and cheapest items.

---

## 🔄 Part 4: Negative Indexing

### What is Negative Indexing?

**Negative indexing** lets you access items from the **end** of the list, using negative numbers!

```python
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
#          0        1         2         3       4          <- Positive index
#         -5       -4        -3        -2      -1          <- Negative index
```

### Why Use Negative Indexing?

- **-1** always gets the last item
- **-2** always gets the second-to-last item
- You don't need to know the list length!

### Examples

```python
games = ["Minecraft", "Roblox", "Fortnite", "Among Us", "Valorant"]

# Positive indexing
print(games[0])     # "Minecraft" - first item
print(games[4])     # "Valorant" - last item (need to know length!)

# Negative indexing
print(games[-1])    # "Valorant" - last item (don't need length!)
print(games[-2])    # "Among Us" - second to last
print(games[-5])    # "Minecraft" - same as [0]
```

### Real-World Use Cases

```python
scores = [85, 90, 78, 92, 88, 95]

# Get the last 3 scores
last_three = scores[-3:]
print(last_three)  # [88, 95]

# Remove the last item
scores_without_last = scores[:-1]
print(scores_without_last)  # [85, 90, 78, 92, 88]

# Get everything except first and last
middle_scores = scores[1:-1]
print(middle_scores)  # [90, 78, 92, 88]
```

### 🎮 Practice: Negative Indexing

Given this list:
```python
players = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank"]
```

1. Print the last player's name
2. Print the second-to-last player's name
3. Print the last 2 players
4. Print all players except the last one

---

## ✅ Part 5: Membership Operators

### The `in` Operator

Check if an item **exists** in a list:

```python
favorite_foods = ["pizza", "tacos", "sushi", "burgers", "pasta"]

print("pizza" in favorite_foods)     # True
print("broccoli" in favorite_foods)  # False
```

### The `not in` Operator

Check if an item **does NOT exist** in a list:

```python
completed_levels = [1, 2, 3, 5, 7, 8]

print(4 not in completed_levels)  # True (level 4 not completed)
print(5 not in completed_levels)  # False (level 5 is completed)
```

### Real-World Examples

#### Example 1: Access Control

```python
vip_members = ["Alice", "Bob", "Charlie"]
username = "Diana"

if username in vip_members:
    print("Welcome, VIP! You get special access! 🌟")
else:
    print("Welcome! Sign up for VIP for special perks!")
```

#### Example 2: Quiz Checker

```python
correct_answers = ["A", "C", "B", "D", "A"]
student_answer = "C"
question_number = 2

if student_answer == correct_answers[question_number - 1]:
    print("✓ Correct!")
else:
    print("✗ Incorrect")
```

#### Example 3: Ingredient Checker

```python
available_ingredients = ["flour", "eggs", "milk", "butter", "sugar"]
needed_ingredients = ["eggs", "milk", "vanilla"]

for ingredient in needed_ingredients:
    if ingredient in available_ingredients:
        print(f"✓ We have {ingredient}")
    else:
        print(f"✗ We need to buy {ingredient}")
```

### 🎮 Practice: Membership Operators

```python
enrolled_courses = ["Math", "Science", "English", "History", "PE"]
```

1. Check if "Science" is in the enrolled courses
2. Check if "Art" is NOT in the enrolled courses
3. Write a program that asks the user for a course name and tells them if they're enrolled in it

---

## 🔁 Part 6: Three Types of Traversals

**Traversal** means going through each item in a list. There are **3 main ways** to do this!

### Method 1: For-Each Loop (Most Common!)

Use this when you **only need the value**, not the position.

```python
fruits = ["apple", "banana", "cherry", "date"]

for fruit in fruits:
    print(f"I like {fruit}s!")
```

**Output:**
```
I like apples!
I like bananas!
I like cherrys!
I like dates!
```

### Method 2: Index-Based Loop

Use this when you **need the index** (position number).

```python
fruits = ["apple", "banana", "cherry", "date"]

for idx in range(len(fruits)):
    print(f"Item {idx}: {fruits[idx]}")
```

**Output:**
```
Item 0: apple
Item 1: banana
Item 2: cherry
Item 3: date
```

### Method 3: Enumerate (Best of Both!)

Use this when you need **both index AND value**.

```python
fruits = ["apple", "banana", "cherry", "date"]

for idx, fruit in enumerate(fruits):
    print(f"#{idx + 1}: {fruit}")
```

**Output:**
```
#1: apple
#2: banana
#3: cherry
#4: date
```

### Comparison Example: Leaderboard

Let's print a game leaderboard using all three methods:

```python
players = ["Alice", "Bob", "Charlie", "Diana"]
scores = [1500, 1200, 1000, 800]
```

#### Method 1: For-Each (just names)
```python
for player in players:
    print(player)
# Just prints: Alice, Bob, Charlie, Diana
```

#### Method 2: Index-Based (with scores)
```python
for i in range(len(players)):
    print(f"{players[i]}: {scores[i]} points")
```
**Output:**
```
Alice: 1500 points
Bob: 1200 points
Charlie: 1000 points
Diana: 800 points
```

#### Method 3: Enumerate (with rank)
```python
for rank, player in enumerate(players):
    print(f"Rank #{rank + 1}: {player} - {scores[rank]} points")
```
**Output:**
```
Rank #1: Alice - 1500 points
Rank #2: Bob - 1200 points
Rank #3: Charlie - 1000 points
Rank #4: Diana - 800 points
```

### When to Use Each Method?

| Method | When to Use | Example |
|--------|-------------|---------|
| **For-Each** | You only need the value | Printing all items |
| **Index-Based** | You need position numbers or need to modify the list | Swapping items, accessing related lists |
| **Enumerate** | You need both value AND position | Numbered lists, rankings |

### 🎮 Practice: Traversals

Given these lists:
```python
subjects = ["Math", "Science", "English", "History"]
grades = [85, 92, 78, 88]
```

1. Use a **for-each loop** to print each subject
2. Use an **index-based loop** to print each subject with its grade
3. Use **enumerate** to print a report card with numbers (e.g., "1. Math: 85")

---

## 🔤 Part 7: Lists and Strings

### Strings Are Like Character Lists!

A string is actually a sequence of characters, so you can treat it like a list in many ways!

```python
word = "PYTHON"
print(word[0])      # 'P' - first character
print(word[-1])     # 'N' - last character
print(word[2:4])    # 'TH' - slicing works!
print(len(word))    # 6 - length works!
```

### Looping Through Strings

```python
message = "HELLO"

# Method 1: For-each (characters)
for char in message:
    print(char)  # H, E, L, L, O (one per line)

# Method 2: Index-based
for i in range(len(message)):
    print(f"Character {i}: {message[i]}")

# Method 3: Enumerate
for idx, char in enumerate(message):
    print(f"Position {idx}: {char}")
```

### Membership Operators with Strings

```python
sentence = "I love Python programming"

print("Python" in sentence)      # True
print("Java" in sentence)        # False
print("love" not in sentence)    # False
```

### Converting Between Strings and Lists

#### Split: String → List

```python
sentence = "Learning Python is fun"
words = sentence.split()  # Split by spaces
print(words)  # ['Learning', 'Python', 'is', 'fun']

# Split by other characters
csv_data = "apple,banana,cherry"
fruits = csv_data.split(",")
print(fruits)  # ['apple', 'banana', 'cherry']
```

#### Join: List → String

```python
words = ["Learning", "Python", "is", "fun"]
sentence = " ".join(words)  # Join with spaces
print(sentence)  # "Learning Python is fun"

# Join with other characters
fruits = ["apple", "banana", "cherry"]
csv_data = ",".join(fruits)
print(csv_data)  # "apple,banana,cherry"
```

### String as a Character List

```python
name = "MINECRAFT"

# Count characters
print(len(name))  # 9

# Get first and last
print(f"First letter: {name[0]}")   # M
print(f"Last letter: {name[-1]}")   # T

# Slice
print(name[0:4])    # MINE
print(name[4:])     # CRAFT

# Check for letters
if 'M' in name:
    print("Found M!")
```

### Cool String Operations

#### Example 1: Vowel Counter

```python
word = "EDUCATION"
vowels = "AEIOU"

vowel_count = 0
for letter in word:
    if letter in vowels:
        vowel_count += 1

print(f"{word} has {vowel_count} vowels")  # 5 vowels
```

#### Example 2: Reverse a String

```python
text = "HELLO"
reversed_text = ""

for char in text:
    reversed_text = char + reversed_text

print(reversed_text)  # "OLLEH"

# Or use slicing!
print(text[::-1])  # "OLLEH"
```

#### Example 3: Character Frequency

```python
word = "MISSISSIPPI"

for letter in "MSIPI":  # Unique letters to check
    count = 0
    for char in word:
        if char == letter:
            count += 1
    print(f"{letter}: {count}")
```

**Output:**
```
M: 1
S: 4
I: 4
P: 2
```

### 🎮 Practice: Lists and Strings

1. Write a program that counts how many times the letter 'E' appears in "MINECRAFT"

2. Split this sentence into a list of words: `"Python is awesome and fun"`

3. Take this list `["I", "love", "coding"]` and join it into a sentence with spaces

4. Write a program that checks if a string is a palindrome (reads the same forwards and backwards) like "RACECAR"

---

## 🎯 Comprehensive Practice Problems

### Problem 1: Grade Calculator
```python
# You have test scores
scores = [78, 85, 92, 88, 76, 95, 82]

# Tasks:
# 1. Map: Add 5 bonus points to each score
# 2. Filter: Get only scores above 85
# 3. Reduce: Find the average score
```

### Problem 2: Word Processor
```python
# You have a list of words
words = ["python", "java", "javascript", "ruby", "go", "rust"]

# Tasks:
# 1. Map: Convert all words to uppercase
# 2. Filter: Get only words with more than 4 letters
# 3. Reduce: Find the longest word
# 4. Check if "python" is in the list
# 5. Use enumerate to print numbered list
```

### Problem 3: Temperature Analyzer
```python
# Weekly temperatures in Fahrenheit
temps = [72, 75, 68, 82, 79, 85, 70]
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

# Tasks:
# 1. Map: Convert all temps to Celsius (C = (F - 32) * 5/9)
# 2. Filter: Find days where temp was above 75°F
# 3. Reduce: Find hottest and coldest days
# 4. Use enumerate to print each day with its temperature
```

### Problem 4: Gaming Statistics
```python
# Player inventory
inventory = ["sword", "shield", "potion", "potion", "gem", "sword", "potion"]

# Tasks:
# 1. Count how many potions the player has
# 2. Check if player has a "shield"
# 3. Remove duplicate items (create a unique list)
# 4. Print inventory with item numbers using enumerate
```

---

## 💡 Quick Reference Guide

### Map, Filter, Reduce
```python
# MAP: Transform each item
new_list = []
for item in original_list:
    new_list.append(transform(item))

# FILTER: Select specific items
new_list = []
for item in original_list:
    if condition:
        new_list.append(item)

# REDUCE: Combine to one value
result = starting_value
for item in original_list:
    result = combine(result, item)
```

### Indexing
```python
my_list = [10, 20, 30, 40, 50]
my_list[0]     # 10 (first)
my_list[-1]    # 50 (last)
my_list[-2]    # 40 (second to last)
```

### Membership
```python
if item in my_list:      # Check if exists
if item not in my_list:  # Check if doesn't exist
```

### Traversals
```python
# 1. For-each (value only)
for value in my_list:
    print(value)

# 2. Index-based (index only, get value using index)
for i in range(len(my_list)):
    print(my_list[i])

# 3. Enumerate (both!)
for idx, value in enumerate(my_list):
    print(idx, value)
```

### Strings
```python
text = "HELLO"
text.split()         # String → List
" ".join(my_list)    # List → String
for char in text:    # Loop through characters
```

---

## 🏆 Challenge Projects

### Challenge 1: Student Grade Manager
Create a program that:
- Has a list of student names and scores
- Adds bonus points to all scores (map)
- Filters to show only passing grades (filter)
- Calculates class average (reduce)
- Shows a ranked list with enumerate

### Challenge 2: Word Game
Create a program that:
- Takes a sentence from the user
- Splits it into words
- Filters words longer than 5 letters
- Converts filtered words to uppercase
- Joins them back with dashes

### Challenge 3: Temperature Tracker
Create a program that:
- Stores daily temperatures for a week
- Finds hot days (over 80°F)
- Finds cold days (under 65°F)
- Calculates average temperature
- Shows day-by-day report with enumerate

---

## 🎓 Key Takeaways

1. **Map** creates a new list by transforming each item
2. **Filter** creates a shorter list by selecting certain items
3. **Reduce** combines all items into a single result
4. **Negative indexing** (`-1`, `-2`) accesses items from the end
5. **`in` and `not in`** check if items exist in a list
6. **Three traversal methods**: for-each, index-based, and enumerate
7. **Strings can be treated like character lists** for many operations

 List comprehensions (a super-fast way to create lists!)

Keep practicing with lists – they're one of the most important tools in Python! 🚀
