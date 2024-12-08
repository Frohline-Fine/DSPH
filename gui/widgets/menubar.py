"""

Menubar for Exam mode

"""
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QDockWidget, QListWidget, QWidget, QMenuBar, QListWidgetItem

from helper.constants import LABEL


def create_side_menu(self):
    # create QDockWidget
    dock = QDockWidget("Menü", self)
    dock.setAllowedAreas(Qt.DockWidgetArea.LeftDockWidgetArea)
    dock.setTitleBarWidget(QWidget())
    dock.setStyleSheet(f"""
            background-color: rgb(245,255,250);
            margin: 20px;
            padding: 10px;
            border: 2px solid black;
            border-radius: 8px;
            font-family: Arial; font-size: 14px;                      
            """)

    # create QListWidget for menu items
    menu_list = QListWidget()
    for index, row in self.exercises.iterrows():
        qu = QListWidgetItem(str(row['question']))
        menu_list.addItem(qu)

    menu_list.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
    menu_list.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
    menu_list.itemClicked.connect(self.on_menu_item_clicked)

    dock.setWidget(menu_list)

    # add QDockWidget to exam window
    self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, dock)

    return dock
