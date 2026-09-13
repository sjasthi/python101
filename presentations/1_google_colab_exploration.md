<p align="center">
  <img src="https://www.learnandhelp.com/images/supported_by/learn_n_help_logo.png"
       alt="Learn and Help Logo"
       width="288">
  <br>
  <strong><em>Empowering Minds, Inspiring Generosity!</em></strong>
  <br>
  <a href="https://www.learnandhelp.com">
    <strong>www.learnandhelp.com</strong>
  </a>
</p>


# 1: Exploring Python with Google Colab

Welcome to Python 101! 🎉 [www.learnandhelp.com](http://www.learnandhelp.com)

Today we are not learning *how* Python works yet — we are just going to **play** with it and see it run for real, in a notebook in your web browser, using a free tool called **Google Colab**.

## How to use Google Colab

1. Open **<https://colab.research.google.com/>**
2. Sign in with your Google account (the same kind you use for Google Classroom)
3. Click **"New notebook"**
4. You'll see a gray box — this is called a **code cell**. This is where your code lives.
5. Copy one of the snippets below and **paste it** into the code cell
6. Press **Shift + Enter** to run the cell — your output appears right underneath!
7. Click the **+ Code** button to add a new cell for the next snippet

That's it! Try each snippet below in order. Don't worry about understanding every detail yet — we'll learn all of this soon. Today is just for exploring and having fun. 🚀

---

## Snippet 1: Say Hello

```
print("Hello, World!")
```

## Snippet 2: Say a Few Things

```
print("Hello, World!")
print("My name is Python.")
print("I am learning to code!")
```

## Snippet 3: A Little Math

```
print(5 + 3)
print(10 - 4)
print(6 * 7)
```

## Snippet 4: My Age (a Box that Holds a Value)

```
age = 12
print(age)
```

Run this one, then click into the cell and change `12` to your own age. Press **Shift + Enter** again — Colab reruns the cell and shows your new output right away!

## Snippet 5: A Few Boxes Together

```
name = "Maya"
age = 12
email = "maya@example.com"
print(name)
print(age)
print(email)
```

## Snippet 6: Doing Some Math

```
apples = 5
oranges = 3
total = apples + oranges
print(total)
```

## Snippet 7: More Math with Marks

```
math_marks = 90
science_marks = 85
total_marks = math_marks + science_marks
average_marks = total_marks / 2
print(total_marks)
print(average_marks)
```

## Snippet 8: A Simple Shopping List

```
print("My Shopping List")
print("Apples")
print("Bananas")
print("Chocolate")
```

## Snippet 9: A Little Drawing with Symbols

```
print("*")
print("**")
print("***")
print("****")
```

## Snippet 10: Ask and Tell

```
name = "Coder"
age = 12
print("Hi there,", name, "!")
print("You are", age, "years old.")
print("Welcome to Python 101!")
```

---

## A Colab Trick Worth Knowing

Unlike a lot of other tools, Colab lets you **run cells in any order**, and each cell remembers what happened before it. Try this:

1. Put Snippet 4 (the `age` one) in one cell and run it
2. Put Snippet 6 (the `apples`/`oranges` one) in a *different* cell and run it
3. Now add a brand-new cell below both, and try:

```
print(age)
print(total)
```

Even though `age` and `total` were created in earlier cells, Colab still remembers them! That's because all your cells share the same notebook "memory" as long as you don't restart it.

## Challenge (optional, for the curious!)

Pick your favorite snippet above and try changing something — a word, a number, or a symbol. Run it again with **Shift + Enter** and see what happens. What did you change, and what changed in the output?

Also try clicking **+ Text** above your cells and typing a short note, like "This one prints my age." Colab lets you mix notes and code in the same notebook — just like a science notebook, but one that actually runs!

You did it — you just explored real Python code in a professional coding notebook. We'll learn exactly *why* everything works the way it does in our next classes.
