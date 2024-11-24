import re
from operator import index

import pandas as pd
from pathlib import Path

input_file = Path('data/cleaned_datei.csv')
problems = Path('data/problems.csv')

pattern = "Korrekte Antwort"
questions = []
answers = []


def check_number(element) -> int:
    if element[0].isdigit():
        if element[1].isdigit():
            if element[2].isdigit():
                return int(element[0] + element[1] + element[2])
            return int(element[0] + element[1])
        return int(element[0])


def divide(path_to_csv: Path) -> pd.DataFrame:
    list_of_problems = []
    exercise = []
    next_nr = 1

    df_in = pd.read_csv(path_to_csv, encoding='utf-8', index_col=False)

    for element in df_in['Question']:
        e_number = check_number(element)
        if e_number is None:
            exercise.append(element)
        elif e_number == next_nr:
            if len(exercise) != 0:
                x = {'Exercise': exercise}
                list_of_problems.append(x)
                exercise = []
            exercise.append(element)
            next_nr += 1
        else:
            exercise.append(element)

    list_of_problems.append({'Exercise': exercise})
    list_of_problems.pop(0)
    df_out = pd.DataFrame(list_of_problems)
    return df_out


if __name__ == '__main__':
    df_divided = divide(input_file)
    df_divided.to_csv('data/divided.csv', encoding='utf-8', index=False)
