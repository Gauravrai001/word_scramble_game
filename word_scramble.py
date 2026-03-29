import tkinter as tk
import random

words = ["cat", "dog", "sun", "hat", "pen", "cup", "book", "tree", "milk", "ring" , "ant", "bat", "car", "map", "bed", "fox", "ice", "key", "lip", "net",
    "owl", "pig", "ram", "toy", "van", "wet", "zip", "ball", "fish",
    "lamp", "moon", "star", "wind", "leaf", "rock"     ]

# Main game class
class WordScrambleGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Word Scramble Game")
        self.root.geometry("450x310")
        self.root.configure(bg="#212121")

        self.score = 0
        self.round = 0
        self.max_rounds = 5

        # Title
        self.tl = tk.Label(root, text="Word Scramble Game", 
                                    font=("Arial", 20, "bold"), 
                                    bg="#0e5d63", fg="white")
        self.tl.pack(pady=10)

        # Scrambled word display
        self.wl = tk.Label(root, text="", 
                                   font=("Arial", 26, "bold"), 
                                   bg="#1e1e2f", fg="#00ffcc")
        self.wl.pack(pady=15)

        # Entry box
        self.entry = tk.Entry(root, font=("Arial", 15))
        self.entry.pack(pady=10)

        # Submit button
        self.sb = tk.Button(root, text="Submit", 
                                    command=self.check_answer,
                                    bg="#443740", fg="black",
                                    font=("Arial", 13, "bold"))
        self.sb.pack(pady=5)

        # Result label
        self.rl = tk.Label(root, text="", 
                                     font=("Arial", 13), 
                                     bg="#CFA3A6", fg="white")
        self.rl.pack(pady=5)

        # Score label
        self.score_label = tk.Label(root, text="Score: 0", 
                                    font=("Arial", 13), 
                                    bg="#065130", fg="white")
        self.score_label.pack(pady=5)

        self.next_word()

    def scramble_word(self, word):
        word_list = list(word)
        random.shuffle(word_list)
        return ''.join(word_list)

    def next_word(self):
        if self.round >= self.max_rounds:
            self.wl.config(text="Game Over!")
            self.rl.config(text=f"Final Score: {self.score}/{self.max_rounds}")
            return

        self.current_word = random.choice(words)
        scrambled = self.scramble_word(self.current_word)

        self.wl.config(text=scrambled)
        self.entry.delete(0, tk.END)
        self.round += 1

    def check_answer(self):
        guess = self.entry.get().lower()

        if guess == self.current_word:
            self.rl.config(text="Correct!", fg="lightgreen")
            self.score += 1
        else:
            self.rl.config(
                text=f" Wrong! Word was: {self.current_word}", 
                fg="red"
            )

        self.score_label.config(text=f"Score: {self.score}")
        self.root.after(1500, self.next_word)


root = tk.Tk()
game = WordScrambleGame(root)
root.mainloop()