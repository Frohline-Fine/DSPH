"""

Window Exam with Timer and Scoring

"""
import sys

from PyQt6.QtCore import QTimer, Qt
from PyQt6.QtWidgets import QWidget, QApplication, QVBoxLayout, QMainWindow

from gui.widgets.label import Label
from gui.widgets.menubar import create_side_menu
from helper.constants import EXAM
from helper.gui_helper import create_exam


class ExamWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.setWindowTitle("Prüfungssimulation")
        self.setFixedSize(1050, 950)
        self.setStyleSheet(f"background-color: rgb({EXAM}); margin: 20px;")
        self.exercises = create_exam()
        self.dock = create_side_menu(self)

        self.score = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.stop_exam)

        self.question = Label(self)
        self.question.setText(self.exercises[0][2])

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignRight)
        layout.addWidget(self.question)

        self.setLayout(layout)

    def stop_exam(self):
        pass

    def on_menu_item_clicked(self, item):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ExamWindow()
    ex.show()
    sys.exit(app.exec())
