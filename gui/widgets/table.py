"""

Table for exam results

"""

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QTableWidget

from helper.constants import TABLE_WIDGET, FONT_LABEL


class Table(QTableWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet(f"""
            background-color: {TABLE_WIDGET};
            margin: 20px;
            padding: 10px;
            border: 2px solid black;
            border-radius: 8px;
            font-family: {FONT_LABEL}; font-size: 14px;   
        """)
        self.column_percentages = 70, 15, 15
        self.horizontalHeader().setVisible(False)
        self.verticalHeader().setVisible(False)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.adjust_column_widths()

    def adjust_column_widths(self):
        if not self.column_percentages:
            return

        total_width = self.viewport().width()
        for col, percentage in enumerate(self.column_percentages):
            width = int(total_width * percentage / 100)
            self.setColumnWidth(col, width)
