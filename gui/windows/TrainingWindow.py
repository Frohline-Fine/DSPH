"""
Window Training: Solve random questions - no strings attached
"""
# imports
from PyQt6.QtWidgets import QWidget

from gui.layouts.training import training_layout
from gui.widgets.button import Button
from gui.widgets.label import Label
from helper.constants import ANSWER, NEXT
from helper.gui_helper import random_exercise, concat


class TrainingWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Training")
        self.setFixedSize(800, 800)
        self.setStyleSheet("background-color: rgb(185,211,238); margin: 20px;")
        self.exercise = random_exercise()

        self.explanation = Label(self)
        self.explanation.setText(None)

        self.question = Label(self)
        self.question.setText(self.exercise[2])

        self.btn_show = Button(self)
        self.btn_show.setText(ANSWER)
        self.btn_show.clicked.connect(self.show_answer)

        self.btn_next = Button(self)
        self.btn_next.setText(NEXT)
        self.btn_next.clicked.connect(self.next_question)

        main_layout = training_layout(self)

        self.setLayout(main_layout)

    def show_answer(self):
        self.explanation.setText(concat(self.exercise[3], self.exercise[4]))

    def next_question(self):
        self.explanation.setText(None)
        self.exercise = random_exercise()
        self.question.setText(self.exercise[2])
