"""

Window Result to show evaluation from exam

"""

from PyQt6.QtWidgets import QWidget, QTableWidgetItem, QLabel

from gui.layouts.evaluation import audit_result_layout
from gui.widgets.table import Table
from helper.evaluation_helper import evaluation


class ResultWindow(QWidget):
    def __init__(self, window):
        super().__init__()
        self.window = window

        self.table = Table()
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

        layout = audit_result_layout(self)
        self.setLayout(layout)
