# Assignment 1 – Pirate Language Translator

**Points:** 25  
**Submission:** Google Colab Notebook (`assignment_1.ipynb`) and PDF

## Objective

In this assignment, you will develop a Python program that translates ordinary English text into **Pirate Language**.

Pirate Language is not a real language. For this assignment, it is a collection of English words and phrases that are replaced with pirate-style expressions.

This assignment gives you practice working with:

- Python strings
- Dictionaries
- String manipulation
- Functions
- User input
- Basic text processing

## Pirate Language Dictionary

Your program should use the following translations:

| English | Pirate Language |
|---|---|
| hello | ahoy |
| hi | yo-ho-ho |
| my | me |
| friend | matey |
| sir | matey |
| madam | proud beauty |
| officer | foul blaggart |
| stranger | scurvy dog |
| where | whar |
| is | be |
| are | be |
| the | th' |
| you | ye |
| your | yer |
| excuse | arr |
| hotel | fleabag inn |
| restaurant | galley |
| kitchen | galley |
| bathroom | head |
| money | doubloons |
| treasure | booty |
| yes | aye |
| no | nay |
| OK | aye |

## Requirements

Write a Python program that:

1. Accepts an English sentence or paragraph as input.
2. Stores the English-to-Pirate translations in a Python **dictionary**.
3. Examines the input text and replaces English words found in the dictionary with their corresponding Pirate Language translations.
4. Handles words regardless of capitalization. For example, `Officer`, `officer`, and `OFFICER` should all be recognized.
5. Handles punctuation appropriately. A word should still be recognized when followed by punctuation such as `Officer!`, `hotel.`, or `kitchen?`.
6. Does not change words that are not found in the Pirate Language dictionary.
7. Displays both the original English text and the translated Pirate Language text.
8. Organizes the translation logic into at least one function.

## Required Test Phrase

At a minimum, test your program using the following phrase:

```python
input_text = "Hello Officer! Excuse my messy hotel! Are you OK to stay in the kitchen?"
```

Your program should identify all applicable English words in the sentence and translate them using the Pirate Language dictionary.

You are encouraged to test your program with additional sentences.

## Important Considerations

Be careful when performing replacements.

For example, replacing a sequence of characters without checking word boundaries can accidentally modify part of another word. Your program should translate **words**, not arbitrary character sequences within words.

Also consider how your program will preserve punctuation while translating the associated word.

## Google Colab Notebook

Complete the assignment using **Google Colab**.

Your notebook should include:

- Your name
- Assignment title
- Brief description of your approach
- Python code
- The required test phrase
- At least two additional test cases
- Program output

Your code should be readable and appropriately commented.

## Use of AI Tools

You may use AI tools such as ChatGPT, Gemini, Claude, or GitHub Copilot to assist you.

However, **you are responsible for understanding the code you submit**. You should be able to explain your solution and make reasonable modifications to it if requested.

## What to Submit

Submit your Google Colab notebook as:

- `assignment_1.ipynb`
- PDF version of the completed notebook

Upload **both files** to the assignment drop box.

## Evaluation Criteria – 25 Points

| Criterion | Points |
|---|---:|
| Correctly defines and uses the Pirate Language dictionary | 4 |
| Correctly translates words using the dictionary | 6 |
| Correctly handles capitalization and punctuation | 4 |
| Uses at least one function to organize the translation logic | 3 |
| Successfully runs the required test phrase | 2 |
| Includes at least two additional meaningful test cases | 2 |
| Code quality: readability, organization, and appropriate comments | 2 |
| Submission is complete: `.ipynb` and PDF with required notebook information and output | 2 |
| **Total** | **25** |
