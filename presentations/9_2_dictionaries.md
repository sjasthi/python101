# Python Dictionaries

## 1. Lists vs Tuples vs Sets vs Dictionaries — What's the Difference?

You already know **lists**, **tuples**, and **sets**. A **dictionary** is the fourth major collection type in Python — and it works very differently from the others!

| Feature              | Lists `[ ]`     | Tuples `( )`    | Sets `{ }`      | Dictionaries `{ : }` |
|----------------------|-----------------|-----------------|-----------------|----------------------|
| Ordered              | ✅              | ✅              | ❌              | ✅ (Python 3.7+)     |
| Indexed              | ✅              | ✅              | ❌              | ❌ (uses **keys**)   |
| Add or Update items  | ✅              | ❌              | ✅ (add only)   | ✅                   |
| Can contain duplicates | ✅            | ✅              | ❌              | ❌ (keys must be unique) |
| Mutable              | ✅              | ❌              | ✅              | ✅                   |
| Uses                 | Square Brackets `[ ]` | Round Brackets `( )` | Curly Braces `{ }` | Curly Braces with colons `{ key: value }` |

> **Key takeaway:** Dictionaries store data as **key-value pairs** — like a real dictionary where each **word** (key) has a **definition** (value). Instead of using index numbers (0, 1, 2…), you look things up by their **key**.

---

## 2. Real-World Examples of Dictionaries

Think of key-value pairs everywhere in daily life:

| Real-World Example        | Key               | Value              |
|---------------------------|--------------------|--------------------|
| English Dictionary        | Word               | Definition         |
| Phone Contacts            | Contact Name       | Phone Number       |
| Student Report Card       | Subject            | Grade              |
| Periodic Table            | Element Symbol     | Element Name       |
| Country Capitals          | Country            | Capital City       |
| Menu at a Restaurant      | Food Item          | Price              |

> 🧠 **Think of it this way:** A dictionary is like your phone's contact list — you don't look up a contact by position #47, you search by **name** (the key) and get their **number** (the value).

---

## 3. CRUD Operations on Dictionaries

Dictionaries support **all four** CRUD operations:

- **C – Create** (build a dictionary with initial key-value pairs)
- **R – Read** (access values by key, traverse, search)
- **U – Update** (modify existing values, add new key-value pairs)
- **D – Delete** (remove individual pairs, or clear the entire dictionary)

> Compare this to tuples (C and R only) and sets (C, R, and partial U/D). Dictionaries are the most flexible!

---

## 4. Creating a Dictionary

### Using Curly Braces `{ }`

```python
student = {"name": "Alice", "age": 13, "grade": "8th"}
print(student)
# {'name': 'Alice', 'age': 13, 'grade': '8th'}
print(type(student))  # <class 'dict'>
```

### Using the `dict()` Constructor

```python
student = dict(name="Alice", age=13, grade="8th")
print(student)
# {'name': 'Alice', 'age': 13, 'grade': '8th'}
```

### Creating an Empty Dictionary

```python
# Both ways work for an empty dictionary:
empty1 = {}
empty2 = dict()
print(type(empty1))  # <class 'dict'>
print(type(empty2))  # <class 'dict'>
```

> ⚠️ **Recall from Sets:** `{}` creates an empty **dictionary**, NOT an empty set. For an empty set, you must use `set()`.

### Dictionary with Different Value Types

```python
student = {
    "name": "Alice",        # str value
    "age": 13,              # int value
    "gpa": 3.85,            # float value
    "is_active": True,      # bool value
    "hobbies": ["art", "coding"]  # list value
}
```

> 📝 **Rules for Keys:**
> - Keys must be **unique** — if you repeat a key, the last value wins
> - Keys must be **immutable** types (strings, numbers, tuples) — you cannot use lists or sets as keys

---

## 5. Reading from a Dictionary

### 5.1 Access a Value by Key

```python
student = {"name": "Alice", "age": 13, "grade": "8th"}

print(student["name"])    # Alice
print(student["age"])     # 13
```

**What if the key doesn't exist?**

```python
print(student["email"])   # ❌ KeyError: 'email'
```

### 5.2 Using `.get()` — Safer Access

```python
print(student.get("name"))     # Alice
print(student.get("email"))    # None  (no error!)
print(student.get("email", "N/A"))  # N/A  (custom default)
```

> 💡 **Tip:** Use `.get()` when you're not sure if a key exists. It returns `None` (or a default you choose) instead of crashing with a `KeyError`.

### 5.3 Check if a Key Exists

```python
student = {"name": "Alice", "age": 13, "grade": "8th"}

print("name" in student)     # True
print("email" in student)    # False
print("email" not in student)  # True
```

### 5.4 Get All Keys, Values, or Pairs

```python
student = {"name": "Alice", "age": 13, "grade": "8th"}

print(student.keys())    # dict_keys(['name', 'age', 'grade'])
print(student.values())  # dict_values(['Alice', 13, '8th'])
print(student.items())   # dict_items([('name', 'Alice'), ('age', 13), ('grade', '8th')])
```

### 5.5 Find the Number of Key-Value Pairs

```python
student = {"name": "Alice", "age": 13, "grade": "8th"}
print(len(student))  # 3
```

### 5.6 Looping Through a Dictionary

**Loop through keys (default):**

```python
student = {"name": "Alice", "age": 13, "grade": "8th"}

for key in student:
    print(key)
# name
# age
# grade
```

**Loop through values:**

```python
for value in student.values():
    print(value)
# Alice
# 13
# 8th
```

**Loop through key-value pairs:**

```python
for key, value in student.items():
    print(f"{key}: {value}")
# name: Alice
# age: 13
# grade: 8th
```

---

## 6. Updating a Dictionary

### 6.1 Change an Existing Value

```python
student = {"name": "Alice", "age": 13, "grade": "8th"}

student["age"] = 14
print(student)
# {'name': 'Alice', 'age': 14, 'grade': '8th'}
```

### 6.2 Add a New Key-Value Pair

```python
student["email"] = "alice@school.com"
print(student)
# {'name': 'Alice', 'age': 14, 'grade': '8th', 'email': 'alice@school.com'}
```

> 📝 **Same syntax, two behaviors:** If the key already exists, it **updates** the value. If the key is new, it **adds** the pair.

### 6.3 Using `.update()` — Add/Change Multiple Pairs at Once

```python
student = {"name": "Alice", "age": 13}

student.update({"age": 14, "grade": "8th", "email": "alice@school.com"})
print(student)
# {'name': 'Alice', 'age': 14, 'grade': '8th', 'email': 'alice@school.com'}
```

---

## 7. Deleting from a Dictionary

### 7.1 `pop(key)` — Remove a Specific Key and Get Its Value

```python
student = {"name": "Alice", "age": 14, "grade": "8th"}

removed_value = student.pop("age")
print(removed_value)  # 14
print(student)        # {'name': 'Alice', 'grade': '8th'}
```

### 7.2 `popitem()` — Remove the Last Inserted Pair

```python
student = {"name": "Alice", "age": 14, "grade": "8th"}

last_item = student.popitem()
print(last_item)  # ('grade', '8th')
print(student)    # {'name': 'Alice', 'age': 14}
```

### 7.3 `del` — Delete a Specific Key or the Entire Dictionary

```python
student = {"name": "Alice", "age": 14, "grade": "8th"}

del student["grade"]
print(student)  # {'name': 'Alice', 'age': 14}

del student     # Deletes the entire dictionary
# print(student)  # ❌ NameError: 'student' is not defined
```

### 7.4 `clear()` — Empty the Dictionary (Keep the Variable)

```python
student = {"name": "Alice", "age": 14, "grade": "8th"}

student.clear()
print(student)  # {}
```

---

## 8. Dictionary Methods — Summary Table

| Method           | Purpose                                                     |
|------------------|-------------------------------------------------------------|
| `get(key)`       | Returns the value for a key (returns `None` if not found)   |
| `keys()`         | Returns all keys                                            |
| `values()`       | Returns all values                                          |
| `items()`        | Returns all key-value pairs as tuples                       |
| `update(dict2)`  | Adds/updates multiple key-value pairs from another dict     |
| `pop(key)`       | Removes the key and returns its value                       |
| `popitem()`      | Removes and returns the last inserted key-value pair        |
| `clear()`        | Removes all items from the dictionary                       |
| `copy()`         | Returns a shallow copy of the dictionary                    |
| `setdefault(key, default)` | Returns value if key exists; if not, inserts key with default |
| `fromkeys(keys, value)`    | Creates a new dictionary from a list of keys with a shared value |

---

## 9. Nested Dictionaries

A dictionary can contain **other dictionaries** as values — this is called **nesting**.

```python
students = {
    "student1": {"name": "Alice", "age": 13},
    "student2": {"name": "Bob", "age": 14},
    "student3": {"name": "Charlie", "age": 13}
}

print(students["student1"])           # {'name': 'Alice', 'age': 13}
print(students["student1"]["name"])   # Alice
print(students["student2"]["age"])    # 14
```

### Looping Through a Nested Dictionary

```python
for student_id, info in students.items():
    print(f"{student_id}: {info['name']}, age {info['age']}")
# student1: Alice, age 13
# student2: Bob, age 14
# student3: Charlie, age 13
```

---

## 10. Dictionary Comprehension

Just like list comprehension, you can build dictionaries in a **single line**:

```python
# Create a dictionary of squares
squares = {x: x**2 for x in range(1, 6)}
print(squares)
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

```python
# Convert a list of names to a dictionary with name lengths
names = ["Alice", "Bob", "Charlie"]
name_lengths = {name: len(name) for name in names}
print(name_lengths)
# {'Alice': 5, 'Bob': 3, 'Charlie': 7}
```

---

## 11. Converting Between Data Structures

### List of Tuples → Dictionary

```python
pairs = [("name", "Alice"), ("age", 13), ("grade", "8th")]
student = dict(pairs)
print(student)  # {'name': 'Alice', 'age': 13, 'grade': '8th'}
```

### Two Lists → Dictionary (using `zip`)

```python
keys = ["name", "age", "grade"]
values = ["Alice", 13, "8th"]

student = dict(zip(keys, values))
print(student)  # {'name': 'Alice', 'age': 13, 'grade': '8th'}
```

### Dictionary → List of Keys / Values

```python
student = {"name": "Alice", "age": 13, "grade": "8th"}

key_list = list(student.keys())
print(key_list)    # ['name', 'age', 'grade']

value_list = list(student.values())
print(value_list)  # ['Alice', 13, '8th']
```

---

## 12. Common Dictionary Patterns

### Counting Occurrences

```python
word = "mississippi"
letter_count = {}

for letter in word:
    if letter in letter_count:
        letter_count[letter] += 1
    else:
        letter_count[letter] = 1

print(letter_count)
# {'m': 1, 'i': 4, 's': 4, 'p': 2}
```

**Shorter version using `.get()`:**

```python
word = "mississippi"
letter_count = {}

for letter in word:
    letter_count[letter] = letter_count.get(letter, 0) + 1

print(letter_count)
# {'m': 1, 'i': 4, 's': 4, 'p': 2}
```

### Finding the Max Value

```python
scores = {"Alice": 95, "Bob": 87, "Charlie": 92}

top_student = max(scores, key=scores.get)
print(f"{top_student} has the highest score: {scores[top_student]}")
# Alice has the highest score: 95
```

---

## 13. When to Use Dictionaries

| Use a **Dictionary** when…                        | Use a **List** when…                     |
|---------------------------------------------------|------------------------------------------|
| You need to look things up by a **name/label**     | You need items in a specific **order**    |
| Each item has a **key** and a **value**            | You just have a collection of **values**  |
| You want **fast lookups** by key                   | You need to access items by **position**  |
| Keys are unique identifiers (IDs, names, codes)    | Duplicate values are okay                 |

**Great real-world uses for dictionaries:**

- 📱 **Contacts app** — name → phone number
- 📊 **Grade book** — student name → grade
- 🌍 **Country data** — country → capital
- 🧪 **Periodic table** — symbol → element name
- 🛒 **Shopping cart** — item name → quantity
- 🎮 **Game inventory** — item → count

---

## 14. Quick CRUD Cheat Sheet

| Operation | Code Example                                   | Description                    |
|-----------|-------------------------------------------------|--------------------------------|
| **Create**   | `d = {"a": 1, "b": 2}`                      | Create with initial pairs      |
| **Create**   | `d = dict(a=1, b=2)`                         | Create using `dict()`          |
| **Read**     | `d["a"]` or `d.get("a")`                     | Access value by key            |
| **Read**     | `d.keys()`, `d.values()`, `d.items()`         | Get keys, values, or pairs     |
| **Read**     | `"a" in d`                                    | Check if key exists            |
| **Read**     | `for k, v in d.items():`                      | Loop through all pairs         |
| **Update**   | `d["a"] = 10`                                 | Change existing value          |
| **Update**   | `d["c"] = 3`                                  | Add new key-value pair         |
| **Update**   | `d.update({"c": 3, "d": 4})`                 | Add/change multiple pairs      |
| **Delete**   | `d.pop("a")`                                  | Remove key, return value       |
| **Delete**   | `del d["a"]`                                  | Remove a specific key          |
| **Delete**   | `d.clear()`                                   | Empty the dictionary           |
| **Delete**   | `del d`                                       | Delete entire dictionary       |

---

*Python 101 — Ch 9.2 Dictionaries | Learn and Help Program | Metropolitan State University*
