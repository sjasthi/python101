# 🔢 Python 101 — Lab 26: Binary Math (Bitwise Operations)

**Week 26 | Chapter 10 | Total: 10 points**

---

| | |
|---|---|
| **Name:** | __________________________________________ |
| **Date:** | __________________________________________ |
| **Score:** | ___________ / 10 |

---

## 📌 Quick Reference — Bitwise Operators

| Operator | Symbol | Rule | Pattern |
|----------|--------|------|---------|
| AND | `&` | 1 only if **BOTH** bits are 1 | |
| OR | `\|` | 1 if **EITHER** bit is 1 | |
| XOR | `^` | 1 if the bits are **DIFFERENT** | |
| NOT | `~` | **Flips** all bits | `~x` = `-(x + 1)` |
| Left Shift | `<<` | Shifts bits left; fills 0s on right | `x << n` = `x × 2ⁿ` |
| Right Shift | `>>` | Shifts bits right; drops bits on right | `x >> n` = `x ÷ 2ⁿ` |

---

## Section 1 — AND (`&`) &nbsp;&nbsp; *(2 points)*

> 💡 AND returns 1 only when **both** bits are 1. Think: both switches must be ON.

---

**Question 1a** &nbsp;*(1 point)*

Compute `14 & 11` by filling in the bit-by-bit table below.

```
  14  in binary  →   1  1  1  0
  11  in binary  →   1  0  1  1
                      -  -  -  -
  &  result      →   _  _  _  _
```

**Answer (decimal):** &nbsp; `14 & 11` = ___________

---

**Question 1b** &nbsp;*(1 point)*

A game uses a binary **access flag** `1111` (decimal 15) to represent a player who has unlocked all four abilities.
A mask `0110` (decimal 6) is used to check abilities 2 and 3 only.

What is `15 & 6`? Show your bit-by-bit work:

```
  15  in binary  →   1  1  1  1
   6  in binary  →   0  1  1  0
                      -  -  -  -
  &  result      →   _  _  _  _
```

**Answer (decimal):** &nbsp; `15 & 6` = ___________

**What does the result tell you?** (Circle one)

&nbsp;&nbsp;&nbsp;&nbsp; A) Both abilities 2 and 3 are unlocked &nbsp;&nbsp;&nbsp;&nbsp; B) Neither ability is unlocked &nbsp;&nbsp;&nbsp;&nbsp; C) Only ability 2 is unlocked

---

## Section 2 — OR (`|`) &nbsp;&nbsp; *(2 points)*

> 💡 OR returns 1 if **at least one** bit is 1. Think: either switch can turn the light on.

---

**Question 2a** &nbsp;*(1 point)*

Compute `5 | 12` by filling in the bit-by-bit table below.

```
   5  in binary  →   0  1  0  1
  12  in binary  →   1  1  0  0
                      -  -  -  -
  |  result      →   _  _  _  _
```

**Answer (decimal):** &nbsp; `5 | 12` = ___________

---

**Question 2b** &nbsp;*(1 point)*

Two robots are sending signals. Robot A sends `0011` (decimal 3) and Robot B sends `1010` (decimal 10).
Mission control uses OR to combine both signals into one.

What is `3 | 10`? Show your bit-by-bit work:

```
   3  in binary  →   0  0  1  1
  10  in binary  →   1  0  1  0
                      -  -  -  -
  |  result      →   _  _  _  _
```

**Answer (decimal):** &nbsp; `3 | 10` = ___________

---

## Section 3 — XOR (`^`) &nbsp;&nbsp; *(2 points)*

> 💡 XOR returns 1 when the two bits are **different**. Same bits → 0. Different bits → 1.

---

**Question 3a** &nbsp;*(1 point)*

Compute `11 ^ 7` by filling in the bit-by-bit table below.

```
  11  in binary  →   1  0  1  1
   7  in binary  →   0  1  1  1
                      -  -  -  -
  ^  result      →   _  _  _  _
```

**Answer (decimal):** &nbsp; `11 ^ 7` = ___________

---

**Question 3b** &nbsp;*(1 point)*

XOR has a special property: if you XOR a number with itself, you always get 0.
If you XOR a number with 0, you get the number back unchanged.

Fill in the blanks **without** doing bit-by-bit work — use the rules above:

```
  9 ^ 9  = ___________    (hint: same number)

  9 ^ 0  = ___________    (hint: XOR with zero)
```

---

## Section 4 — NOT (`~`) &nbsp;&nbsp; *(1 point)*

> 💡 NOT flips every bit. In Python: `~x` always equals `-(x + 1)`.

---

**Question 4** &nbsp;*(1 point — 0.5 pt each)*

Use the rule `~x = -(x + 1)` to find each result. No bit-by-bit work needed — just apply the formula!

```
  ~5   = ___________

  ~0   = ___________

  ~(-3) = ___________     (bonus — think carefully!)
```

> *(The third blank is a bonus — it will not reduce your score if skipped.)*

---

## Section 5 — Left Shift (`<<`) &nbsp;&nbsp; *(1.5 points)*

> 💡 Left shift moves bits to the left and fills 0s on the right.
> Each left shift by 1 **doubles** the number.
> Pattern: `x << n` = `x × 2ⁿ`

---

**Question 5a** &nbsp;*(0.5 points)*

Compute `3 << 2` using the bit diagram below:

```
   3  in binary  →   0  0  1  1
   << 2 (shift)  →   _  _  _  _  0  0    (two 0s added on the right)
```

**Answer (decimal):** &nbsp; `3 << 2` = ___________

Verify using the pattern: &nbsp; `3 × 2²` = `3 × ___` = ___________

---

**Question 5b** &nbsp;*(0.5 points)*

Without drawing bits, use the pattern `x << n = x × 2ⁿ` to fill in the blanks:

```
  7 << 1  =  7 ×  ___  =  ___________

  7 << 3  =  7 ×  ___  =  ___________

  1 << 4  =  1 ×  ___  =  ___________
```

---

**Question 5c** &nbsp;*(0.5 points)*

A program uses left shift to calculate storage size.
It starts with 1 KB and shifts left 3 times (`1 << 3`).

How many KB is the final result? ___________

What does this represent in computing? (Circle one)

&nbsp;&nbsp;&nbsp;&nbsp; A) 3 KB &nbsp;&nbsp;&nbsp;&nbsp; B) 6 KB &nbsp;&nbsp;&nbsp;&nbsp; C) 8 KB &nbsp;&nbsp;&nbsp;&nbsp; D) 16 KB

---

## Section 6 — Right Shift (`>>`) &nbsp;&nbsp; *(1.5 points)*

> 💡 Right shift moves bits to the right and drops bits on the right.
> Each right shift by 1 **halves** the number (integer division — remainder is dropped).
> Pattern: `x >> n` = `x ÷ 2ⁿ`

---

**Question 6a** &nbsp;*(0.5 points)*

Compute `20 >> 2` using the bit diagram below:

```
  20  in binary  →   1  0  1  0  0
  >> 2 (shift)   →         _  _  _    (two bits dropped on the right)
```

**Answer (decimal):** &nbsp; `20 >> 2` = ___________

Verify using the pattern: &nbsp; `20 ÷ 2²` = `20 ÷ ___` = ___________

---

**Question 6b** &nbsp;*(0.5 points)*

Without drawing bits, use the pattern `x >> n = x ÷ 2ⁿ` to fill in the blanks:

```
  48 >> 1  =  48 ÷  ___  =  ___________

  48 >> 3  =  48 ÷  ___  =  ___________

   7 >> 1  =   7 ÷  ___  =  ___________    (hint: what happens to the remainder?)
```

---

**Question 6c** &nbsp;*(0.5 points)*

A clever programmer uses a bitwise trick to check if a number is **even or odd**:

```
  if n & 1 == 0:
      print("even")
  else:
      print("odd")
```

Using the AND trick, label each number below as **even** or **odd**:

| Expression | Result | Even or Odd? |
|------------|--------|--------------|
| `42 & 1` | ___ | ___________ |
| `17 & 1` | ___ | ___________ |
| `100 & 1` | ___ | ___________ |

*(Hint: a number ANDed with 1 gives 0 if even, 1 if odd.)*

---

## ✅ Self-Check Before Submitting

Go through the checklist — check each box when done:

- [ ] I wrote my name and date at the top
- [ ] Section 1 (AND): Questions 1a and 1b are complete with bit-by-bit work and decimal answers
- [ ] Section 2 (OR): Questions 2a and 2b are complete with bit-by-bit work and decimal answers
- [ ] Section 3 (XOR): Questions 3a and 3b are complete
- [ ] Section 4 (NOT): Applied the formula `~x = -(x + 1)`
- [ ] Section 5 (Left Shift): All three parts (5a, 5b, 5c) are answered
- [ ] Section 6 (Right Shift): All three parts (6a, 6b, 6c) are answered

---

## 📸 Submission Instructions

1. Complete all sections on paper **or** by typing your answers directly in this file
2. If written on paper → take a **clear photo or scan** of your completed answer sheet
3. Upload your photo/file to **Google Classroom** under the Lab 26 assignment
4. Make sure your **name is visible** before submitting

---

*Python 101 · Learn and Help Program · [www.learnandhelp.com](https://www.learnandhelp.com) · Week 26*
