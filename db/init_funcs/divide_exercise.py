"""
This class divides the exercises into individual parts
"""
# imports
import re
import pandas as pd
from helper.exercise_divider import split_element, replace_chars
from db.init_funcs.clean_exercise import clean_exercise
from helper.constants import CORRECT, R_ANSWERS, R_ANSWER, RIGHT, WRONG, SOLUTION
from helper.translator import translate


# split exercises into parts and update dataframe
def divide(df_in: pd.DataFrame) -> pd.DataFrame:
    exercises = []
    i = 0

    for element in df_in['Exercise']:
        name = f"Übung {i + 1}"
        problem = []

        str_element = str(element)
        str_element1 = replace_chars(str_element)

        if re.findall(CORRECT, str_element1):
            problem = split_element(CORRECT, str_element1)
        elif re.findall(R_ANSWERS, str_element1):
            problem = split_element(R_ANSWERS, str_element1)
        elif re.findall(R_ANSWER, str_element1):
            problem = split_element(R_ANSWER, str_element1)
        elif re.findall(SOLUTION, str_element):
            problem = split_element(SOLUTION, str_element)
        elif re.findall(RIGHT, str_element1):
            problem = split_element(RIGHT, str_element1)
        elif re.findall(WRONG, str_element1):
            problem = split_element(WRONG, str_element1)

        cleaned_problem = clean_exercise(problem)

        if len(problem) > 0:
            exercises.append({'id': i,
                              'name': name,
                              'question': cleaned_problem[0],
                              'question_e': translate(cleaned_problem[0]),
                              'answer': cleaned_problem[1],
                              'explanation': cleaned_problem[2],
                              'explanation_e': translate(cleaned_problem[2]),
                              })
        print(f"Übung {i} bearbeitet")
        i += 1

    df_out = pd.DataFrame(exercises)

    print("exercises divided")

    return df_out
