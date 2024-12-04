from PyQt6.QtWidgets import QLabel

from helper.constants import LABEL


class Label(QLabel):
    def __init__(self, parent):
        super().__init__(parent)
        self.setFixedSize(760, 300)
        self.setStyleSheet(f"""
        color: black; background-color: rgb({LABEL});
        padding: 20px;
        margin: 20px;
        border: 2px solid black;
        font-family: Arial; font-size: 14px; font-weight: bold;
        """)
        self.setWordWrap(True)