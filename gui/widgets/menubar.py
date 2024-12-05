"""

Menubar for Exam mode

"""
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QDockWidget, QListWidget


def create_side_menu(self):
    # create QDockWidget
    dock = QDockWidget("Menü", self)
    dock.setAllowedAreas(Qt.DockWidgetArea.LeftDockWidgetArea)

    # create QListWidget for menu items
    menu_list = QListWidget()
    for ex in self.exercises:
        menu_list.addItem(ex[2])

    menu_list.itemClicked.connect(self.on_menu_item_clicked)

    dock.setWidget(menu_list)

    # add QDockWidget to exam window
    self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, dock)
    #
    # return dock
