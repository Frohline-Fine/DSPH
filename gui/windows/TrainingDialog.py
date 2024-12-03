"""
Window Training: Solve random questions - no strings attached
"""
import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel, QWidget, QVBoxLayout, QHBoxLayout

from gui.widgets.label import Label
from helper.gui_helper import random_exercise


class TrainDialog(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Training")
        self.setFixedSize(1440, 800)
        self.setStyleSheet("background-color: rgb(185,211,238);")
        self.exercise = random_exercise()

        self.question = Label(self)
        self.question.setText(self.exercise[2])

        self.explanation = Label(self)
        self.explanation.setText(self.exercise[4])

        label_layout = QHBoxLayout()
        label_layout.addWidget(self.question)
        label_layout.addWidget(self.explanation)

        main_layout = QVBoxLayout()
        main_layout.addLayout(label_layout)

        self.setLayout(main_layout)


def test_gui():
    app = QApplication(sys.argv)
    main_dialog = TrainDialog()
    main_dialog.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    test_gui()
