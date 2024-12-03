import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QMainWindow, QPushButton, QApplication, QVBoxLayout, QWidget

from gui.widgets.button import Button
from gui.windows.TrainingWindow import TrainingWindow
from helper.constants import MAIN, BTN_TRAINING, BTN_EXAM, BTN_TRAINING_E, BTN_EXIT


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hauptmenü")
        self.setFixedSize(600, 600)
        self.setStyleSheet(f"background-color: rgb({MAIN});")

        self.button = QPushButton(BTN_TRAINING)
        self.button.clicked.connect(self.open_training)
        self.setCentralWidget(self.button)

        # Erstellen der Buttons
        self.btn_training = Button(BTN_TRAINING)
        self.btn_training.setFixedSize(QSize(400, 100))

        self.btn_training_e = Button(BTN_TRAINING_E)
        self.btn_training_e.setFixedSize(QSize(400, 100))

        self.btn_exam = Button(BTN_EXAM)
        self.btn_exam.setFixedSize(QSize(400, 100))

        self.btn_exit = Button(BTN_EXIT)
        self.btn_exit.setFixedSize(QSize(400, 100))

        # Verbinden der Buttons mit Funktionen
        self.btn_training.clicked.connect(self.open_training)
        self.btn_training_e.clicked.connect(self.open_training_english)
        self.btn_exam.clicked.connect(self.open_exam)
        self.btn_exit.clicked.connect(self.exit_program)

        # Layout erstellen und Buttons hinzufügen
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.btn_training)
        layout.addWidget(self.btn_training_e)
        layout.addWidget(self.btn_exam)
        layout.addWidget(self.btn_exit)

        # Zentrales Widget erstellen und Layout zuweisen
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def open_training(self):
        self.training_window = TrainingWindow()
        self.training_window.show()

    def open_training_english(self):
        pass

    def open_exam(self):
        pass

    def exit_program(self):
        pass


def main():
    app = QApplication(sys.argv)
    main_dialog = MainWindow()
    main_dialog.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
