"""

Menubar for Exam mode

"""

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QDockWidget, QListWidget, QWidget, QMenuBar, QListWidgetItem

from helper.constants import LABEL


def create_side_menu(self):
    # create QDockWidget
    self.dock = QDockWidget("Menü", self)
    self.dock.setAllowedAreas(Qt.DockWidgetArea.LeftDockWidgetArea)
    self.dock.setTitleBarWidget(QWidget())
    self.dock.setStyleSheet(f"""
            background-color: rgb(245,255,250);
            margin: 20px;
            padding: 10px;
            border: 2px solid black;
            border-radius: 8px;
            font-family: Arial; font-size: 14px;                      
            """)

    # create QListWidget for menu items
    self.menu_list = QListWidget()
    for index, row in self.exercises.iterrows():
        qu = QListWidgetItem(str(row['question']))
        self.menu_list.addItem(qu)

    self.menu_list.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
    self.menu_list.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
    self.menu_list.itemClicked.connect(self.on_menu_item_clicked)

    self.dock.setWidget(self.menu_list)

    # add QDockWidget to exam window
    self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.dock)

    # return self.dock
