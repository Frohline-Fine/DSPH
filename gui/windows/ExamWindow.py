"""

Window Exam with Timer and Scoring

"""
import sys

from PyQt6.QtCore import QTimer, Qt
from PyQt6.QtWidgets import QWidget, QApplication, QVBoxLayout, QMainWindow, QDockWidget, QListWidget

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
        self.create_side_menu()

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

    def create_side_menu(self):
        # create QDockWidget
        dock = QDockWidget("Menü", self)
        dock.setAllowedAreas(Qt.DockWidgetArea.RightDockWidgetArea)

        # create QListWidget for menu items
        menu_list = QListWidget()
        for ex in self.exercises:
            menu_list.addItem(ex[2])

        menu_list.itemClicked.connect(self.on_menu_item_clicked)

        dock.setWidget(menu_list)

        # add QDockWidget
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, dock)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ExamWindow()
    ex.show()
    sys.exit(app.exec())