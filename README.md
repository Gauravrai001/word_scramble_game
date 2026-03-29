# Word Scramble Game (Python & Tkinter)

A fast-paced, interactive word-puzzle desktop application built with Python. This game challenges the user's vocabulary and cognitive processing by presenting scrambled words that must be solved within a set number of rounds.

---

## 📖 Table of Contents
1. [Introduction](#introduction)
2. [Key Features](#key-features)
3. [Technical Overview](#technical-overview)
4. [Installation & Setup](#installation--setup)
5. [How to Play](#how-to-play)
6. [Code Architecture](#code-architecture)
7. [UI Design & Aesthetics](#ui-design--aesthetics)
8. [Troubleshooting](#troubleshooting)
9. [Future Enhancements](#future-enhancements)
10. [License](#license)

---

## 1. Introduction
The **Word Scramble Game** is a lightweight Graphical User Interface (GUI) application. It is designed to be both an educational tool for language learners and a foundational project for developers interested in Python’s `tkinter` library. By utilizing event-driven programming, the application manages real-time user input, scoring, and automated game transitions.

## 2. Key Features
* **Randomized Word Selection:** Pulls from a built-in library of diverse nouns and objects.
* **Dynamic Shuffling:** Uses the Fisher-Yates shuffle logic to ensure character positions are randomized every time.
* **Automated Game Loop:** A 5-round system that tracks progress and displays a final summary.
* **Visual Feedback:** Immediate color-coded responses (Green for success, Red for failure).
* **Non-Blocking Delay:** Uses the `.after()` method to pause briefly after an answer, allowing the user to see the result before the next word appears.

## 3. Technical Overview
The project is written in **Python 3.x** and relies on two core modules:
* **Tkinter:** The standard Python interface for Tcl/Tk, used to create the window, labels, buttons, and entry fields.
* **Random:** Used for both selecting a word from the list and shuffling the characters of that word.

## 4. Installation & Setup
To run this game locally, follow these steps:

### Prerequisites
Ensure you have Python installed. You can verify this by typing `python --version` in your terminal.

### Steps
1.  **Clone or Copy:** Copy the source code into a file named `word_scramble.py`.
2.  **Navigate:** Open your terminal or command prompt and navigate to the folder where the file is saved.
3.  **Execute:** Run the script using the following command:
    ```bash
    python word_scramble.py
    ```

## 5. How to Play
1.  **Launch the Game:** A window titled "Word Scramble Game" will appear.
2.  **Identify the Word:** Look at the bright cyan text in the center—this is your scrambled word.
3.  **Type Your Guess:** Enter what you believe is the correct word into the text box.
4.  **Submit:** Click the "Submit" button or press Enter (if bound).
5.  **Review:** If correct, your score increases. If wrong, the correct word is revealed.
6.  **Repeat:** Complete 5 rounds to see your final score!

## 6. Code Architecture
The application is built using **Object-Oriented Programming (OOP)** principles.

### The `WordScrambleGame` Class
* **`__init__(self, root)`**: Sets up the GUI environment, defines the color scheme, and initializes the score counters.
* **`scramble_word(self, word)`**: 
    * Converts the string into a list of characters.
    * Uses `random.shuffle()` to rearrange them.
    * Joins them back into a string.
* **`next_word(self)`**: The "manager" function. It checks if the game is over. If not, it picks a new word and resets the entry field.
* **`check_answer(self)`**: Logic handler that compares `guess.lower()` to the `current_word`. It updates the UI labels based on the result.

## 7. UI Design & Aesthetics
The game utilizes a "Dark Mode" aesthetic to provide a modern feel and reduce eye strain:
* **Window Background:** `#212121` (Deep Charcoal)
* **Primary Accent:** `#00ffcc` (Neon Cyan) for the scrambled word.
* **Feedback Labels:** `#CFA3A6` (Muted Rose) and `#065130` (Forest Green) to provide distinct visual zones for status and scoring.

## 8. Troubleshooting
* **Tkinter Not Found:** If you receive an `ImportError`, you may be on a Linux system that requires a separate install. Run `sudo apt-get install python3-tk`.
* **Window Scaling:** The geometry is set to `450x310`. On high-DPI displays, you may want to adjust `self.root.geometry` to a larger size.
* **Input Sensitivity:** The game is case-insensitive (it converts your input to lowercase automatically), so don't worry about accidental Caps Lock!

## 9. Future Enhancements
Planned updates for version 2.0 include:
1.  **Timer Integration:** A 15-second countdown for each word.
2.  **Difficulty Settings:** Choosing between 3-letter words and 8-letter words.
3.  **External Word List:** The ability to load words from a `.txt` file.
4.  **Sound Effects:** Audio cues for "Correct" and "Game Over."

## 10. License
This project is released under the **MIT License**. You are free to use, modify, and distribute this code for personal and commercial projects.
