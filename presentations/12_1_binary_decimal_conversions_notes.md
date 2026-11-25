# Week 25: Binary and Decimal Conversions

---

## What is Binary?

Computers only understand two digits: **0** and **1**. This is called the **binary number system** (base-2).

We humans use the **decimal number system** (base-10), which has ten digits: 0 through 9. People have 10 fingers — that's why base-10 feels natural to us. Computers, on the other hand, have only two "fingers": 0 and 1.

| Number System | Base   | Digits Used       | Example  |
|---------------|--------|-------------------|----------|
| Decimal       | Base-10 | 0, 1, 2, …, 9   | 42       |
| Binary        | Base-2  | 0, 1             | 101010   |

> 💡 **Tip:** Every number you see on a screen is stored as binary inside the computer!

---

## Binary Counting: How It Works

In decimal, we count 0, 1, 2, … 9, then carry over to 10. In binary, we only have 0 and 1, so we carry over much sooner:

| Decimal | Binary |
|---------|--------|
| 0       | 0      |
| 1       | 1      |
| 2       | 10     |
| 3       | 11     |
| 4       | 100    |
| 5       | 101    |
| 6       | 110    |
| 7       | 111    |
| 8       | 1000   |
| 9       | 1001   |
| 10      | 1010   |
| 11      | 1011   |
| 12      | 1100   |
| 13      | 1101   |
| 14      | 1110   |
| 15      | 1111   |
| 16      | 10000  |
| 17      | 10001  |
| 18      | 10010  |
| 19      | 10011  |

---

## Place Values in Binary

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

Each position in a binary number represents a power of 2, just like each position in a decimal number represents a power of 10.

---

## Binary to Decimal Conversion

**Method:** Multiply each binary digit by its place value and add them up.

### Example 1: Convert `11111111` to decimal

```
1     1     1     1     1     1     1     1
2⁷    2⁶    2⁵    2⁴    2³    2²    2¹    2⁰
128   64    32    16    8     4     2     1

= 128 + 64 + 32 + 16 + 8 + 4 + 2 + 1
= 255
```

### Example 2: Convert `10010101` to decimal

```
1     0     0     1     0     1     0     1
2⁷    2⁶    2⁵    2⁴    2³    2²    2¹    2⁰
128   64    32    16    8     4     2     1

= 128 + 0 + 0 + 16 + 0 + 4 + 0 + 1
= 149
```

### Example 3: Convert `1011` to decimal

```
1    0    1    1
2³   2²   2¹   2⁰
8    4    2    1

= (1 × 8) + (0 × 4) + (1 × 2) + (1 × 1)
= 8 + 0 + 2 + 1
= 11
```

### Example 4: Convert `11001` to decimal

```
1     1     0     0     1
2⁴    2³    2²    2¹    2⁰
16    8     4     2     1

= (1 × 16) + (1 × 8) + (0 × 4) + (0 × 2) + (1 × 1)
= 16 + 8 + 0 + 0 + 1
= 25
```

### Worked Example with All Steps: Convert `101010` to decimal

```
1     0     1     0     1     0
2⁵    2⁴    2³    2²    2¹    2⁰
32    16    8     4     2     1

→ 2⁰ × 0 = 1 × 0 = 0
→ 2¹ × 1 = 2 × 1 = 2
→ 2² × 0 = 4 × 0 = 0
→ 2³ × 1 = 8 × 1 = 8
→ 2⁴ × 0 = 16 × 0 = 0
→ 2⁵ × 1 = 32 × 1 = 32

Resultant decimal number = 0 + 2 + 0 + 8 + 0 + 32 = 42
```

---

## Decimal to Binary Conversion (Successive Division Method)

**Method:** Repeatedly divide by 2 and record the remainders. Read the remainders from **bottom to top**.

### Example 1: Convert 13 to binary

```
13 ÷ 2 = 6  remainder 1   ← LSB (Least Significant Bit)
 6 ÷ 2 = 3  remainder 0
 3 ÷ 2 = 1  remainder 1
 1 ÷ 2 = 0  remainder 1   ← MSB (Most Significant Bit)

Read bottom to top: 1101
```

✅ **Check:** 8 + 4 + 0 + 1 = 13 ✓

### Example 2: Convert 25 to binary

```
25 ÷ 2 = 12  remainder 1
12 ÷ 2 = 6   remainder 0
 6 ÷ 2 = 3   remainder 0
 3 ÷ 2 = 1   remainder 1
 1 ÷ 2 = 0   remainder 1

Read bottom to top: 11001
```

✅ **Check:** 16 + 8 + 0 + 0 + 1 = 25 ✓

### Example 3: Convert 75 to binary

```
75 ÷ 2 = 37  remainder 1   ← LSB
37 ÷ 2 = 18  remainder 1
18 ÷ 2 = 9   remainder 0
 9 ÷ 2 = 4   remainder 1
 4 ÷ 2 = 2   remainder 0
 2 ÷ 2 = 1   remainder 0
 1 ÷ 2 = 0   remainder 1   ← MSB

Read bottom to top: 1001011
```

✅ **Check:** 64 + 0 + 0 + 8 + 0 + 2 + 1 = 75 ✓

### Example 4: Convert 156 to binary

```
156 ÷ 2 = 78  remainder 0
 78 ÷ 2 = 39  remainder 0
 39 ÷ 2 = 19  remainder 1
 19 ÷ 2 = 9   remainder 1
  9 ÷ 2 = 4   remainder 1
  4 ÷ 2 = 2   remainder 0
  2 ÷ 2 = 1   remainder 0
  1 ÷ 2 = 0   remainder 1

Read bottom to top: 10011100
```

✅ **Check:** 128 + 0 + 0 + 16 + 8 + 4 + 0 + 0 = 156 ✓

### Example 5: Convert 100 to binary

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

## Python Built-in Functions for Conversion

### Decimal to Binary: `bin()`

```python
# bin() converts a decimal integer to a binary string
print(bin(13))       # 0b1101
print(bin(25))       # 0b11001
print(bin(75))       # 0b1001011
print(bin(156))      # 0b10011100
```

### Binary to Decimal: `int()` with base 2

```python
# int(string, 2) converts a binary string to a decimal integer
print(int("1101", 2))     # 13
print(int("11001", 2))    # 25
print(int("1001011", 2))  # 75
print(int("10011100", 2)) # 156
```

### Working with Binary Literals and Types

```python
# Binary string literal (with 0b prefix) — stored as a string
d = '0b1001'
print(d, type(d))         # 0b1001 <class 'str'>

# Binary literal WITHOUT quotes — stored as an int
f = 0b1001
print(f, type(f))         # 9 <class 'int'>

# Binary string without 0b prefix — also a string
g = '1001'
print(g, type(g))         # 1001 <class 'str'>

# Convert binary string to decimal int (must provide base 2)
e = int(d, 2)
print(e, type(e))         # 9 <class 'int'>

h = int(g, 2)
print(h, type(h))         # 9 <class 'int'>
```

> 💡 **Tip:** The `0b` prefix in Python means "this is a binary number." When converting binary strings to decimal using `int()`, always pass `2` as the second argument to specify the base.

---

## Quick Reference Table

| Decimal | Binary    |
|---------|-----------|
| 0       | 0         |
| 1       | 1         |
| 2       | 10        |
| 3       | 11        |
| 4       | 100       |
| 5       | 101       |
| 6       | 110       |
| 7       | 111       |
| 8       | 1000      |
| 9       | 1001      |
| 10      | 1010      |
| 15      | 1111      |
| 16      | 10000     |
| 32      | 100000    |
| 64      | 1000000   |
| 128     | 10000000  |
| 255     | 11111111  |

---

## Practice Exercises

### Exercise A: Convert Decimals to Binary

Use the successive division method by hand, then verify with `bin()` in Python.

| Decimal | Binary (your answer) |
|---------|---------------------|
| 10      |                     |
| 12      |                     |
| 15      |                     |
| 22      |                     |
| 26      |                     |
| 94      |                     |
| 98      |                     |
| 128     |                     |
| 256     |                     |
| 640     |                     |
| 763     |                     |

📎 *See slide 18 in the presentation for this exercise and the worked example for decimal 94.*

### Exercise B: Convert Binary to Decimal

Use the place value method by hand, then verify with `int(binary_str, 2)` in Python.

| Binary  | Decimal (your answer) |
|---------|-----------------------|
| 101110  |                       |
| 100101  |                       |
| 111101  |                       |
| 101000  |                       |
| 111111  |                       |
| 111100  |                       |
| 110100  |                       |
| 101011  |                       |
| 100001  |                       |
| 110011  |                       |

📎 *See slide 19 in the presentation for this exercise.*

---

## Some Binary Fun on Your Fingers!

You can count in binary on your fingers! Each finger represents a power of 2:

- Thumb = 1 (2⁰)
- Index = 2 (2¹)
- Middle = 4 (2²)
- Ring = 8 (2³)
- Pinky = 16 (2⁴)

With just one hand, you can count from 0 to 31. With two hands, you can count all the way to 1023!

Examples:
- Fist (no fingers up) = **0**
- Thumb only = **1**
- Index only = **2**
- Middle finger only = **4**
- Index + middle + ring = **14** (2 + 4 + 8)
- All five fingers = **31** (1 + 2 + 4 + 8 + 16)

📎 * More info: [Finger Binary on Wikipedia](https://en.wikipedia.org/wiki/Finger_binary)*

---

> 📌 **Key Takeaway:** Binary is the language of computers. Understanding how to convert between decimal and binary gives you a deeper understanding of how programs and data work under the hood!

> 📝 **Coming Next:** Binary Math — Bitwise Operations (AND, OR, XOR, NOT, Shifts) will be covered in a separate topic.
