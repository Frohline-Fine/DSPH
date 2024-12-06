"""

Helper functions for GUI

"""
# imports
import random

from db.init import cursor
from helper.constants import TABLE


# combine answer and explanation for Label
def concat(answer, explanation):
    return answer + '<br>' + explanation


# provide random item from database
def random_exercise():
    i = random.randint(0, 799)
    query = f"SELECT * FROM {TABLE} WHERE id = {i}"
    exercise = cursor.execute(query).fetchone()

    return exercise


# create collection of questions for exam
def create_exam():
    exam = []

    for i in range(80):
        exam.append(random_exercise())

    return exam
