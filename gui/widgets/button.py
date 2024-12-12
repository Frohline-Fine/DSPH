"""

Buttons for GUI

"""

from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QPushButton

from helper.constants import BUTTON_BG, FONT_BTN


class Button(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(QSize(200, 100))
        self.setStyleSheet(f"""
        color: black; background-color: {BUTTON_BG};
        padding: 10px;
        margin: 20px;
        border: 2px solid black;
        border-radius: 8px;
        font-family: {FONT_BTN}; font-size: 14px; font-weight: bold;
        """)
