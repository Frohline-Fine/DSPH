"""

Window Exam with Timer and Scoring

"""
import sys

from PyQt6.QtWidgets import QWidget, QApplication, QMainWindow

from gui.widgets.menubar import create_side_menu
from gui.windows.AuditWindow import AuditWindow
from gui.windows.ResultWindow import ResultWindow
from helper.constants import EXAM
from helper.gui_helper import create_exam


class ExamWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.audit_results = None
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.setWindowTitle("Prüfungssimulation")
        self.setFixedSize(1000, 900)
        self.setStyleSheet(f"background-color: rgb({EXAM}); margin: 20px;")

        self.exercises = create_exam()
        self.index = 0
        self.menu = create_side_menu(self)

        self.audit_window = AuditWindow(self)
        self.change_central_widget(self.audit_window)

    def change_central_widget(self, new_widget):
        current_widget = self.centralWidget()
        if current_widget:
            current_widget.setParent(None)
        self.setCentralWidget(new_widget)

    def on_menu_item_clicked(self, item):
        self.audit_window.set_answer()
        self.index = self.menu_list.row(item)
        self.audit_window.update_question()

    def stop_exam(self):
        self.audit_results = ResultWindow(self)
        self.change_central_widget(self.audit_results)


def main():
    app = QApplication(sys.argv)
    ex = ExamWindow()
    ex.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
