# Python List Comprehension

**Course:** Python 101  
**Chapter:** 7 – Lists and Tuples  
**Topic:** List Comprehension  
**Instructor:** Siva R Jasthi | Metropolitan State University  

---

## Quick Recap: What Is a List?

A **list** is a collection that is **ordered** and **changeable**. It allows duplicate members. We use **square brackets** `[]` to create a list.

```python
marks = [10, 8, 7, 0, 9, 11, 10, 10, 4, 5]
```

You can visualize this list like a row of boxes:

```
marks
┌────┬────┬────┬────┬────┬────┬────┬────┬────┬────┐
│ 10 │  8 │  7 │  0 │  9 │ 11 │ 10 │ 10 │  4 │  5 │   ← values
├────┼────┼────┼────┼────┼────┼────┼────┼────┼────┤
│  0 │  1 │  2 │  3 │  4 │  5 │  6 │  7 │  8 │  9 │   ← index positions
└────┴────┴────┴────┴────┴────┴────┴────┴────┴────┘
```

**Think about it:** Who got the highest marks? Who got the lowest marks?

---

## What Is List Comprehension?

List Comprehension is used to **create a new list from an existing list** based on certain conditions. Think of it as a shortcut that combines a `for` loop and (optionally) an `if` statement into a single, clean line of code.

**Why use it?**

- It's an **elegant** way to create lists
- It's **faster** than traditional loops
- It requires **less code**

List Comprehension can do two powerful things:

- **Mapping** — apply an operation to every element
- **Mapping + Filtering** — apply an operation only to elements that meet a condition

---

## The Syntax

```
new_list = [expression for item in iterable if condition]
```

Let's break this down into three parts:

| Part | What It Does | Required? |
|------|-------------|-----------|
| **Expression** (output) | What you want to do with each item | Yes |
| **Iterable** (input sequence) | The list (or range, tuple, etc.) you're looping through | Yes |
| **Condition** (filter) | Only includes items where this is `True` | No (optional) |

> **Remember:** The return value is always a **new list**. The original list stays unchanged!

---

## Example 1: Mapping (Without List Comprehension)

**Goal:** Given a list, create a new list by adding 10 to each element.

```python
given_list = [1, 4, 7, 1]

# Without List Comprehension (the long way)
new_list = []
for item in given_list:
    new_list.append(item + 10)

print(new_list)   # Output: [11, 14, 17, 11]
```

This works, but it takes **4 lines** just to build a new list!

---

## Example 1c: Mapping (With List Comprehension)

**Same goal:** Add 10 to each element — but now in just **one line**.

```python
given_list = [1, 4, 7, 1]

# With List Comprehension (the short way)
new_list = [item + 10 for item in given_list]

print(new_list)   # Output: [11, 14, 17, 11]
```

Let's map this to the syntax:

```
new_list = [item + 10   for item in given_list]
            ─────────   ──────────────────────
            expression   iterable (no condition)
```

Much cleaner, right?

---

## Example 2: Mapping + Filtering (Without List Comprehension)

**Goal:** Given a list, add 5 to each element — but only if the element is **even**.

```python
given_list = [1, 4, 7, 1, 2]

# Without List Comprehension
new_list = []
for item in given_list:
    if item % 2 == 0:           # filtering: only even numbers
        new_list.append(item + 5)   # mapping: add 5

print(new_list)   # Output: [9, 7]
```

Why `[9, 7]`? Because only `4` and `2` are even → `4 + 5 = 9` and `2 + 5 = 7`.

---

## Example 2c: Mapping + Filtering (With List Comprehension)

**Same goal — one line!**

```python
given_list = [1, 4, 7, 1, 2]

# With List Comprehension
new_list = [item + 5 for item in given_list if item % 2 == 0]

print(new_list)   # Output: [9, 7]
```

Let's map this to the syntax:

```
new_list = [item + 5   for item in given_list   if item % 2 == 0]
            ────────   ──────────────────────   ─────────────────
            expression       iterable               condition
```

---

## Example 3: Filtering with Strings

**Goal:** From a list of fruits, create a new list containing only fruits that have the letter "a" in their name.

```python
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# Without List Comprehension
new_list = []
for fruit in fruits:
    if "a" in fruit:
        new_list.append(fruit)

print(new_list)   # Output: ['apple', 'banana', 'mango']
```

```python
# With List Comprehension
new_list = [fruit for fruit in fruits if "a" in fruit]

print(new_list)   # Output: ['apple', 'banana', 'mango']
```

Notice: in this example, the expression is just `fruit` (no transformation) — we're only **filtering**, not mapping.

---

## Example 4: Filtering Even Numbers

**Goal:** Create a new list with only the even numbers from a given list.

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# With List Comprehension
evens = [num for num in numbers if num % 2 == 0]

print(evens)   # Output: [2, 4, 6, 8, 10]
```

---

## Common Mistake: Don't Forget the Square Brackets!

List Comprehension creates a **new list**. You **must** use square brackets `[]`.

```python
# CORRECT
new_list = [x * 2 for x in my_list]

# WRONG — this creates a generator, not a list!
new_list = (x * 2 for x in my_list)
```

> **Always use `[ ]` around your list comprehension!**

---

## The Condition Is Optional

If you leave out the condition, the expression is applied to **every** element.

```python
# With condition (filtering)
# expression for item in iterable if condition
new_list = [x * 2 for x in numbers if x > 3]

# Without condition (no filtering — applies to all)
# expression for item in iterable
new_list = [x * 2 for x in numbers]
```

---

## Condition in the Expression (if...else)

Sometimes you don't want to filter items out — you want to **treat them differently** based on a condition. In that case, put the condition **inside the expression** using `if...else`.

**Syntax:**

```
new_list = [expression1 if condition else expression2 for item in iterable]
```

> **Important:** When using `if...else` in the expression, the condition goes **before** the `for` keyword.

**Example:** Label each number as "even" or "odd":

```python
numbers = [1, 2, 3, 4, 5]

labels = ["even" if x % 2 == 0 else "odd" for x in numbers]

print(labels)   # Output: ['odd', 'even', 'odd', 'even', 'odd']
```

**Example:** Replace negative numbers with 0:

```python
values = [5, -3, 8, -1, 2]

cleaned = [x if x >= 0 else 0 for x in values]

print(cleaned)   # Output: [5, 0, 8, 0, 2]
```

---

## Where Does the `if` Go? A Quick Guide

| What You Want | Syntax | `if` Position |
|--------------|--------|---------------|
| **Filter** items (exclude some) | `[expr for x in list if condition]` | After `iterable` |
| **Transform** items differently | `[expr1 if cond else expr2 for x in list]` | Before `for` |

---

## Cool List Comprehension #1: Split a String into Characters

```python
word = "hello"

chars = [char for char in word]

print(chars)   # Output: ['h', 'e', 'l', 'l', 'o']
```

Since a string is iterable (you can loop through each character), list comprehension works on strings too!

---

## Cool List Comprehension #2: Reverse Each String in a List

```python
words = ["hello", "world", "python"]

reversed_words = [word[::-1] for word in words]

print(reversed_words)   # Output: ['olleh', 'dlrow', 'nohtyp']
```

Here, `word[::-1]` is Python's slice trick to reverse a string.

---

## Summary

List Comprehensions are used to **create new lists** based on existing lists (or other iterables).

Three key elements:

| Element | Description | Required? |
|---------|------------|-----------|
| **Output Expression** | What to do with each item | Yes |
| **Input Sequence** | The iterable to loop through | Yes |
| **Conditional Predicate** | Filter to include/exclude items | Optional |

**The basic pattern:**

```
new_list = [what_you_want   for item in old_list   if some_condition]
```

---

## Practice Challenges

Try these on your own! Use list comprehension for each one.

1. Given `numbers = [1, 2, 3, 4, 5]`, create a new list with each number **squared**.
2. Given `words = ["Cat", "DOG", "Bird"]`, create a new list with each word in **lowercase**.
3. Given `temps_f = [32, 68, 95, 50, 212]`, convert each temperature from **Fahrenheit to Celsius** using the formula `(f - 32) * 5/9`.
4. Given `scores = [85, 42, 97, 63, 78, 55, 91]`, create a new list with only scores **70 or above**.
5. Given `names = ["Alice", "Bob", "Charlie", "Dan", "Eve"]`, create a new list with names that have **more than 3 characters**.
6. Given `numbers = [1, 2, 3, 4, 5, 6]`, create a new list where even numbers are **doubled** and odd numbers stay the **same**. *(Hint: use if...else in the expression)*

---

## Useful Links

- [W3Schools – Python Lists](https://www.w3schools.com/python/python_lists.asp)
- [W3Schools – List Comprehension](https://www.w3schools.com/python/python_lists_comprehension.asp)
- [Think Like a Computer Scientist – Lists](https://openbookproject.net/thinkcs/python/english3e/lists.html)
- [Python Docs – Built-in Functions](https://docs.python.org/3/library/functions.html)
