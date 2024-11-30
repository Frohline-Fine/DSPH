# -*- coding: utf-8 -*-
# imports
import sys

from PyQt6.QtWidgets import QApplication

from db.init_db import client, init_db
from gui.test_gui import TrainDialog
from helper.constants import DB_NAME

if __name__ == '__main__':
    if DB_NAME not in client.list_database_names():
        print("Datenbank wird erstellt")
        init_db()

    app = QApplication(sys.argv)
    main_dialog = TrainDialog()
    main_dialog.show()
    sys.exit(app.exec())
