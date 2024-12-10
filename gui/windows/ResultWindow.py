"""

Window Result to show evaluation from exam

"""
# imports
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QLabel, QHBoxLayout

from helper.evaluation_helper import evaluation


class ResultWindow(QWidget):
    def __init__(self, window):
        super().__init__()
        self.window = window

        self.table = QTableWidget()
        self.table.setRowCount(len(self.window.exercises))
        self.table.setColumnCount(len(self.window.exercises.columns))

        for row in range(0, len(self.window.exercises)):
            for column in range(0, len(self.window.exercises.columns)):
                self.table.setItem(row,
                                   column,
                                   QTableWidgetItem(str(self.window.exercises.iloc[row, column])))

        self.correct = evaluation(self.window.exercises)

        self.correct_count = QLabel(self)
        self.correct_count.setText(f"Richtige Antworten: {self.correct[0]}")

        self.accuracy = QLabel(self)
        self.accuracy.setText(f"Genauigkeit: {self.correct[1]}%")

        h_layout = QHBoxLayout()
        h_layout.addWidget(self.correct_count)
        h_layout.addWidget(self.accuracy)

        layout = QVBoxLayout()
        layout.addWidget(self.table)
        layout.addLayout(h_layout)
        self.setLayout(layout)
