import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt, QTimer
import random

motivational_quotes = [
    "You're beautiful, keep going!",
    "You're doing great!",
    "Wow! So good!",
    "Great job!",
    "Woo!",
    "YEAAH! YOU'RE SO GOOD",
    "Smarty pants",
    ":)",
    "Wow",
    "Amazing math skills"
]

class MathGame(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple Math Game")
        self.setWindowIcon(QIcon('doomed.ico'))  # Set the GIF as the program's icon
        self.setGeometry(100, 100, 400, 250)

        self.current_color = "white"
        self.fade_speed = 0.1
        self.cheat_uses = 5

        self.question_label = QLabel(self)
        self.question_label.setGeometry(20, 20, 360, 50)
        self.question_label.setAlignment(Qt.AlignCenter)

        self.motivational_label = QLabel(self)
        self.motivational_label.setGeometry(20, 80, 360, 50)
        self.motivational_label.setAlignment(Qt.AlignCenter)

        self.answer_entry = QLineEdit(self)
        self.answer_entry.setGeometry(20, 140, 360, 40)
        self.answer_entry.setFont(QFont(self.answer_entry.font().family(), self.answer_entry.font().pointSize() * 2))
        self.answer_entry.setStyleSheet("background-color: white;")

        self.check_button = QPushButton("Check", self)
        self.check_button.setGeometry(20, 190, 100, 40)
        self.check_button.clicked.connect(self.check_answer)

        self.cheat_button = QPushButton("Cheat", self)
        self.cheat_button.setGeometry(130, 190, 100, 40)
        self.cheat_button.clicked.connect(self.cheat_answer)

        self.cheat_counter_label = QLabel(self)
        self.cheat_counter_label.setGeometry(240, 190, 140, 40)
        self.cheat_counter_label.setAlignment(Qt.AlignCenter)
        self.update_cheat_counter()

        self.generate_question_timer = QTimer(self)
        self.generate_question_timer.timeout.connect(self.generate_question)

        self.answer_color_timer = QTimer(self)
        self.answer_color_timer.timeout.connect(self.reset_color)

        self.generate_question()

    def generate_question(self):
        num1 = random.randint(1, 5000)
        num2 = random.randint(1, 5000)
        operator = random.choice(['+', '*'])
        question = f"{num1} {operator} {num2}"
        self.answer = eval(question)
        self.question_label.setText(question)

        self.motivational_label.setText(random.choice(motivational_quotes))

        self.enable_cheat_button()

    def check_answer(self):
        try:
            user_answer = int(self.answer_entry.text())
            if user_answer == self.answer:
                self.change_color("green")
                self.answer_color_timer.start(2000)
                self.generate_question_timer.start(2000)
            else:
                self.change_color("red")
                self.answer_color_timer.start(2000)
        except ValueError:
            QMessageBox.critical(self, "Error", "Please enter a valid number.")
            self.answer_entry.clear()

    def cheat_answer(self):
        if self.cheat_uses > 0:
            self.answer_entry.setText(str(self.answer))
            self.cheat_uses -= 1
            self.update_cheat_counter()
            self.disable_cheat_button()
            if self.cheat_uses == 0:
                self.disable_cheat_button()
        else:
            QMessageBox.information(self, "Cheat Limit", "You have exhausted all cheat uses.")

    def update_cheat_counter(self):
        self.cheat_counter_label.setText(f"Cheat uses left: {self.cheat_uses}")

    def change_color(self, color):
        self.current_color = color
        self.setStyleSheet(f"background-color: {color};")
        self.question_label.setStyleSheet(f"background-color: {color};")
        self.motivational_label.setStyleSheet(f"background-color: {color};")
        self.cheat_counter_label.setStyleSheet(f"background-color: {color};")
        self.answer_entry.setStyleSheet("background-color: white;")

    def reset_color(self):
        self.change_color("white")
        self.answer_color_timer.stop()

    def disable_cheat_button(self):
        self.cheat_button.setEnabled(False)

    def enable_cheat_button(self):
        self.cheat_button.setEnabled(True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MathGame()
    window.show()
    sys.exit(app.exec_())