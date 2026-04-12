# Python 101 — Lab 25: Decimal & Binary Conversions

---

| | |
|---|---|
| **Course** | Python 101 |
| **Lab** | Lab 25 — Decimal & Binary Conversions |
| **Total Points** | 10 |
| **Student Name** | _________________________ |
| **Date** | _________________________ |

---

### Instructions

- Complete **all 5 problems** below on a piece of paper.
- **Show your work** for every problem — answers without work will not receive full credit.
- Submit a **digital image** of your handwritten work to Google Classroom (PDF, photo, or Google Slides).

---

## Problem 1 (2 points) — Binary to Decimal

Convert the following **binary** numbers to **decimal**. Use the **place value method** (multiply each bit by its power of 2 and add them up). Show all your steps.

| # | Binary | Decimal (show your work) |
|---|--------|--------------------------|
| a | 1101 | |
| b | 101011 | |
| c | 10011100 | |
| d | 11010110 | |

**Example (how to show your work):**

```
Binary: 1011

1    0    1    1
2³   2²   2¹   2⁰
8    4    2    1

= (1×8) + (0×4) + (1×2) + (1×1)
= 8 + 0 + 2 + 1
= 11
```

---

## Problem 2 (2 points) — Binary to Decimal (8-bit)

Each of the following is an **8-bit binary number**. Convert each to decimal. Show your work.

| # | Binary | Decimal (show your work) |
|---|--------|--------------------------|
| a | 00101110 | |
| b | 10101010 | |
| c | 01111100 | |
| d | 11100001 | |

**Hint:** The 8-bit place values are:

```
128   64   32   16    8    4    2    1
 2⁷   2⁶   2⁵   2⁴   2³   2²   2¹   2⁰
```

---

## Problem 3 (2 points) — Decimal to Binary

Convert the following **decimal** numbers to **binary**. Use the **successive division method** (divide by 2 repeatedly and read the remainders bottom to top). Show all your division steps.

| # | Decimal | Binary (show your work) |
|---|---------|-------------------------|
| a | 23 | |
| b | 94 | |
| c | 145 | |
| d | 200 | |

**Example (how to show your work):**

```
Decimal: 13

13 ÷ 2 = 6   remainder 1  ← LSB
 6 ÷ 2 = 3   remainder 0
 3 ÷ 2 = 1   remainder 1
 1 ÷ 2 = 0   remainder 1  ← MSB

Read bottom to top → 1101
```

---

## Problem 4 (2 points) — Decimal to Binary with Verification

Convert the following **decimal** numbers to **binary** using the successive division method. Then **verify your answer** by converting your binary result back to decimal using the place value method.

| # | Decimal | Binary (show division work) | Verification (show place value work) |
|---|---------|-----------------------------|--------------------------------------|
| a | 37 | | |
| b | 156 | | |

**Example (how to show your work):**

```
CONVERT: Decimal 11 → Binary

11 ÷ 2 = 5   remainder 1
 5 ÷ 2 = 2   remainder 1
 2 ÷ 2 = 1   remainder 0
 1 ÷ 2 = 0   remainder 1

Read bottom to top → 1011

VERIFY: Binary 1011 → Decimal

1    0    1    1
2³   2²   2¹   2⁰
= 8 + 0 + 2 + 1 = 11  ✓
```

---

## Problem 5 (2 points) — Finger Binary

You can count in binary using your fingers! Each finger on one hand represents a power of 2:

| Finger | Thumb | Index | Middle | Ring | Pinky |
|--------|-------|-------|--------|------|-------|
| Value  | 1 (2⁰) | 2 (2¹) | 4 (2²) | 8 (2³) | 16 (2⁴) |

A raised finger = 1, a closed finger = 0. With one hand you can count from 0 to 31.

### Part A — Draw or describe which fingers are UP for each number:

| # | Decimal Number | Which fingers are up? | How? (show the addition) |
|---|----------------|----------------------|--------------------------|
| a | 6 | | |
| b | 19 | | |
| c | 25 | | |
| d | 31 | | |

**Example:**

```
Decimal: 10

Pinky=0  Ring=1  Middle=0  Index=1  Thumb=0
  16      8       4        2        1

Ring (8) + Index (2) = 10  ✓
```

### Part B — What decimal number do these finger positions represent?

| # | Fingers Up | Decimal Number | How? (show the addition) |
|---|-----------|----------------|--------------------------|
| e | Thumb + Middle | | |
| f | Pinky + Ring + Thumb | | |

---

## Submission

1. Complete all 5 problems **on paper**, showing your work.
2. Take a **photo or scan** of your work.
3. Submit to **Google Classroom** as a PDF, image(s), or Google Slides.

---

### Points Summary

| Problem | Topic | Points |
|---------|-------|--------|
| 1 | Binary to Decimal (place value method) | 2 |
| 2 | Binary to Decimal (8-bit numbers) | 2 |
| 3 | Decimal to Binary (successive division) | 2 |
| 4 | Decimal to Binary with Verification | 2 |
| 5 | Finger Binary | 2 |
| **Total** | | **10** |

---

*Python 101 — Siva R Jasthi — Metropolitan State University*
