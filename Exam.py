import tkinter as tk
from tkinter import messagebox
import random


class MathGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Math Game")
        self.root.geometry("400x200")

        self.dark_mode = False
        self.current_color = "white"
        self.fade_speed = 0.1

        self.question_label = tk.Label(root, text="", font=("Arial", 24))
        self.question_label.pack()

        self.answer_entry = tk.Entry(root, font=("Arial", 18))
        self.answer_entry.pack()

        self.check_button = tk.Button(root, text="Check", command=self.check_answer)
        self.check_button.pack()

        self.cheat_button = tk.Button(root, text="Cheat", command=self.cheat_answer)
        self.cheat_button.pack(side="left")

        self.dark_mode_button = tk.Button(root, text="Dark Mode", command=self.toggle_dark_mode)
        self.dark_mode_button.pack(side="right")

        self.generate_question()

    def generate_question(self):
        num1 = random.randint(1, 5000)
        num2 = random.randint(1, 5000)
        operator = random.choice(['+', '*'])  # Removing division operation
        question = f"{num1} {operator} {num2}"
        self.answer = eval(question)
        self.question_label.config(text=question)

    def check_answer(self):
        try:
            user_answer = int(self.answer_entry.get())
            if user_answer == self.answer:
                self.change_color("green")
                self.root.after(int(self.fade_speed * 1000), self.change_color, self.current_color)
                self.generate_question()
            else:
                self.change_color("red")
                self.root.after(int(self.fade_speed * 1000), self.change_color, self.current_color)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")
            self.answer_entry.delete(0, tk.END)

    def cheat_answer(self):
        self.answer_entry.delete(0, tk.END)
        self.answer_entry.insert(0, str(self.answer))

    def toggle_dark_mode(self):
        if self.dark_mode:
            self.root.config(bg="white")
            self.dark_mode = False
        else:
            self.root.config(bg="#363636")
            self.dark_mode = True

    def change_color(self, color):
        self.root.config(bg=color)
        self.current_color = color


if __name__ == "__main__":
    root = tk.Tk()
    app = MathGame(root)
    root.mainloop()