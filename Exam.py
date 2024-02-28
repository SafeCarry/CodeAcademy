import tkinter as tk
from tkinter import messagebox
import random


class MathGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Math Game")
        self.root.geometry("400x200")

        self.current_color = "white"
        self.fade_speed = 0.1
        self.cheat_uses = 5

        self.question_label = tk.Label(root, text="", font=("Arial", 24))
        self.question_label.pack()

        self.answer_entry = tk.Entry(root, font=("Arial", 18))
        self.answer_entry.pack()

        self.check_button = tk.Button(root, text="Check", command=self.check_answer)
        self.check_button.pack()

        self.cheat_button = tk.Button(root, text="Cheat", command=self.cheat_answer)
        self.cheat_button.pack()

        self.cheat_counter_label = tk.Label(root, text=f"Cheat uses left: {self.cheat_uses}", font=("Arial", 12))
        self.cheat_counter_label.pack()

        self.generate_question()

    def generate_question(self):
        num1 = random.randint(1, 5000)
        num2 = random.randint(1, 5000)
        operator = random.choice(['+', '*'])  # Addition or multiplication only
        question = f"{num1} {operator} {num2}"
        self.answer = eval(question)
        self.question_label.config(text=question)

    def check_answer(self):
        try:
            user_answer = int(self.answer_entry.get())
            if user_answer == self.answer:
                self.change_color("green")
                self.root.after(int(self.fade_speed * 1000), self.change_color, "white")
                self.generate_question()
            else:
                self.change_color("red")
                self.root.after(int(self.fade_speed * 1000), self.change_color, "white")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")
            self.answer_entry.delete(0, tk.END)

    def check_answer(self):
        try:
            user_answer = int(self.answer_entry.get())
            if user_answer == self.answer:
                self.change_color("green")
                self.root.after(int(self.fade_speed * 1000), self.change_color, "white")
                self.root.after(2000, self.change_color, "white")  # Wait for 2 seconds before turning the color back to white
                self.generate_question()
            else:
                self.change_color("red")
                self.root.after(int(self.fade_speed * 1000), self.change_color, "white")
                self.root.after(2000, self.change_color, "white")  # Wait for 2 seconds before turning the color back to white
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")
            self.answer_entry.delete(0, tk.END)

    def update_cheat_counter(self):
        self.cheat_counter_label.config(text=f"Cheat uses left: {self.cheat_uses}")

    def change_color(self, color):
        self.root.config(bg=color)
        self.current_color = color

    def cheat_answer(self):
        if self.cheat_uses > 0:
            self.answer_entry.delete(0, tk.END)
            self.answer_entry.insert(0, str(self.answer))
            self.cheat_uses -= 1
            self.update_cheat_counter()
        else:
            messagebox.showinfo("Cheat Limit", "You have exhausted all cheat uses.")

if __name__ == "__main__":
    root = tk.Tk()
    app = MathGame(root)
    root.mainloop()