# -*- coding: utf-8 -*-
# imports
from db.init import create_table
from gui.main_gui import main_gui

if __name__ == '__main__':
    create_table()
    main_gui()
