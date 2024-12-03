"""
Hauptfunktion GUI
"""
import sys

from PyQt6.QtWidgets import QApplication

from gui.windows.MainWindow import MainWindow


def main_gui():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
