# -*- coding: utf-8 -*-
# imports
import sys

from PyQt6.QtWidgets import QApplication

from db.init import create_table
from gui.test_gui import TrainDialog

if __name__ == '__main__':
    create_table()

    app = QApplication(sys.argv)
    main_dialog = TrainDialog()
    main_dialog.show()
    sys.exit(app.exec())
