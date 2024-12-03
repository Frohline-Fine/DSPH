from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QPushButton


class Button(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.button_answer = QPushButton("Zeige Antwort")
        self.button_answer.setIconSize(QSize(16, 16))
