import sys
from pathlib import Path

from PyQt6.QtGui import QFont

from helper.get_exercise import get_exercise
from helper.translator import translate

import pandas as pd
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QDialog,
    QApplication, QLabel, QVBoxLayout, QPushButton, )

path_to_csv = Path(__file__).parent.parent / 'data_extractor' / 'data' / 'test.csv'


class TrainDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aufgabe")
        self.resize(500, 500)
        self.dataframe = pd.read_csv(path_to_csv)
        self.exercise = get_exercise(self.dataframe)

        self.button = QPushButton("Zeige Antwort")
        self.button.clicked.connect(self.on_click)

        self.label_question = QLabel(self.exercise[0])
        self.label_question.setFont(QFont('Arial', 12))
        self.label_question_e = QLabel(translate(self.label_question.text()))
        self.label_question_e.setFont(QFont('Arial', 12))
        # label_question.setWordWrap(True)
        self.label_answer = QLabel(self.exercise[1])
        self.label_answer.setFont(QFont('Arial', 12))
        self.label_explanation = QLabel(self.exercise[2])
        self.label_explanation.setFont(QFont('Arial', 12))
        self.label_explanation_e = QLabel(translate(self.exercise[2]))
        self.label_explanation_e.setFont(QFont('Arial', 12))

        mein_layout = QVBoxLayout()
        mein_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        mein_layout.setSpacing(20)
        mein_layout.setContentsMargins(20, 20, 20, 20)
        mein_layout.addWidget(self.label_question)
        mein_layout.addWidget(self.label_question_e)
        mein_layout.addWidget(self.label_answer)
        mein_layout.addWidget(self.label_explanation)
        mein_layout.addWidget(self.button)

        self.setLayout(mein_layout)

    def on_click(self):
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
