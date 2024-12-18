"""

Labels for GUI

"""

from PyQt6.QtWidgets import QLabel

from helper.constants import LABEL, FONT_LABEL


class Label(QLabel):
    def __init__(self, parent):
        super().__init__(parent)
        self.setFixedSize(760, 450)
        self.setStyleSheet(f"""
            color: black; background-color: {LABEL};
            padding: 20px;
            margin: 20px;
            border: 2px solid black;
            border-radius: 8px;
            font-family: {FONT_LABEL}; font-size: 16px;
        """)
        self.setWordWrap(True)
