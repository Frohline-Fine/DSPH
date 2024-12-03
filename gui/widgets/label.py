from PyQt6.QtWidgets import QLabel


class Label(QLabel):
    def __init__(self, parent):
        super().__init__(parent)
        self.setFixedSize(760, 300)
        self.setStyleSheet("""
        color: black; background-color: rgb(245,245,245);
        padding: 20px;
        margin: 20px;
        border: 2px solid black;
        font-family: Arial; font-size: 14px; font-weight: bold;
        """)
        self.setWordWrap(True)
