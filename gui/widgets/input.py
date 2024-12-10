"""

User input for audit window

"""

from PyQt6.QtWidgets import QLineEdit


class Input(QLineEdit):
    def __init__(self, parent=None):
        super(Input, self).__init__(parent)
        self.setFixedSize(760, 140)
        self.setMaxLength(10)
        self.setStyleSheet("""
                    QLineEdit {
                        background-color: rgb(245,255,250);
                        color: black;
                        border: 2px solid black;
                        border-radius: 8px;
                        padding: 20px;
                        font-family: Arial; 
                        font-size: 16px;
                    }
                    QLineEdit:focus {
                        border: 1px solid #d0e3ff;
                    }
                    QLineEdit::placeholder {
                        color: #767e89;
                    }
                """)
