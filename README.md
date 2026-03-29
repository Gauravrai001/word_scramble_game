# word_scramble_game

# Word Scramble Game (Python & Tkinter)

This is a simple and interactive **Word Scramble Game** made using Python and Tkinter. In this game, a scrambled (mixed) word is shown to the user, and the user has to guess the correct word.

---

## 📖 Table of Contents

1. Introduction
2. Key Features
3. Technical Overview
4. Installation & Setup
5. How to Play
6. Code Structure
7. UI Design
8. Problems & Solutions
9. Future Improvements
10. License

---

## 1. Introduction

**Word Scramble Game** is a basic GUI project that is very useful for beginners. In this project, we used Python’s `tkinter` library to create a window-based game.

This game is useful for both learning and fun. It also helps improve vocabulary and programming skills.

---

## 2. Key Features

* Random words are generated
* Words are automatically scrambled
* Game has total 5 rounds
* Score increases for correct answers
* Correct word is shown for wrong answers
* Simple and clean GUI
* Instant feedback (Correct / Wrong)

---

## 3. Technical Overview

This project uses:

* **Python 3.x** → Main programming language
* **Tkinter** → For creating GUI
* **Random Module** → For selecting and shuffling words

---

## 4. Installation & Setup

### Step 1: Check Python

Type in terminal:

```bash
python --version
```

### Step 2: Create file

Save the code in a file:

```bash
word_scramble.py
```

### Step 3: Run the program

```bash
python word_scramble.py
```

---

## 5. How to Play

1. The game window will open
2. A scrambled word will be shown
3. You have to guess the correct word
4. Type your answer in the input box
5. Click the submit button
6. Result will be shown (Correct or Wrong)
7. Score will update
8. After 5 rounds, final score will be displayed

---

## 6. Code Structure

The game is based on a class:

### `WordScrambleGame` Class

* `__init__()`
  → Sets up the GUI (window, labels, buttons)

* `scramble_word()`
  → Mixes the letters of the word

* `next_word()`
  → Selects the next word for the next round

* `check_answer()`
  → Checks the user's answer

---

## 7. UI Design

The game uses a simple dark theme:

* Background color → Dark (#212121)
* Scrambled word → Neon color (#00ffcc)
* Result → Green (correct) / Red (wrong)
* Score → Highlighted

This design is clean and easy for the eyes

---

## 8. Problems & Solutions

* If tkinter error comes:

```bash
sudo apt-get install python3-tk
```

* To change window size:

```python
self.root.geometry("500x350")
```

* No case issue because input is converted to lowercase

---

## 9. Future Improvements

* Add timer
* Add difficulty levels
* Add sound effects
* Add restart button
* Add high score system

---

## 10. License

This project is free to use for learning and practice. You can modify and improve it.

---


##  Final Note

This project is perfect for beginners. You can learn:

* Python basics
* GUI programming
* Game logic
