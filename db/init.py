"""

This Class creates and fills SQLite

"""

import sqlite3

from db.init_funcs.divide_exercise import divide
from db.init_funcs.extract_text import extract
from db.init_funcs.separate_exercises import separate
from helper.constants import TABLE
from helper.paths import db_file, src_file

connection = sqlite3.connect(db_file)
cursor = connection.cursor()


def fill_table():
    # extract data from pdf and put it in dataframe
    df_page = extract(src_file)
    df_separated = separate(df_page)
    df_divided = divide(df_separated)

    try:
        with open(db_file, 'w') as f:
            df_divided.to_sql(TABLE, con=connection, if_exists='replace', index=False)
    except IOError as e:
        print(e)


def create_table():
    try:
        cursor.execute('''
            CREATE TABLE exercises (
                id INTEGER,
                spalte1 TEXT,
                spalte2 TEXT,
                spalte3 TEXT,
                spalte4 TEXT
            )
        ''')
        connection.commit()
        fill_table()
    except sqlite3.OperationalError as e:
        print(e)
