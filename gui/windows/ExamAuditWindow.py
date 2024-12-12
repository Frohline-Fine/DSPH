"""

Window Audit for exam

"""

from PyQt6.QtCore import QTimer, Qt, QTime
from PyQt6.QtWidgets import QWidget

from gui.layouts.exam_window import exam_layout
from gui.widgets.button import Button
from gui.widgets.input import Input
from gui.widgets.label import Label
from helper.constants import BTN_BACK, BTN_NEXT, BTN_STOP


class AuditWindow(QWidget):
    def __init__(self, window):
        super().__init__()
        self.window = window
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
        self.question.setText(self.window.exercises.loc[self.window.index, 'question'])

        self.answer = Input()
        self.answer.returnPressed.connect(self.set_answer)

        self.btn_stop = Button(self)
        self.btn_stop.setText(BTN_STOP)
        self.btn_stop.clicked.connect(self.stop_exam)

        self.btn_back = Button(self)
        self.btn_back.setText(BTN_BACK)
        self.btn_back.clicked.connect(self.backward)

        self.btn_next = Button(self)
        self.btn_next.setText(BTN_NEXT)
        self.btn_next.clicked.connect(self.forward)

        layout = exam_layout(self)
        self.setLayout(layout)

    def update_display(self):
        rem_time = self.timer.remainingTime()
        time = QTime(0, 0).addMSecs(rem_time)
        string_time = time.toString("mm:ss")
        self.label_time.setText(string_time)

    def update_question(self):
        if not self.window.exercises.empty:
            current_question = self.window.exercises.loc[self.window.index, 'question']
            self.question.setText(current_question)

    def backward(self):
        self.set_answer()
        if self.window.index > 0:
            self.window.index -= 1
            self.update_question()

    def forward(self):
        self.set_answer()
        if self.window.index < len(self.window.exercises) - 1:
            self.window.index += 1
            self.update_question()

    def set_answer(self):
        if len(self.answer.text()) > 0:
            self.window.exercises.loc[self.window.index, 'user_answer'] = self.answer.text()

    def stop_exam(self):
        try:
            self.window.stop_exam()
        except Exception as e:
            print(e)
