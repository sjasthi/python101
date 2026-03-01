# Python Tuples 

## 1. Lists vs Tuples — What's the Difference?


| Feature              | Lists           | Tuples          |
|----------------------|-----------------|-----------------|
| Ordered              | ✅              | ✅              |
| Indexed              | ✅              | ✅              |
| Add or Update items  | ✅              | ❌              |
| Can contain duplicates | ✅            | ✅              |
| Uses                 | Square Brackets `[ ]` | Round Brackets `( )` |

> **Key takeaway:** Tuples are like lists, but you **cannot** add or update items once they are created.

---

---

## 2. When Should You Use Tuples?

![When to Use Tuples](images_tuples/when_to_use_tuples.png)

Use tuples when your data should **not change**. Great examples include:

- **Days of the week** — there are always 7 days and they never change
- **Elements of the Periodic Table** — fixed set of elements
- **Coordinates** (latitude, longitude)
- **RGB colour values**

```python
days_of_week = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")

periodic_elements = ("Hydrogen", "Helium", "Lithium", "Beryllium", ...)
```

Since these values are constant and fixed, tuples are the perfect data structure to use!

## 3. CRUD Operations on Tuples

![CRUD of Tuples](images_tuples/crud_of_tuples.png)

Tuples only support **Create** and **Read** operations:

- **C – Create** (with an initial list)
- **R – Read** (Query, Traversal, Find, Search)
- ~~**U – Update**~~ (Modify, Change, Edit) — ❌ Not allowed
- ~~**D – Delete**~~ (Remove, Empty) — ❌ You **can** delete the entire tuple, but you **cannot** delete individual items inside a tuple

---

## 4. Tuples are Immutable (Unchangeable)

![Cannot Update Tuple](images_tuples/cannot_update.png)

Tuples are **immutable**, meaning their values **cannot be changed** after creation.

### Example — Trying to change a value:

```python
tuple = ("one", "three")
tuple[1] = "two"   # ❌ This will cause an error!
```

**Error:**
```
TypeError: 'tuple' object does not support item assignment
```

For example, given a students tuple:

```python
students = ("abe", "barb", "chris", "abe", "dan", "chris", "ellie")
#  index:     0       1        2       3      4       5        6
```

If you try to change the 4th student from `"abe"` to `"anna"`:

```python
students[3] = "anna"   # ❌ This will NOT work!
```

This will throw a `TypeError` because tuples do not support item assignment.

---

### Example: You Can't Append to a Tuple

![Cannot Append](images_tuples/cannot_append.png)

```python
list = [10, 20, 30]
list.append(40)       # ✅ Works fine for lists

tuple = (10, 20, 30)
tuple.append(40)      # ❌ ERROR!
```

**Error:**
```
AttributeError: 'tuple' object has no attribute 'append'
```

The list grows to `[10, 20, 30, 40]`, but the tuple stays as `(10, 20, 30)` and throws an error when you try to append.

---

## 5. Tuple Methods — Only Two Are Valid

Because tuples are immutable, most list methods are **not available** for tuples. Only **two methods** are valid:

| Method      | Purpose                                          |
|-------------|--------------------------------------------------|
| `index(x)`  | Returns the index of the **first** occurrence of item `x` |
| `count(x)`  | Counts the number of times `x` appears in the tuple |

The following list methods are **crossed out** because they do **NOT** work on tuples:

| ~~Method~~         | ~~Purpose~~                                                   |
|--------------------|---------------------------------------------------------------|
| ~~`append(x)`~~    | ~~Add x to the end of the list~~                              |
| ~~`extend(list_x)`~~ | ~~Add all items from list_x at the end~~                   |
| ~~`insert(i, x)`~~ | ~~Inserts an item at a given position~~                       |
| ~~`remove(x)`~~    | ~~Removes the first item x~~                                  |
| ~~`pop()`~~        | ~~Removes the last item and returns it~~                      |
| ~~`pop([i])`~~     | ~~Removes the first item~~                                    |
| ~~`clear()`~~      | ~~Removes all elements in the list~~                          |
| ~~`sort()`~~       | ~~Sorts elements in ascending order~~                         |
| ~~`reverse()`~~    | ~~Reverses the list~~                                         |
| ~~`copy()`~~       | ~~Returns a copy of the list~~                                |

> 📖 Reference: [W3Schools — Python Tuple Methods](https://www.w3schools.com/python/python_ref_tuple.asp)


---

## Summary

| | Lists | Tuples |
|---|---|---|
| **Syntax** | `[1, 2, 3]` | `(1, 2, 3)` |
| **Mutable?** | ✅ Yes | ❌ No (immutable) |
| **Methods available** | Many | Only `index()` and `count()` |
| **Best used for** | Data that changes | Data that stays constant |
