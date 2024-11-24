import re
import pandas as pd
from pathlib import Path

i_file = Path('data/divided.csv')


def conquer(df: pd.DataFrame) -> pd.DataFrame:
    exercises = []
    # question = []
    # answer = []
    i = 0
    test = []

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
        exercise = []
        q, a = get_question(seperator, string)
        # print(q,a)
        # if re.findall("\\?", q):
        #     s_question = q.split("\\?")
        #     q = f"{s_question[0]}?"
        #     o = s_question[1]
        #     exercise.append({'option': o, })

        an, ex = get_explanation(a)

        exercise.append({'question': q, 'answer': an, 'explanation': ex})

        return exercise

    for element in df['Exercise']:
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

        exercises.append({'name': name, 'problem': problem})
        i += 1

    df = pd.DataFrame(exercises)
    return df


if __name__ == '__main__':
    df_in = pd.read_csv(i_file, encoding='utf-8', index_col=False)
    df_out = conquer(df_in)
    df_out.to_csv('data/conquer.csv')
