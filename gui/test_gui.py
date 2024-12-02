import sys

from PyQt6.QtGui import QFont

from helper.translator import translate
from helper.gui_helper import random_exercise

from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import (
    QDialog,
    QApplication, QLabel, QPushButton, QGridLayout, )


class TrainDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aufgabe")
        self.setFixedSize(1200, 800)
        self.exercise = random_exercise()

        self.button_answer = QPushButton("Zeige Antwort")
        self.button_answer.setIconSize(QSize(16, 16))
        self.button_answer.clicked.connect(self.show_answer)

        self.button_reset = QPushButton("Neue Frage")
        self.button_reset.setIconSize(QSize(16, 16))
        self.button_reset.clicked.connect(self.reset)

        self.label_question = QLabel(self.exercise[2])
        self.label_question.setFont(QFont('Arial', 12))
        self.label_question.setWordWrap(True)

        self.label_question_e = QLabel(translate(self.exercise[2]))
        self.label_question_e.setFont(QFont('Arial', 12))
        self.label_question_e.setWordWrap(True)

        self.label_answer = QLabel(self.exercise[3])
        self.label_answer.setFont(QFont('Arial', 12))
        self.label_answer.setWordWrap(True)
        self.label_answer.setHidden(True)

        self.label_explanation = QLabel(self.exercise[4])
        self.label_explanation.setFont(QFont('Arial', 12))
        self.label_explanation.setWordWrap(True)
        self.label_explanation.setHidden(True)

        self.label_explanation_e = QLabel(translate(self.exercise[4]))
        self.label_explanation_e.setFont(QFont('Arial', 12))
        self.label_explanation_e.setWordWrap(True)
        self.label_explanation_e.setHidden(True)

        main_layout = QGridLayout()
        main_layout.setSpacing(20)
        main_layout.setContentsMargins(20, 20, 20, 20)

        main_layout.addWidget(self.label_question, 0, 0)
        main_layout.addWidget(self.label_question_e, 0, 1)

        main_layout.addWidget(self.label_answer, 1, 0)
        main_layout.addWidget(self.label_explanation, 2, 0)
        main_layout.addWidget(self.label_explanation_e, 2, 1)
        main_layout.addWidget(self.button_answer, 3, 0)
        main_layout.addWidget(self.button_reset, 3, 1)

        self.setLayout(main_layout)

    def show_answer(self):
        self.label_answer.setHidden(False)
        self.label_explanation.setHidden(False)
        self.label_explanation_e.setHidden(False)
        self.button_answer.setHidden(True)

    def hide_answer(self):
        self.label_answer.setHidden(True)
        self.label_explanation.setHidden(True)
        self.label_explanation_e.setHidden(True)
        self.button_answer.setHidden(False)

    def reset(self):
        self.hide_answer()

        self.exercise = random_exercise()
        self.label_question.setText(self.exercise[2])
        self.label_question_e.setText(translate(self.exercise[2]))
        self.label_answer.setText(self.exercise[3])
        self.label_explanation.setText(self.exercise[4])
        self.label_explanation_e.setText(translate(self.exercise[4]))


def test_gui():
    app = QApplication(sys.argv)
    main_dialog = TrainDialog()
    main_dialog.show()
    sys.exit(app.exec())
