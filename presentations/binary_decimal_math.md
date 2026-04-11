# Week 25: Binary Conversions & Binary Math Operations

---

## Part 1: Decimal to Binary and Binary to Decimal Conversions

---

### 1. What is Binary?

Computers only understand two digits: **0** and **1**. This is called the **binary number system** (base-2).

We humans use the **decimal number system** (base-10), which has ten digits: 0 through 9.

| Number System | Base   | Digits Used       | Example  |
|---------------|--------|-------------------|----------|
| Decimal       | Base-10 | 0, 1, 2, …, 9   | 42       |
| Binary        | Base-2  | 0, 1             | 101010   |

> 💡 **Tip:** Every number you see on a screen is stored as binary inside the computer!

---

### 2. Place Values in Binary

In decimal, each place is a power of 10:

```
Hundreds  Tens  Ones
 10²      10¹   10⁰
 100       10     1
```

In binary, each place is a power of 2:

```
128   64   32   16    8    4    2    1
 2⁷   2⁶   2⁵   2⁴   2³   2²   2¹   2⁰
```

---

### 3. Binary to Decimal Conversion

**Method:** Multiply each binary digit by its place value and add them up.

**Example 1: Convert `1011` to decimal**

```
1    0    1    1
2³   2²   2¹   2⁰
8    4    2    1

= (1 × 8) + (0 × 4) + (1 × 2) + (1 × 1)
= 8 + 0 + 2 + 1
= 11
```

**Example 2: Convert `11001` to decimal**

```
1     1     0     0     1
2⁴    2³    2²    2¹    2⁰
16    8     4     2     1

= (1 × 16) + (1 × 8) + (0 × 4) + (0 × 2) + (1 × 1)
= 16 + 8 + 0 + 0 + 1
= 25
```

**Example 3: Convert `10000000` to decimal**

```
1     0     0     0     0     0     0     0
2⁷    2⁶    2⁵    2⁴    2³    2²    2¹    2⁰
128   64    32    16    8     4     2     1

= 128
```

---

### 4. Decimal to Binary Conversion

**Method:** Repeatedly divide by 2 and record the remainders. Read the remainders from **bottom to top**.

**Example 1: Convert 13 to binary**

```
13 ÷ 2 = 6  remainder 1
 6 ÷ 2 = 3  remainder 0
 3 ÷ 2 = 1  remainder 1
 1 ÷ 2 = 0  remainder 1

Read bottom to top: 1101
```

✅ **Check:** 8 + 4 + 0 + 1 = 13 ✓

**Example 2: Convert 25 to binary**

```
25 ÷ 2 = 12  remainder 1
12 ÷ 2 = 6   remainder 0
 6 ÷ 2 = 3   remainder 0
 3 ÷ 2 = 1   remainder 1
 1 ÷ 2 = 0   remainder 1

Read bottom to top: 11001
```

✅ **Check:** 16 + 8 + 0 + 0 + 1 = 25 ✓

**Example 3: Convert 100 to binary**

```
100 ÷ 2 = 50  remainder 0
 50 ÷ 2 = 25  remainder 0
 25 ÷ 2 = 12  remainder 1
 12 ÷ 2 = 6   remainder 0
  6 ÷ 2 = 3   remainder 0
  3 ÷ 2 = 1   remainder 1
  1 ÷ 2 = 0   remainder 1

Read bottom to top: 1100100
```

✅ **Check:** 64 + 32 + 0 + 0 + 4 + 0 + 0 = 100 ✓

---

### 5. Python Built-in Functions for Conversion

```python
# Decimal to Binary
print(bin(13))       # 0b1101
print(bin(25))       # 0b11001

# Binary to Decimal
print(int("1101", 2))   # 13
print(int("11001", 2))  # 25
```

> 💡 **Tip:** The `0b` prefix in Python means "this is a binary number." You can also write binary literals directly: `x = 0b1101` sets x to 13.

---

### 6. Quick Reference Table

| Decimal | Binary   |
|---------|----------|
| 0       | 0        |
| 1       | 1        |
| 2       | 10       |
| 3       | 11       |
| 4       | 100      |
| 5       | 101      |
| 6       | 110      |
| 7       | 111      |
| 8       | 1000     |
| 9       | 1001     |
| 10      | 1010     |
| 15      | 1111     |
| 16      | 10000    |
| 32      | 100000   |
| 64      | 1000000  |
| 128     | 10000000 |
| 255     | 11111111 |

---

---

## Part 2: Binary Math — Bitwise Operations

---

### 7. What Are Bitwise Operations?

Bitwise operations work on individual **bits** (0s and 1s) of a number. Python provides these operators:

| Operator | Symbol | Description                        |
|----------|--------|------------------------------------|
| AND      | `&`    | 1 only if BOTH bits are 1          |
| OR       | `\|`   | 1 if EITHER bit is 1              |
| XOR      | `^`    | 1 if bits are DIFFERENT            |
| NOT      | `~`    | Flips all bits (inverts)           |
| Left Shift  | `<<` | Shifts bits to the left (× 2)   |
| Right Shift | `>>` | Shifts bits to the right (÷ 2)  |

---

### 8. AND (`&`)

Returns 1 only when **both** bits are 1.

**Truth Table:**

| A | B | A & B |
|---|---|-------|
| 0 | 0 |   0   |
| 0 | 1 |   0   |
| 1 | 0 |   0   |
| 1 | 1 |   1   |

**Example: 13 & 10**

```
  13 = 1 1 0 1
  10 = 1 0 1 0
       -------
  &  = 1 0 0 0  → 8
```

```python
print(13 & 10)   # 8
```

> 💡 **Real-world analogy:** AND is like two switches in a row — the light only turns on if BOTH switches are ON.

---

### 9. OR (`|`)

Returns 1 when **at least one** bit is 1.

**Truth Table:**

| A | B | A \| B |
|---|---|--------|
| 0 | 0 |   0    |
| 0 | 1 |   1    |
| 1 | 0 |   1    |
| 1 | 1 |   1    |

**Example: 13 | 10**

```
  13 = 1 1 0 1
  10 = 1 0 1 0
       -------
  |  = 1 1 1 1  → 15
```

```python
print(13 | 10)   # 15
```

> 💡 **Real-world analogy:** OR is like two switches side by side — the light turns on if EITHER switch is ON.

---

### 10. XOR (`^`)

Returns 1 when the bits are **different**.

**Truth Table:**

| A | B | A ^ B |
|---|---|-------|
| 0 | 0 |   0   |
| 0 | 1 |   1   |
| 1 | 0 |   1   |
| 1 | 1 |   0   |

**Example: 13 ^ 10**

```
  13 = 1 1 0 1
  10 = 1 0 1 0
       -------
  ^  = 0 1 1 1  → 7
```

```python
print(13 ^ 10)   # 7
```

> 💡 **Fun fact:** XOR is used in encryption! If you XOR a message with a key, you can XOR the result with the same key to get the original message back.

---

### 11. NOT (`~`)

Flips every bit. In Python, `~x` equals `-(x + 1)` because Python uses **two's complement** representation.

```python
print(~0)    # -1
print(~1)    # -2
print(~13)   # -14
print(~-5)   #  4
```

**How it works (simplified):**

```
~13:
  13 in binary =  0 0 0 0 1 1 0 1
  NOT          =  1 1 1 1 0 0 1 0  → -14 (two's complement)
```

> 💡 **Quick rule:** `~x` gives you `-(x + 1)`. So `~13 = -14` and `~0 = -1`.

---

### 12. Left Shift (`<<`)

Shifts all bits to the **left** by the specified number of positions. Zeros fill in on the right. Each left shift **multiplies by 2**.

**Example: 5 << 1**

```
  5 = 0 1 0 1
 <<1= 1 0 1 0  → 10
```

```python
print(5 << 1)    # 10   (5 × 2)
print(5 << 2)    # 20   (5 × 4)
print(5 << 3)    # 40   (5 × 8)
print(3 << 4)    # 48   (3 × 16)
```

> 💡 **Pattern:** `x << n` is the same as `x × 2ⁿ`

---

### 13. Right Shift (`>>`)

Shifts all bits to the **right** by the specified number of positions. Bits on the right are dropped. Each right shift **divides by 2** (integer division).

**Example: 20 >> 1**

```
 20 = 1 0 1 0 0
 >>1= 0 1 0 1 0  → 10
```

```python
print(20 >> 1)   # 10   (20 ÷ 2)
print(20 >> 2)   # 5    (20 ÷ 4)
print(20 >> 3)   # 2    (20 ÷ 8)
print(7 >> 1)    # 3    (7 ÷ 2, drops remainder)
```

> 💡 **Pattern:** `x >> n` is the same as `x ÷ 2ⁿ` (integer division, remainder dropped)

---

### 14. Summary of All Bitwise Operations (13 and 10)

```python
a = 13   # binary: 1101
b = 10   # binary: 1010

print(f"a & b  = {a & b}")    # 8   (AND)
print(f"a | b  = {a | b}")    # 15  (OR)
print(f"a ^ b  = {a ^ b}")    # 7   (XOR)
print(f"~a     = {~a}")       # -14 (NOT)
print(f"a << 2 = {a << 2}")   # 52  (Left Shift by 2)
print(f"a >> 2 = {a >> 2}")   # 3   (Right Shift by 2)
```

**Output:**

```
a & b  = 8
a | b  = 15
a ^ b  = 7
~a     = -14
a << 2 = 52
a >> 2 = 3
```

---

### 15. When Are Bitwise Operations Used?

| Use Case                    | Example                                      |
|-----------------------------|----------------------------------------------|
| Checking if a number is even/odd | `if n & 1 == 0:` means n is even       |
| Fast multiply/divide by 2   | `n << 1` doubles, `n >> 1` halves           |
| Permissions and flags        | File permissions use AND/OR with bit masks  |
| Encryption                  | XOR is used in simple ciphers                |
| Graphics and games          | Color values and pixel manipulation          |

---

### 16. Practice Problems

1. Convert 45 to binary (by hand, then check with `bin(45)`).
2. Convert `110110` to decimal (by hand, then check with `int("110110", 2)`).
3. What is `12 & 10`? Work it out bit by bit.
4. What is `12 | 10`? Work it out bit by bit.
5. What is `12 ^ 10`? Work it out bit by bit.
6. What is `~7`?
7. What is `6 << 3`? What decimal number is that?
8. What is `100 >> 2`? What decimal number is that?
9. Use Python to check: is 42 even or odd using `&`?
10. What is `0b1111 & 0b1010`? Convert the result to decimal.

---

> 📌 **Key Takeaway:** Binary is the language of computers. Understanding how to convert between decimal and binary — and how bitwise operations manipulate individual bits — gives you a deeper understanding of how programs work under the hood!
