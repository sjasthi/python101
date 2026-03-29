# Python Sets

## 1. Lists vs Tuples vs Sets — What's the Difference?

You already know **lists** and **tuples**. A **set** is a third type of collection in Python — and it has some unique properties!

| Feature              | Lists `[ ]`     | Tuples `( )`    | Sets `{ }`      |
|----------------------|-----------------|-----------------|-----------------|
| Ordered              | ✅              | ✅              | ❌              |
| Indexed              | ✅              | ✅              | ❌              |
| Add or Update items  | ✅              | ❌              | ✅ (add only)   |
| Can contain duplicates | ✅            | ✅              | ❌              |
| Mutable              | ✅              | ❌              | ✅              |
| Uses                 | Square Brackets `[ ]` | Round Brackets `( )` | Curly Braces `{ }` |
| Constructor          | `list()` or `[]` | `tuple()` or `()` | `set()`           |

> **Key takeaway:** Sets are **unordered**, **unindexed**, and **do not allow duplicate values**. Think of a set like a bag of unique items — you can toss things in and pull things out, but there's no particular order, and no item appears twice.

---

## 2. Creating a Set

### Using Curly Braces `{ }`

```python
fruits = {"apple", "banana", "cherry"}
print(fruits)       # {'cherry', 'banana', 'apple'}  — order may vary!
print(type(fruits)) # <class 'set'>
```

### Using the `set()` Constructor

```python
colors = set(["red", "green", "blue"])
print(colors)       # {'blue', 'red', 'green'}  — order may vary!
```

### Creating an Empty Set

```python
# ⚠️ Common Mistake!
wrong = {}            # This creates an EMPTY DICTIONARY, not a set!
print(type(wrong))    # <class 'dict'>

# ✅ Correct way to create an empty set:
correct = set()
print(type(correct))  # <class 'set'>
```

> ⚠️ **Watch out:** `{}` creates an empty **dictionary**, NOT an empty set. Always use `set()` for an empty set!

---

## 3. Sets Automatically Remove Duplicates

One of the most powerful features of sets — if you add duplicate values, Python keeps **only one copy**.

```python
numbers = {1, 2, 3, 2, 1, 4, 3, 5}
print(numbers)    # {1, 2, 3, 4, 5}  — duplicates are gone!
```

### Real-World Example — Unique Student Names

```python
sign_ups = ["abe", "barb", "chris", "abe", "dan", "chris", "ellie"]
unique_students = set(sign_ups)
print(unique_students)    # {'abe', 'barb', 'chris', 'dan', 'ellie'}
print(len(unique_students))  # 5 unique students
```

> 💡 **Pro tip:** Converting a list to a set is a quick way to remove duplicates!

---

## 4. Sets are Unordered and Unindexed

Unlike lists and tuples, sets have **no order** and **no index positions**. You cannot access elements by index.

```python
fruits = {"apple", "banana", "cherry"}

print(fruits[0])    # ❌ This will cause an error!
```

**Error:**
```
TypeError: 'set' object is not subscriptable
```

You also **cannot slice** a set:

```python
print(fruits[0:2])  # ❌ TypeError!
```

> **Key takeaway:** Since sets are unordered, there is no "first" or "last" item. Every time you print a set, the order may be different!

---

## 5. Sets Only Support Immutable Data Types

Sets can contain numbers, strings, booleans, and tuples — but **not lists**. Why? Because set items must be **immutable** (unchangeable).

### Why can't you put a list inside a set?

Let's think it through with a scenario:

```python
A = [1, 2, 3]
B = [2, 3, 4]
set_x = {A, B}    # ❌ TypeError: unhashable type: 'list'
```

**Why does Python block this?** Imagine if it *were* allowed:

```
set_x = {[1, 2, 3], [2, 3, 4]}    # Assume this works...

B.insert(0, 1)    # Insert 1 at the front of B
B.remove(4)        # Remove 4 from B
# Now B → [1, 2, 3]

# set_x → {[1, 2, 3], [1, 2, 3]}  — DUPLICATES! 💥
# This violates the set rule!
```

Since lists are **mutable** (you can change them), allowing them in a set could create duplicates — which breaks the whole point of a set.

### But tuples work just fine!

```python
A = (1, 2, 3)
B = (2, 3, 4)
set_x = {A, B}    # ✅ This works!
print(set_x)       # {(1, 2, 3), (2, 3, 4)}
```

Tuples are **immutable** — they can't be changed after creation — so there's no risk of accidental duplicates.

> **Key takeaway:** Only items that **cannot be changed** (immutable items) can be added to a set. This includes numbers, strings, booleans, and tuples — but **not lists**.

---

## 6. A Single Set Can Contain Multiple Data Types

A set doesn't have to contain all the same type. You can mix strings, numbers, and booleans in one set:

```python
# student name, age, email, and is_student_active?
student_info = {"John Doe", 15, "john.doe@gmail.com", True}
print(student_info)
# {'John Doe', 'john.doe@gmail.com', True, 15}  — order may vary!
```

> ⚠️ **Remember:** The order is **not guaranteed** in sets. Even though you typed the name first, Python may print the items in a completely different order!

---

## 7. CRUD Operations on Sets

Remember the CRUD framework from tuples? Let's see how sets compare:

| Operation   | Lists | Tuples | Sets  |
|-------------|-------|--------|-------|
| **C**reate  | ✅    | ✅     | ✅    |
| **R**ead    | ✅    | ✅     | ✅ (but no indexing!) |
| **U**pdate  | ✅    | ❌     | ✅ (add/remove, but can't change an item) |
| **D**elete  | ✅    | ❌     | ✅    |

> **Key takeaway:** Sets are mutable — you **can** add and remove items. But you **cannot** change an existing item (since there's no index to target). You can only add new items or remove existing ones.

---

## 8. Adding Items to a Set

### `add()` — Add a Single Item

```python
fruits = {"apple", "banana", "cherry"}
fruits.add("dragonfruit")
print(fruits)    # {'apple', 'banana', 'cherry', 'dragonfruit'}
```

Adding a duplicate does nothing (no error, just ignored):

```python
fruits.add("apple")
print(fruits)    # {'apple', 'banana', 'cherry', 'dragonfruit'}  — no change!
```

### `update()` — Add Multiple Items

You can add items from another set, list, tuple, or any iterable:

```python
fruits = {"apple", "banana", "cherry"}
tropical = ["mango", "pineapple", "banana"]

fruits.update(tropical)
print(fruits)    # {'apple', 'banana', 'cherry', 'mango', 'pineapple'}
# "banana" was already there — not duplicated!
```

---

## 9. Removing Items from a Set

Python gives you several ways to remove items:

### `remove()` — Remove a Specific Item (raises error if not found)

```python
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits)    # {'apple', 'cherry'}

fruits.remove("grape")   # ❌ KeyError: 'grape'
```

### `discard()` — Remove a Specific Item (NO error if not found)

```python
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
print(fruits)    # {'apple', 'cherry'}

fruits.discard("grape")  # ✅ No error — just does nothing
```

> 💡 **Tip:** Use `discard()` when you're not sure if the item exists. Use `remove()` when you **expect** the item to be there and want Python to alert you if it's missing.

### `pop()` — Remove a Random Item

```python
fruits = {"apple", "banana", "cherry"}
removed = fruits.pop()
print(removed)   # Could be any item — sets are unordered!
print(fruits)    # The remaining items
```

### `clear()` — Remove All Items

```python
fruits = {"apple", "banana", "cherry"}
fruits.clear()
print(fruits)    # set()  — empty set
```

### `del` — Delete the Entire Set

```python
fruits = {"apple", "banana", "cherry"}
del fruits
print(fruits)    # ❌ NameError: name 'fruits' is not defined
```

---

## 10. Looping Through a Set

Even though you can't use indexing, you **can** iterate through a set with a `for` loop:

```python
fruits = {"apple", "banana", "cherry"}
for fruit in fruits:
    print(fruit)
# Output order may vary each time!
```

### Membership Operators (`in` / `not in`)

Just like lists and tuples:

```python
fruits = {"apple", "banana", "cherry"}
print("banana" in fruits)       # True
print("grape" not in fruits)    # True
```

> 💡 **Fun fact:** Checking membership with `in` is **much faster** on a set than on a list. This is one of the reasons programmers use sets!

---

## 11. Built-in Functions Work on Sets

| Function       | Example                        | Result |
|----------------|--------------------------------|--------|
| `len()`        | `len({"a", "b", "c"})`        | `3`    |
| `min()`        | `min({3, 1, 4, 1, 5})`        | `1`    |
| `max()`        | `max({3, 1, 4, 1, 5})`        | `5`    |
| `sum()`        | `sum({3, 1, 4, 1, 5})`        | `13` (duplicates removed first → `{1, 3, 4, 5}`) |
| `sorted()`     | `sorted({3, 1, 4, 5})`        | `[1, 3, 4, 5]` (returns a **list**) |

---

## 12. Set Operations — The Superpower of Sets! 🦸

This is where sets truly shine. Sets support powerful **mathematical operations** that make them perfect for comparing groups of data.

### Real-World Scenario — Mammals vs Aquatic Animals

```python
mammals = {"Tiger", "Camel", "Sheep", "Whale", "Walrus"}
aquatic = {"Octopus", "Squid", "Crab", "Whale", "Walrus"}
```

Notice that **Whale** and **Walrus** appear in both sets — they are mammals that live in water!

### Union (`|` or `.union()`) — All animals from EITHER group

The **union** of two sets A and B is the set containing the elements that are in A, B, or both (A ∪ B).

```python
animals = mammals.union(aquatic)
print(animals)
# {'Octopus', 'Tiger', 'Sheep', 'Walrus', 'Whale', 'Crab', 'Camel', 'Squid'}

# Same thing using the | operator:
animals = mammals | aquatic

# The original sets are NOT modified:
print(mammals)   # {'Tiger', 'Sheep', 'Walrus', 'Whale', 'Camel'}
print(aquatic)   # {'Octopus', 'Walrus', 'Crab', 'Whale', 'Squid'}
```

### Intersection (`&` or `.intersection()`) — Animals in BOTH groups

The **intersection** of two sets A and B is the set containing the elements that are common to both sets (A ∩ B).

```python
both = mammals.intersection(aquatic)
print(both)
# {'Walrus', 'Whale'}

# Same thing using the & operator:
both = mammals & aquatic
```

### Difference (`-` or `.difference()`) — In one group but NOT the other

The **difference** of two sets A and B is the set of all elements in A that are not in B (A - B).

```python
mammals_only = mammals.difference(aquatic)
print(mammals_only)
# {'Sheep', 'Tiger', 'Camel'}

# Same thing using the - operator:
mammals_only = mammals - aquatic

aquatic_only = aquatic.difference(mammals)
print(aquatic_only)
# {'Octopus', 'Squid', 'Crab'}
```

> ⚠️ **Note:** `A - B` is **not** the same as `B - A`! The order matters with difference.

### Symmetric Difference (`^` or `.symmetric_difference()`) — In one group but NOT both

The **symmetric difference** of two sets A and B is the set of elements that are in either A or B, but not in both (A △ B).

```python
exclusive = mammals.symmetric_difference(aquatic)
print(exclusive)
# {'Sheep', 'Octopus', 'Crab', 'Camel', 'Tiger', 'Squid'}

# Same thing using the ^ operator:
exclusive = mammals ^ aquatic
```

### Visual Summary of Set Operations

```
mammals = {Tiger, Camel, Sheep, Whale, Walrus}
aquatic = {Octopus, Squid, Crab, Whale, Walrus}

Union (|)                → {Tiger, Camel, Sheep, Whale, Walrus, Octopus, Squid, Crab}  — ALL
Intersection (&)         → {Whale, Walrus}                                              — BOTH
Difference (-)           → {Tiger, Camel, Sheep}                — mammals only
Symmetric Difference (^) → {Tiger, Camel, Sheep, Octopus, Squid, Crab}  — ONE group only
```

---

## 13. Subset and Superset

### `issubset()` — Is every item in set A also in set B?

```python
a = {1, 2, 3}
b = {1, 2, 3, 4, 5}

print(a.issubset(b))     # True  — all items in a are in b
print(b.issubset(a))     # False — 4 and 5 are NOT in a
```

### `issuperset()` — Does set A contain every item in set B?

```python
print(b.issuperset(a))   # True  — b contains everything in a
print(a.issuperset(b))   # False
```

### `isdisjoint()` — Do the two sets have NO items in common?

```python
x = {1, 2, 3}
y = {4, 5, 6}
z = {3, 4, 5}

print(x.isdisjoint(y))   # True  — no common items
print(x.isdisjoint(z))   # False — 3 is in both
```

---

## 14. Set Methods — Quick Reference

| Method                  | Description                                                    |
|-------------------------|----------------------------------------------------------------|
| `add(x)`                | Adds item `x` to the set                                      |
| `update(iterable)`      | Adds multiple items from a list, tuple, or set                 |
| `remove(x)`             | Removes item `x` (raises `KeyError` if not found)             |
| `discard(x)`            | Removes item `x` (does nothing if not found)                  |
| `pop()`                 | Removes and returns a random item                              |
| `clear()`               | Removes all items from the set                                 |
| `copy()`                | Returns a copy of the set                                      |
| `union(set2)`           | Returns all items from both sets                               |
| `intersection(set2)`    | Returns items that exist in both sets                          |
| `intersection_update(set2)` | Removes items not present in `set2` (modifies in place)   |
| `difference(set2)`      | Returns items in this set but not in `set2`                    |
| `difference_update(set2)` | Removes items found in `set2` (modifies in place)            |
| `symmetric_difference(set2)` | Returns items in either set, but not both                |
| `symmetric_difference_update(set2)` | Keeps only items in either set, not both (modifies in place) |
| `issubset(set2)`        | Returns `True` if all items exist in `set2`                    |
| `issuperset(set2)`      | Returns `True` if this set contains all items of `set2`        |
| `isdisjoint(set2)`      | Returns `True` if no items in common                           |

Reference: [https://www.w3schools.com/python/python_ref_set.asp](https://www.w3schools.com/python/python_ref_set.asp)

---

## 15. When to Use Sets?

Sets are the perfect choice when:

- **You need unique values** — Student IDs, email addresses, usernames
- **You need to remove duplicates** — Convert a list to a set and back
- **You need to compare groups** — Who is in both clubs? What items are missing?
- **You need fast membership checks** — `in` is much faster with sets than lists

### Real-World Examples

| Use Case                          | Why a Set?                                    |
|-----------------------------------|-----------------------------------------------|
| Unique visitors to a website      | No duplicates — each visitor counted once     |
| Ingredients you already have      | Quick check: "Do I have eggs?"                |
| Students who submitted homework   | Compare against class roster to find missing  |
| Countries you've visited          | Each country listed only once                 |

---

## Summary

| Concept                     | What to Remember                                              |
|-----------------------------|---------------------------------------------------------------|
| **Syntax**                  | Curly braces `{ }` or `set()` constructor                     |
| **Empty set**               | Use `set()`, NOT `{}` (that's a dictionary!)                  |
| **Ordered?**                | ❌ No — items have no fixed position                          |
| **Indexed?**                | ❌ No — you cannot use `[0]`, `[1]`, etc.                     |
| **Duplicates?**             | ❌ No — each item appears only once                           |
| **Mutable?**                | ✅ Yes — you can add and remove items                         |
| **Add items**               | `add()` for one, `update()` for many                          |
| **Remove items**            | `remove()`, `discard()`, `pop()`, `clear()`                   |
| **Set operations**          | `union`, `intersection`, `difference`, `symmetric_difference` |
| **Operators**               | `|` (union), `&` (intersection), `-` (difference), `^` (sym diff) |
| **Fast membership checks**  | `in` / `not in` — faster than lists!                          |

---

*Python 101 | Learn and Help Program | Metropolitan State University*
