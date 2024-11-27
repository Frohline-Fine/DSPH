"""
This class divides the exercises into individual parts
"""
# imports
import re
import pandas as pd

# constants
CORRECT = 'Korrekte Antwort'
R_ANSWERS = 'Richtige Antworten'
R_ANSWER = 'Richtige Antwort'
RIGHT = 'Richtig'
WRONG = 'Falsch'


# separate question and answer
def get_question(seperator, string):
    words = string.split(seperator)
    qu = words[0]
    ans = f"{seperator}{words[1]}"

    return qu, ans


# separate answer and explanation
def get_explanation(string):
    words = string.split('Erklärung')
    ans = words[0]
    e = f"Erklärung{words[1]}"

    return ans, e


# split element in three parts (question, answer and explanation)
def split_element(seperator, string):
    exercise = {'question': [], 'answer': [], 'explanation': []}

    q, a = get_question(seperator, string)
    an, ex = get_explanation(a)

    exercise['question'].append(q)
    exercise['answer'].append(an)
    exercise['explanation'].append(ex)

    return exercise


def divide(df_in: pd.DataFrame) -> pd.DataFrame:
    exercises = []
    i = 0

    for element in df_in['Exercise']:
        name = f"Übung {i + 1}"
        problem = []

        str_element = str(element)
        str_element1 = str_element.replace("', '", ' ')

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
