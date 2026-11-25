# Final Project: Substitution Cipher Decoding

## Programming Exercise

For the **Final Project**, you will be implementing **Programming Exercise 8.1 from Chapter 8 (Page 283)**.

The goal of this project is to decode an English-language message that has been encoded using a **substitution cipher**.

---


## What is a Substitution Cipher?

A **substitution cipher** is a method of encoding a message by replacing each letter in the original message with another letter according to a fixed mapping.

For example, suppose part of the mapping is:

```text
Original:  a  b  c  d  e
Encoded:   q  w  e  r  t
```

Using this mapping, every `a` in the original message would be replaced with `q`, every `b` with `w`, every `c` with `e`, and so on.

The important rule is **consistency**: the same plaintext letter is always replaced by the same encoded letter throughout the message.

Although the letters are changed, many characteristics of the original English message remain visible:

- Spaces between words
- Word lengths
- Repeated words
- Repeated letter patterns
- Frequency of letters
- Common one-letter, two-letter, and three-letter word patterns

These clues can be used to decode the message.

For example, if the encoded word:

```text
gsc
```

appears frequently, you might hypothesize that it represents the common English word:

```text
the
```

If that assumption is correct, you have discovered three possible mappings:

```text
g -> t
s -> h
c -> e
```

You can then apply these mappings throughout the encoded message and examine the partially decoded text for additional clues.

In this project, you will use this type of reasoning together with **character frequency analysis** and a Python **dictionary** to gradually determine the substitution mapping and recover the original message.

---

## Encoded Message

Use the following encoded message as the input to your program:

```python
encoded_msg = "jyn fg jggtwj djtfcn stf sjyn edcyjnc ia zy stes fjqtye z wzdn owcff gstf gsq sjyn edcyjnc gsjg mtgs tg gszi xjqcfg owzm gstyc cycxtcf gz gtyq otgf ty gsq xcdhq jyn gsc wzdn ntn edty jyn aczawc ntn lcjfg iazy gsc wjxof jyn fwzgsf jyn hjda jyn jyhszktcf jyn zdjyeigjyf jyn odcjvljfg hcdcjwf jyn lditg ojgf jyn gsc wzdn fajvc fjqtye ltdfg fsjwg gszi gjvc zig gsc szwq aty gscy fsjwg gszi hziyg gz gsdcc yz xzdc yz wcff gsdcc fsjwg oc gsc yixocd gszi fsjwg hziyg jyn gsc yixocd zl gsc hziygtye fsjwg oc gsdcc lzid fsjwg gszi yzg hziyg yctgscd hziyg gszi gmz cphcagtye gsjg gszi gscy adzhccn gz gsdcc ltkc tf dtesg zig zyhc gsc yixocd gsdcc octye gsc gstdn yixocd oc dcjhscn gscy wzoocfg gszi gsq szwq sjyn edcyjnc zl jygtzhs gzmjdnf gszi lzc msz octye yjiesgq ty xq ftesg fsjww fyill tg"
```

---

## Project Requirements

### 1. Decode a Substitution Cipher

The message has been encoded using a **substitution cipher**.

In a substitution cipher, each plaintext letter is consistently replaced by another letter.

For example, a hypothetical mapping might look like this:

```text
Plaintext:   a b c d e ...
Encoded:     q w e r t ...
```

Your goal is to determine the mapping between the encoded characters and the original plaintext characters.

---

### 2. No `wordslist.txt`

For this Final Project:

> **There will NOT be a `wordslist.txt` file.**

Your solution should therefore **not depend on a supplied list of English words**.

Instead, you will need to analyze the encoded message and make reasonable assumptions about the English language.

---

### 3. Use Character Frequency Analysis

English letters do not appear with equal frequency.

For example, letters such as:

```text
e, t, a, o, i, n
```

are generally more common in English text than letters such as:

```text
q, x, z, j
```

Your program should analyze the frequency of characters in the encoded message and use those frequencies as clues for determining the substitution mapping.

You may also use other observations, such as:

- Common one-letter words
- Common two-letter words
- Common three-letter words
- Repeated words
- Repeated letter patterns
- Word lengths
- Common English sentence patterns
- Character frequency
- Context within partially decoded sentences

---

## 4. Maintain a Mapping Table

Use a Python **dictionary** to maintain the mapping between encoded characters and plaintext characters.

For example:

```python
mapping = {
    'x': 'e',
    'q': 't',
    'm': 'a'
}
```

You may choose either of these approaches:

```text
encoded character -> plaintext character
```

or

```text
plaintext character -> encoded character
```

However, your choice must be used consistently throughout your program.

---

## 5. Build the Mapping Iteratively

You are **not expected to determine the complete mapping immediately**.

Instead, develop the mapping iteratively.

A possible workflow is:

1. Count the frequency of encoded characters.
2. Make an initial mapping based on English-language frequency.
3. Apply the mapping to the encoded message.
4. Examine the partially decoded output.
5. Identify recognizable words or patterns.
6. Update the mapping.
7. Decode the message again.
8. Repeat until the plaintext message becomes understandable.

Your Google Colab notebook should clearly show this progression.

---

## 6. Manual Updates Are Allowed

You may manually update the mapping dictionary when your analysis suggests that a particular encoded character corresponds to a specific plaintext character.

For example:

```python
mapping['x'] = 'e'
```

Manual updates are allowed and are expected to be part of the problem-solving process.

However, whenever you make a manual update, you must provide a brief explanation of your reasoning.

For example:

```text
The encoded word "abc" occurs many times and appears in positions where
the word "the" would make sense. Therefore, I am testing the mapping
a -> t, b -> h, and c -> e.
```

Your reasoning may be written in a Markdown cell immediately before or after the corresponding code cell.

---

## 7. Show Your Problem-Solving Process

Your notebook should demonstrate **how you arrived at the solution**, not simply contain the final mapping.

Include relevant intermediate work such as:

- Frequency counts
- Sorted frequency tables
- Initial mapping assumptions
- Partially decoded messages
- Mapping-table revisions
- Explanations for manual substitutions
- Additional observations about English words or sentence structure

The iterative reasoning process is an important part of the project.

---

## 8. Final Coding Cell

The **last coding cell** in your Google Colab notebook must print the completely decoded message.

For example:

```python
print(decoded_message)
```

The output of this final cell should be readable English plaintext.

---

# What to Submit

You must submit the following files to the Final Project drop box.

## 1. Google Colab Notebook

Submit your notebook using the filename:

```text
final_project.ipynb
```

Submit the notebook in **both** formats:

- `final_project.ipynb`
- PDF version of the notebook

Your notebook should include your code, analysis, intermediate results, mapping changes, explanations, and final decoded output.

---

## 2. Decoded Text File

Submit a plain-text file named:

```text
decoded.txt
```

This file should contain **only the final decoded message in plain-text format**.

---

# Important

The primary objective of this Final Project is to successfully decode the substitution cipher.

> **If you correctly determine and submit the decoded message, you will earn full credit for the Final Project.**

At the same time, your Google Colab notebook should clearly demonstrate the iterative analysis and reasoning you used to arrive at the decoded text.

---

## Suggested Notebook Organization

A well-organized submission might contain the following sections:

```text
1. Encoded Message
2. Character Frequency Analysis
3. Initial Mapping
4. First Decoding Attempt
5. Mapping Revisions
6. Additional Decoding Attempts
7. Final Mapping
8. Final Decoded Message
9. Save / Produce decoded.txt
```

Your exact implementation may differ. There is no single required algorithm as long as you satisfy the project requirements and successfully decode the message.
