"""

Window Result to show evaluation from exam

"""
# imports
from PyQt6.QtWidgets import QWidget

from helper.constants import EXAM


class ResultWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ergebnis")
        self.setFixedSize(1550, 950)
        self.setStyleSheet(f"background-color: rgb({EXAM}); margin: 20px;")
        self.dataframe = None

    def set_dataframe(self, dataframe):
        self.dataframe = dataframe
