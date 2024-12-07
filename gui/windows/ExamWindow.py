"""

Window Exam with Timer and Scoring

"""
import sys

from PyQt6.QtCore import QTimer, Qt
from PyQt6.QtWidgets import QWidget, QApplication, QVBoxLayout, QMainWindow, QLineEdit

from gui.widgets.label import Label
from gui.widgets.menubar import create_side_menu
from helper.constants import EXAM
from helper.gui_helper import create_exam
from helper.strings import sort_answers_for_exam


class ExamWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.setWindowTitle("Prüfungssimulation")
        self.setFixedSize(1000, 900)
        self.setStyleSheet(f"background-color: rgb({EXAM}); margin: 20px;")

        self.exercises = create_exam()
        self.dock = create_side_menu(self)

        self.score = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.stop_exam)

        self.question = Label(self)
        self.question.setText(self.exercises[0][2])

        self.answer = QLineEdit()
        self.answer.setText(self.exercises[0][3])
        self.answer.setMaxLength(10)
        self.answer.returnPressed.connect(self.set_answer)

        # self.answer = Label(self)
        # self.answer.setText(sort_answers_for_exam(self.exercises[0][3]))

        layout = QVBoxLayout()
        layout.addWidget(self.question)
        layout.addWidget(self.answer)

        central_widget.setLayout(layout)

    def set_answer(self):
        pass

    def stop_exam(self):
        pass

    def on_menu_item_clicked(self, item):
        pass


def main():
    app = QApplication(sys.argv)
    ex = ExamWindow()
    ex.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
