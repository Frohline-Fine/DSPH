import sys
from pathlib import Path

from PyQt6.QtGui import QFont

from helper.get_exercise import get_exercise
from helper.translator import translate

import pandas as pd
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import (
    QDialog,
    QApplication, QLabel, QPushButton, QGridLayout, )

path_to_csv = Path(__file__).parent.parent / 'data_extractor' / 'data' / 'test.csv'


class TrainDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aufgabe")
        self.resize(500, 500)
        self.dataframe = pd.read_csv(path_to_csv)
        self.exercise = get_exercise(self.dataframe)

        self.button_answer = QPushButton("Zeige Antwort")
        self.button_answer.setIconSize(QSize(16, 16))
        self.button_answer.clicked.connect(self.show_answer)

        self.button_reset = QPushButton("Neue Frage")
        self.button_reset.setIconSize(QSize(16, 16))
        self.button_reset.clicked.connect(self.reset)

        self.label_question = QLabel(self.exercise[0])
        self.label_question.setFont(QFont('Arial', 12))
        self.label_question_e = QLabel(translate(self.label_question.text()))
        self.label_question_e.setFont(QFont('Arial', 12))

        self.label_answer = QLabel(self.exercise[1])
        self.label_answer.setFont(QFont('Arial', 12))
        self.label_answer.setHidden(True)

        self.label_explanation = QLabel(self.exercise[2])
        self.label_explanation.setFont(QFont('Arial', 12))
        self.label_explanation.setHidden(True)

        self.label_explanation_e = QLabel(translate(self.exercise[2]))
        self.label_explanation_e.setFont(QFont('Arial', 12))
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

    def reset(self):
        self.label_answer.setHidden(True)
        self.label_explanation.setHidden(True)
        self.label_explanation_e.setHidden(True)
        self.button_answer.setHidden(False)

        self.exercise = get_exercise(self.dataframe)
        self.label_question.setText(self.exercise[0])
        self.label_question_e.setText(translate(self.exercise[0]))
        self.label_answer.setText(self.exercise[1])
        self.label_explanation.setText(self.exercise[2])
        self.label_explanation_e.setText(self.exercise[2])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_dialog = TrainDialog()
    main_dialog.show()
    sys.exit(app.exec())
