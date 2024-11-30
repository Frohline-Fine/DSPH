"""
This class divides the exercises into individual parts
"""
# imports
import re
import pandas as pd
from helper.exercise_divider import split_element, replace_chars
from helper.constants import CORRECT, R_ANSWERS, R_ANSWER, RIGHT, WRONG


# split exercises into parts and update dataframe
def divide(df_in: pd.DataFrame) -> pd.DataFrame:
    exercises = []
    i = 0

    for element in df_in['Exercise']:
        name = f"Übung {i + 1}"
        problem = {'question': [], 'answer': [], 'explanation': []}

        str_element = str(element)
        str_element1 = replace_chars(str_element)

        if re.findall(CORRECT, str_element1):
            problem = split_element(CORRECT, str_element1)
        elif re.findall(R_ANSWERS, str_element1):
            problem = split_element(R_ANSWERS, str_element1)
        elif re.findall(R_ANSWER, str_element1):
            problem = split_element(R_ANSWER, str_element1)
        elif re.findall(RIGHT, str_element1):
            problem = split_element(RIGHT, str_element1)
        elif re.findall(WRONG, str_element1):
            problem = split_element(WRONG, str_element1)

        if len(problem) > 0:
            exercises.append({'name': name,
                              'question': problem['question'],
                              'answer': problem['answer'],
                              'explanation': problem['explanation']})
        i += 1

    df_out = pd.DataFrame(exercises)

    print("exercises divided")

    return df_out
