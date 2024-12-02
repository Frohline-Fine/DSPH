"""
Helper for GUI
"""
# imports
import random

from db.init import cursor
from helper.constants import TABLE


def random_exercise():
    id = random.randint(0, 799)
    query = f"SELECT * FROM {TABLE} WHERE id = {id}"

    exercise = cursor.execute(query).fetchone()

    return exercise
