"""
Helper for GUI
"""
# imports
import random
from db.init_db import collection


def random_exercise():
    id = random.randint(0, 799)

    exercise = collection.find_one({'id': id})

    return exercise
