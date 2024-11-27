"""
This class divides the exercises into individual parts
"""
import re
import pandas as pd


def divide(df_in: pd.DataFrame) -> pd.DataFrame:
    exercises = []
    i = 0

    def get_question(seperator, string):
        words = string.split(seperator)
        qu = words[0]
        ans = f"{seperator}{words[1]}"
        return qu, ans

    def get_explanation(string):
        words = string.split('Erklärung')
        ans = words[0]
        e = f"Erklärung{words[1]}"
        return ans, e

    def split_element(seperator, string):
        exercise = {'question': [], 'answer': [], 'explanation': []}
        q, a = get_question(seperator, string)
        an, ex = get_explanation(a)

        exercise['question'].append(q)
        exercise['answer'].append(an)
        exercise['explanation'].append(ex)

        return exercise

    for element in df_in['Exercise']:
        name = f"Exercise {i + 1}"
        problem = []

        str_element = str(element)
        str_element1 = str_element.replace("', '", ' ')

        if re.findall('Korrekte Antwort', str_element1):
            problem = split_element('Korrekte Antwort', str_element1)
        elif re.findall('Richtige Antworten', str_element1):
            problem = split_element('Richtige Antworten', str_element1)
        elif re.findall('Richtige Antwort', str_element1):
            problem = split_element('Richtige Antwort', str_element1)
        elif re.findall('Richtig', str_element1):
            problem = split_element('Richtig', str_element1)
        elif re.findall('Falsch', str_element1):
            problem = split_element('Falsch', str_element1)

        if len(problem) > 0:
            exercises.append({'name': name,
                              'question': problem['question'],
                              'answer': problem['answer'],
                              'explanation': problem['explanation']})
        i += 1

    df_out = pd.DataFrame(exercises)

    print("exercises divided")

    return df_out
