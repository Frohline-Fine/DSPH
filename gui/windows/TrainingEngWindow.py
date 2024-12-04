"""
Window Training with translation: Solve random questions - no strings attached
"""
# imports
from PyQt6.QtWidgets import QWidget

from gui.layouts.training_eng_window import training_eng_layout
from gui.widgets.button import Button
from gui.widgets.label import Label
from helper.constants import BTN_ANSWER, BTN_NEXT, TRAINING
from helper.gui_helper import random_exercise, concat
from helper.translator import translate


class TrainingEngWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Training (english)")
        self.setFixedSize(1550, 950)
        self.setStyleSheet(f"background-color: rgb({TRAINING}); margin: 20px;")
        self.exercise = random_exercise()

        self.explanation = Label(self)
        self.explanation.setText(None)

        self.question = Label(self)
        self.question.setText(self.exercise[2])

        self.btn_show = Button(self)
        self.btn_show.setText(BTN_ANSWER)
        self.btn_show.clicked.connect(self.show_answer)

        self.btn_next = Button(self)
        self.btn_next.setText(BTN_NEXT)
        self.btn_next.clicked.connect(self.next_question)

        self.explanation_e = Label(self)
        self.explanation_e.setText(None)

        self.question_e = Label(self)
        self.question_e.setText(translate(self.exercise[2]))

        layout = training_eng_layout(self)

        self.setLayout(layout)

    def show_answer(self):
        self.explanation.setText(concat(self.exercise[3], self.exercise[4]))
        self.explanation_e.setText(translate(concat(self.exercise[3], self.exercise[4])))

    def next_question(self):
        self.explanation.setText(None)
        self.explanation_e.setText(None)
        self.exercise = random_exercise()
        self.question.setText(self.exercise[2])
        self.question_e.setText(translate(self.exercise[2]))
