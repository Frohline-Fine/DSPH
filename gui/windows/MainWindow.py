import sys

from PyQt6.QtWidgets import QMainWindow, QPushButton, QApplication

from gui.windows.TrainingWindow import TrainingWindow
from helper.constants import MAIN


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hauptmenü")
        self.setFixedSize(1440, 800)
        self.setStyleSheet(f"background-color: rgb({MAIN});")

        self.button = QPushButton("Öffne zweites Fenster")
        self.button.clicked.connect(self.open_second_window)
        self.setCentralWidget(self.button)

    def open_second_window(self):
        self.second_window = TrainingWindow()
        self.second_window.show()


def main():
    app = QApplication(sys.argv)
    main_dialog = MainWindow()
    main_dialog.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
