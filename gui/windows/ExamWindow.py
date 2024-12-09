"""

Window Exam with Timer and Scoring

"""
import sys

from PyQt6.QtCore import QTimer, Qt, QTime
from PyQt6.QtWidgets import QWidget, QApplication, QVBoxLayout, QMainWindow, QHBoxLayout

from gui.layouts.exam_window import exam_layout
from gui.widgets.button import Button
from gui.widgets.input import Input
from gui.widgets.label import Label
from gui.widgets.menubar import create_side_menu
from gui.windows import ResultWindow
from helper.constants import EXAM, BTN_BACK, BTN_NEXT
from helper.gui_helper import create_exam


class ExamWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.setWindowTitle("Prüfungssimulation")
        self.setFixedSize(1000, 900)
        self.setStyleSheet(f"background-color: rgb({EXAM}); margin: 20px;")

        self.exercises = create_exam()
        self.index = 0
        self.menu = create_side_menu(self)

        self.display_timer = QTimer()
        self.display_timer.timeout.connect(self.update_display)
        self.display_timer.start(100)  # Update every 100 ms

        self.timer = QTimer()
        self.timer.setSingleShot(True)
        self.timer.start(3600000)
        self.timer.timeout.connect(self.stop_exam)

        self.label_time = Label(self)
        self.label_time.setFixedSize(300, 100)
        self.label_time.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.question = Label(self)
        self.question.setText(self.exercises.loc[self.index, 'question'])

        self.answer = Input()
        self.answer.returnPressed.connect(self.set_answer)

        self.btn_back = Button(self)
        self.btn_back.setText(BTN_BACK)
        self.btn_back.clicked.connect(self.backward)

        self.btn_next = Button(self)
        self.btn_next.setText(BTN_NEXT)
        self.btn_next.clicked.connect(self.forward)

        layout = exam_layout()
        central_widget.setLayout(layout)

    def update_display(self):
        rem_time = self.timer.remainingTime()
        time = QTime(0, 0).addMSecs(rem_time)
        string_time = time.toString("mm:ss")
        self.label_time.setText(string_time)

    def update_question(self):
        if not self.exercises.empty:
            current_question = self.exercises.loc[self.index, 'question']
            self.question.setText(current_question)

    def backward(self):
        self.set_answer()
        if self.index > 0:
            self.index -= 1
            self.update_question()

    def forward(self):
        self.set_answer()
        if self.index < len(self.exercises) - 1:
            self.index += 1
            self.update_question()

    def set_answer(self):
        if len(self.answer.text()) > 0:
            self.exercises.loc[self.index, 'user_answer'] = self.answer.text()

    def on_menu_item_clicked(self, item):
        self.set_answer()
        self.index = self.menu_list.row(item)
        self.update_question()

    def stop_exam(self):
        self.result_window = ResultWindow()
        self.result_window.set_dataframe(self.exercises)
        self.result_window.show()


def main():
    app = QApplication(sys.argv)
    ex = ExamWindow()
    ex.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
