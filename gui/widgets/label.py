from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QLabel


class Label(QLabel):
    def __init__(self, parent):
        super().__init__(parent)
        self.setFixedSize(700, 400)
        self.setStyleSheet("""
        color: black; background-color: white;
        spacing: 100,100, 100, 100;
        margin: 20px;
        border: 2px solid black;
        font-family: Arial; font-size: 14px; font-weight: bold;
        """)
        self.setWordWrap(True)
