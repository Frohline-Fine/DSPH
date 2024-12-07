"""

Window Exam with Timer and Scoring

"""
import sys

from PyQt6.QtCore import QTimer, Qt, QTime
from PyQt6.QtWidgets import QWidget, QApplication, QVBoxLayout, QMainWindow, QLineEdit, QHBoxLayout, QLabel

from gui.widgets.button import Button
from gui.widgets.input import Input
from gui.widgets.label import Label
from gui.widgets.menubar import create_side_menu
from helper.constants import EXAM, BTN_BACK, BTN_NEXT
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

        self.display_timer = QTimer()
        self.display_timer.timeout.connect(self.update_display)
        self.display_timer.start(100)  # Aktualisiert alle 100 ms

        self.timer = QTimer()
        self.timer.setSingleShot(True)
        self.timer.start(3600000)
        self.timer.timeout.connect(self.stop_exam)

        self.label_time = Label(self)
        self.label_time.setFixedSize(300, 100)
        self.label_time.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.question = Label(self)
        self.question.setText(self.exercises[0][2])

        self.answer = Input()
        self.answer.setText(self.exercises[0][3])
        self.answer.returnPressed.connect(self.set_answer)

        self.btn_back = Button(self)
        self.btn_back.setText(BTN_BACK)
        self.btn_back.clicked.connect(self.backward)

        self.btn_next = Button(self)
        self.btn_next.setText(BTN_NEXT)
        self.btn_next.clicked.connect(self.forward)

        btn_layout = QHBoxLayout()
        btn_layout.addWidget(self.btn_back)
        btn_layout.addWidget(self.btn_next)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        layout.addWidget(self.label_time)
        layout.addWidget(self.question)
        layout.addWidget(self.answer)
        layout.addLayout(btn_layout)

        central_widget.setLayout(layout)

    def update_display(self):
        restzeit = self.timer.remainingTime()
        zeit = QTime(0, 0).addMSecs(restzeit)
        zeit_string = zeit.toString("mm:ss")
        self.label_time.setText(zeit_string)

    def backward(self):
        pass

    def forward(self):
        pass

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
