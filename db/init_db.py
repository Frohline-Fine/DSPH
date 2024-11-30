"""
This Class creates and fills Mongo DB
"""
# imports
from pymongo import MongoClient
from pymongoarrow.api import write

from db.init_funcs.extract_data import extract_data
from db.init_funcs.separate_exercises import separate
from db.init_funcs.divide_exercise import divide
from helper.constants import DB_NAME, COLLECTION

# create db connection
client = MongoClient('mongodb://localhost:27017/')

# create db and collection
db = client[DB_NAME]
collection = db[COLLECTION]


def init_db():
    # extract data from pdf and put it in dataframe
    df_page = extract_data()
    df_separated = separate(df_page)
    df_divided = divide(df_separated)

    # add dataframe to db
    write(db.exercises, df_divided)
