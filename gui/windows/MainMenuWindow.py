"""

Window Main

"""

from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QMainWindow, QWidget

from gui.layouts.main_window import main_layout
from gui.widgets.button import Button
from gui.windows.ExamMainWindow import ExamWindow
from gui.windows.TrainingTranslatedWindow import TrainingEngWindow
from gui.windows.TrainingWindow import TrainingWindow
from helper.constants import MAIN, BTN_TRAINING, BTN_EXAM, BTN_TRAINING_E, BTN_EXIT


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hauptmenü")
        self.setFixedSize(600, 600)
        self.setStyleSheet(f"background-color: {MAIN};")

        # Create buttons
        self.btn_training = Button(BTN_TRAINING)
        self.btn_training.setFixedSize(QSize(400, 100))

        self.btn_training_e = Button(BTN_TRAINING_E)
        self.btn_training_e.setFixedSize(QSize(400, 100))

        self.btn_exam = Button(BTN_EXAM)
        self.btn_exam.setFixedSize(QSize(400, 100))

        self.btn_exit = Button(BTN_EXIT)
        self.btn_exit.setFixedSize(QSize(400, 100))

        self.btn_training.clicked.connect(self.open_training)
        self.btn_training_e.clicked.connect(self.open_training_english)
        self.btn_exam.clicked.connect(self.open_exam)
        self.btn_exit.clicked.connect(self.close)

        layout = main_layout(self)

        # Create central widget
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def open_training(self):
        self.training_window = TrainingWindow()
        self.training_window.show()

    def open_training_english(self):
        try:
            self.training_eng_window = TrainingEngWindow()
            self.training_eng_window.show()
        except Exception as e:
            print(e)

    def open_exam(self):
        self.exam_window = ExamWindow()
        self.exam_window.show()
