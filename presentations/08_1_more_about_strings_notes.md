# More About Strings

## 1. Strings = Character Lists

A string in Python is a **sequence of characters** — you can think of it as a list of individual characters. You can even convert a string into a list using the `list()` function:

```python
name = 'Siva Jasthi'
print(type(name))         # <class 'str'>

name_lst = list(name)
print(type(name_lst))     # <class 'list'>
print(name_lst)
# ['S', 'i', 'v', 'a', ' ', 'J', 'a', 's', 't', 'h', 'i']
```

> **Key takeaway:** Each character in the string — including spaces — gets its own index position, just like elements in a list.

---

## 2. Strings Support Index Notation

Since strings are sequences, you can access individual characters using **positive** or **negative** indexing:

```python
lang = 'PYTHON'
#       P  Y  T  H  O  N
#       0  1  2  3  4  5     ← positive index (left to right)
#      -6 -5 -4 -3 -2 -1    ← negative index (right to left)
```

| Expression  | Result | Explanation                    |
|-------------|--------|--------------------------------|
| `lang[0]`   | `'P'`  | First character                |
| `lang[5]`   | `'N'`  | Last character                 |
| `lang[-1]`  | `'N'`  | Last character (negative)      |
| `lang[-6]`  | `'P'`  | First character (negative)     |
| `lang[6]`   | **IndexError** | Out of bounds!          |
| `lang[-7]`  | **IndexError** | Out of bounds!          |

> ⚠️ **IndexError:** If you try to access an index that doesn't exist, Python raises an `IndexError`. The valid positive indices for a string of length `n` are `0` through `n-1`.

---

## 3. String Slicing

Slicing lets you extract a **portion** of a string. The syntax is:

```
string[start : stop : step]
```

- **start** — index where the slice begins (inclusive, default `0`)
- **stop** — index where the slice ends (exclusive, default end of string)
- **step** — how many characters to skip (default `1`)

### Examples

```python
text = 'Programming'
#       P  r  o  g  r  a  m  m  i  n  g
#       0  1  2  3  4  5  6  7  8  9  10
```

| Expression         | Result            | Explanation                                     |
|--------------------|-------------------|-------------------------------------------------|
| `text[1:3]`        | `'ro'`            | Characters at index 1 and 2                     |
| `text[:3]`         | `'Pro'`           | From the beginning to index 2                   |
| `text[-2:]`        | `'ng'`            | Last two characters                             |
| `text[:]`          | `'Programming'`   | A copy of the entire string                     |
| `text[1:5:2]`      | `'rg'`            | Index 1, skip to 3 (step of 2)                  |
| `text[1:6:2]`      | `'rgm'`           | Index 1, 3, 5                                   |
| `text[1::2]`       | `'rgamn'`         | Every other character starting from index 1     |
| `text[::-1]`       | `'gnimmargorP'`   | **Reverse** the entire string                   |

> 💡 **Tip:** `text[::-1]` is a quick and elegant way to reverse a string in Python!

---

## 4. Strings are Immutable

Strings **cannot be changed** after they are created. If you try to assign a new character to a specific index, Python will raise a `TypeError`:

```python
input_str = 'Python'
input_str[0] = 'C'   # ❌ TypeError: 'str' object does not support item assignment
```

### How to "Modify" a String — Create a New One

Even though you can't modify the original string, you can build a **brand new** string using slicing and concatenation:

```python
input_str = 'Python'
print('Before:', input_str)   # Before: Python

slice1 = input_str[1:]        # 'ython'
new_string = 'C' + slice1     # 'Cython'

print('New String:', new_string)    # New String: Cython
print('Original:', input_str)       # Original: Python  ← unchanged!
```

### What Happens Behind the Scenes

When you concatenate strings with `+`, Python creates a **new string object** in memory. The variable is reassigned to point to the new object, while the old one becomes an orphan and is eventually cleaned up by **garbage collection**.

```python
name = 'Carmen'
#  name → [ Carmen ]

name = name + ' Brown'
#  name → [ Carmen Brown ]  (new object)
#          [ Carmen ]        (old object — will be garbage collected)
```

---

## 5. Membership Operations (`in` / `not in`)

You can check whether a substring exists inside a string using the `in` and `not in` operators:

```python
text = 'Python programming is cool'

print('python' in text)       # False  — case-sensitive! 'P' ≠ 'p'
print('python' not in text)   # True
print('Python' in text)       # True
print('cool' in text)         # True
```

These operators also work with lists:

```python
some_numbers = [4, 6, 7, 34, 20, 99, 56]

print(99 in some_numbers)       # True
print(88 not in some_numbers)   # True
print(4 not in some_numbers)    # False
```

> ⚠️ **Remember:** String membership checks are **case-sensitive**. `'python' in 'Python'` returns `False`!

---

## 6. Traversing a String

You can loop through every character in a string using a `for` loop — just like iterating over a list.

### Method 1 — Direct Iteration (values only)

```python
name = 'Python'
for ch in name:
    print(ch, end=',')
# P,y,t,h,o,n,
```

### Method 2 — Using `range()` and `len()` (index-based)

```python
name = 'Python'
for idx in range(len(name)):
    print(idx, '-->', name[idx])
# 0 --> P
# 1 --> y
# 2 --> t
# 3 --> h
# 4 --> o
# 5 --> n
```

### Method 3 — Using `enumerate()` (index and value)

```python
name = 'Python'
for idx, value in enumerate(name):
    print(idx, value)
# 0 P
# 1 y
# 2 t
# 3 h
# 4 o
# 5 n
```

---

## 7. Built-in Functions on Strings

Python's built-in functions like `len()`, `max()`, and `min()` work on strings:

```python
name = 'india'
print(len(name))    # 5
print(max(name))    # n   ← highest character alphabetically
print(min(name))    # a   ← lowest character alphabetically
```

```python
name = 'Indigo'
print(len(name))    # 6
print(max(name))    # o
print(min(name))    # I   ← uppercase letters come before lowercase in ASCII!
```

> 💡 **Note:** When comparing characters, Python uses ASCII/Unicode values. Uppercase letters (`A–Z`) have **lower** values than lowercase letters (`a–z`), so `min()` may return an uppercase letter.

---

## 8. String Testing Methods (Querying / Asking)

These methods return `True` or `False` and are useful for **validating** string content:

| Method       | Description                                                                         |
|--------------|-------------------------------------------------------------------------------------|
| `isalnum()`  | Returns `True` if the string contains only letters or digits (at least 1 character) |
| `isalpha()`  | Returns `True` if the string contains only alphabetic letters                       |
| `isdigit()`  | Returns `True` if the string contains only numeric digits                           |
| `islower()`  | Returns `True` if all letters are lowercase                                         |
| `isupper()`  | Returns `True` if all letters are uppercase                                         |
| `isspace()`  | Returns `True` if the string contains only whitespace (spaces, `\n`, `\t`)          |

### Example

```python
s1 = '123'
print(s1.isdigit())    # True
print(s1.isalpha())    # False

s2 = 'PYTHON'
print(s2.isupper())    # True
print(s2.islower())    # False
```

---

## 9. String Modification Methods

These methods return a **new string** — they do **not** change the original (because strings are immutable!).

| Method         | Description                                                    |
|----------------|----------------------------------------------------------------|
| `lower()`      | Returns a copy with all letters converted to lowercase         |
| `upper()`      | Returns a copy with all letters converted to uppercase         |
| `strip()`      | Removes leading and trailing whitespace                        |
| `lstrip()`     | Removes leading (left) whitespace                              |
| `rstrip()`     | Removes trailing (right) whitespace                            |
| `strip(char)`  | Removes specified character from both ends                     |
| `capitalize()` | Converts the first character to uppercase                      |
| `title()`      | Converts the first character of each word to uppercase         |
| `swapcase()`   | Swaps lowercase to uppercase and vice versa                    |

### Example

```python
str_1 = 'Python Programming is COOL'

print(str_1.lower())       # python programming is cool
print(str_1.upper())       # PYTHON PROGRAMMING IS COOL
print(str_1.swapcase())    # pYTHON pROGRAMMING IS cool
print(str_1.title())       # Python Programming Is Cool
```

> 💡 **Important:** All string methods return **new values** — they do **not** change the original string.

---

## 10. Search and Replace Methods

| Method                    | Description                                                          |
|---------------------------|----------------------------------------------------------------------|
| `find(substring)`         | Returns the lowest index where the substring is found; returns `-1` if not found |
| `startswith(substring)`   | Returns `True` if the string starts with the given substring         |
| `endswith(substring)`     | Returns `True` if the string ends with the given substring           |
| `replace(old, new)`       | Returns a copy with all occurrences of `old` replaced by `new`       |
| `count(substring)`        | Returns the number of times a substring appears                      |

### Example — Counting Characters

```python
title = "Oh boy! Python programming is cool"

print(title.count('O'))               # 1
print(title.count('o'))               # 5
print(title.lower().count('o'))       # 6  ← converts to lowercase first!
print(title.upper().count('O'))       # 6  ← converts to uppercase first!
```

> 💡 **Tip:** You can **chain** string methods! `title.lower().count('o')` first converts the string to lowercase, then counts — giving you a case-insensitive count.

---

## 11. Splitting and Tokenizing Strings

The `split()` method breaks a string into a **list** of substrings based on a delimiter (separator).

### Splitting by Whitespace (default)

```python
input_str = 'Python programming is cool'

tokens = input_str.split()
print(tokens)
# ['Python', 'programming', 'is', 'cool']

print('There are', len(tokens), 'words in the sentence')
# There are 4 words in the sentence

print('Second word is', tokens[1])
# Second word is programming
```

### Splitting by a Custom Delimiter

```python
input_str = '1/22/2023'

tokens = input_str.split('/')
print(tokens)
# ['1', '22', '2023']

print('Year:', tokens[2])    # Year: 2023
print('Month:', tokens[0])   # Month: 1
```

### Real-World Example — Parsing a Date and Time

```python
input_str = '1/22/2023 10:00 AM'

tokens_1 = input_str.split()           # ['1/22/2023', '10:00', 'AM']
tokens_2 = tokens_1[0].split('/')      # ['1', '22', '2023']

print('Day:', tokens_2[1])                               # Day: 22
print('Time:', tokens_1[1] + ' ' + tokens_1[2])          # Time: 10:00 AM
```

---

## 12. Formatted Strings (f-strings)

F-strings let you embed expressions directly inside a string using `{ }` placeholders, prefixed with `f`:

```python
name = 'Alex'
marks = 40
gpa = 3.9

print(f"Hi {name}! You got {marks} marks. And your GPA is {gpa}")
# Hi Alex! You got 40 marks. And your GPA is 3.9
```

### Controlling Decimal Places

```python
import math

print(f'The value of pi is approximately {math.pi:.3f}.')
# The value of pi is approximately 3.142.

print(f'The value of pi is approximately {math.pi:.5f}.')
# The value of pi is approximately 3.14159.
```

### Formatting Tables with Column Widths

```python
dictionary = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}

for name, phone in dictionary.items():
    print(f'{name:10} ==> {phone:10}')
# Sjoerd     ==>       4127
# Jack       ==>       4098
# Dcab       ==>       7678
```

The number after `:` sets the **minimum width** of the field, which helps align columns in output.

---

## 13. Repetition Operator (`*`)

The `*` operator repeats a string a given number of times:

```python
some_str = '* '
new_str = some_str * 30
print(new_str)
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
```

This is handy for quickly creating dividers, borders, or patterns in your output.

---

## 14. All String Methods — Quick Reference

Reference: [https://www.w3schools.com/python/python_ref_string.asp](https://www.w3schools.com/python/python_ref_string.asp)

> **Note:** All string methods return new values. They do **not** change the original string.

| Method           | Description                                                                  |
|------------------|------------------------------------------------------------------------------|
| `capitalize()`   | Converts the first character to upper case                                   |
| `casefold()`     | Converts string into lower case                                              |
| `center()`       | Returns a centered string                                                    |
| `count()`        | Returns the number of times a specified value occurs in a string             |
| `encode()`       | Returns an encoded version of the string                                     |
| `endswith()`     | Returns `True` if the string ends with the specified value                   |
| `expandtabs()`   | Sets the tab size of the string                                              |
| `find()`         | Searches for a value and returns the position where it was found             |
| `format()`       | Formats specified values in a string                                         |
| `format_map()`   | Formats specified values in a string                                         |
| `index()`        | Searches for a value and returns the position (raises error if not found)    |
| `isalnum()`      | Returns `True` if all characters are alphanumeric                            |
| `isalpha()`      | Returns `True` if all characters are in the alphabet                         |
| `isascii()`      | Returns `True` if all characters are ASCII characters                        |
| `isdecimal()`    | Returns `True` if all characters are decimals                                |
| `isdigit()`      | Returns `True` if all characters are digits                                  |
| `isidentifier()` | Returns `True` if the string is a valid identifier                           |
| `islower()`      | Returns `True` if all characters are lower case                              |
| `isnumeric()`    | Returns `True` if all characters are numeric                                 |
| `isprintable()`  | Returns `True` if all characters are printable                               |
| `isspace()`      | Returns `True` if all characters are whitespaces                             |
| `istitle()`      | Returns `True` if the string follows title case rules                        |
| `isupper()`      | Returns `True` if all characters are upper case                              |
| `join()`         | Converts the elements of an iterable into a string                           |
| `ljust()`        | Returns a left justified version of the string                               |
| `lower()`        | Converts a string into lower case                                            |
| `lstrip()`       | Returns a left-trimmed version of the string                                 |
| `maketrans()`    | Returns a translation table to be used in translations                       |
| `partition()`    | Returns a tuple where the string is parted into three parts                  |
| `replace()`      | Returns a string where a specified value is replaced with a specified value   |
| `rfind()`        | Searches for a value and returns the last position where it was found        |
| `rindex()`       | Searches for a value and returns the last position (raises error if not found)|
| `rjust()`        | Returns a right justified version of the string                              |
| `rpartition()`   | Returns a tuple where the string is parted into three parts                  |
| `rsplit()`       | Splits the string at the specified separator and returns a list              |
| `rstrip()`       | Returns a right-trimmed version of the string                                |
| `split()`        | Splits the string at the specified separator and returns a list              |
| `splitlines()`   | Splits the string at line breaks and returns a list                          |
| `startswith()`   | Returns `True` if the string starts with the specified value                 |
| `strip()`        | Returns a trimmed version of the string                                      |
| `swapcase()`     | Swaps cases — lower becomes upper and vice versa                             |
| `title()`        | Converts the first character of each word to upper case                      |
| `translate()`    | Returns a translated string                                                  |
| `upper()`        | Converts a string into upper case                                            |
| `zfill()`        | Fills the string with a specified number of 0 values at the beginning        |

---

## 15. Summary

1. **string = character list** — you can use `list()` to convert a string to a list of characters
2. **Subscript notation** — access characters with `x[0]`, `x[1]`, `x[-1]`, etc.
3. **For loops** — you can iterate through a string character by character
4. **IndexError** — you get this when you go out of bounds
5. **`len()`** — returns the length of a string (just like lists)
6. **Concatenation (`+`)** — you can add strings together
7. **Strings are immutable** — you cannot change a string after creation; `name[0] = 'C'` will raise a `TypeError`
8. **F-strings** — strings can be formatted using `f''` strings and `{ }` placeholders
9. **Slicing** — `string[start:stop:step]` extracts portions of a string; `string[::-1]` reverses it
10. **`in` / `not in`** — check for the presence of a substring (case-sensitive!)
11. **Many string methods** — for querying, modification, searching, and splitting/tokenizing
12. **Repetition operator (`*`)** — repeats a string a given number of times

---

*Python 101 | Learn and Help Program | Metropolitan State University*
