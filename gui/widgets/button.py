from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QPushButton


class Button(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(QSize(200, 100))
        self.setStyleSheet("""
        color: black; background-color: rgb(245, 245, 245);
        padding: 10px;
        margin: 20px;
        border: 2px solid black;
        font-family: Arial; font-size: 14px; font-weight: bold;
        """)
