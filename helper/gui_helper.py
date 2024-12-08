"""

Helper functions for GUI

"""
# imports
import random

import pandas as pd

from db.init import cursor
from helper.constants import TABLE
from helper.strings import sort_answers_for_exam


# combine answer and explanation for Label
def concat(answer, explanation):
    return answer + '<br>' + explanation


# provide random item from database
def random_exercise():
    i = random.randint(0, 799)
    query = f"SELECT * FROM {TABLE} WHERE id = {i}"
    exercise = cursor.execute(query).fetchone()

    return exercise


# create collection of 80 random questions for exam
def create_tasks():
    tasks = []

    for i in range(80):
        tasks.append(random_exercise())

    return tasks


# create dataframe exercises for ExamWindow
def create_exam():
    tasks = create_tasks()
    exam = []

    for i, task in enumerate(tasks):
        exam.append({
            'question': task[2],
            'correct_answer': sort_answers_for_exam(task[3]),
            'user_answer': [],
        })

    df_exam = pd.DataFrame(exam)
    return df_exam

