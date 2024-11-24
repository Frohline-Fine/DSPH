import re
import pandas as pd
from pathlib import Path

from numpy import number

input_file = Path('data/data.csv')
problems = Path('data/problems.csv')
# questions_file = 'data/questions.csv'
# answers_file = 'data/answers.csv'

pattern = "Korrekte Antwort"
questions = []
answers = []


# df = pd.read_csv(input_file, encoding='utf-8', index_col=False)

def check_number(element):
    if element[0].isdigit():
        if element[1].isdigit():
            if element[2].isdigit():
                return int(element[0] + element[1] + element[2])
            return int(element[0] + element[1])
        return int(element[0])


def divide(path_to_csv: Path):
    list_of_problems = []
    exercise = []
    next_nr = 1

    df = pd.read_csv(path_to_csv, encoding='utf-8', index_col=False)

    for element in df['Question']:
        e_number = check_number(element)
        print(e_number)
        if e_number is None:
            exercise.append(element)
            print("e_number none")
        elif e_number == next_nr:
            print("e_number == next_nr")
            if len(exercise) != 0:
                list_of_problems.append(exercise)
                exercise = []
                print("problems.append & exercise.clear")
            exercise.append(element)
            next_nr += 1
            print(next_nr)
        else:
            exercise.append(element)
            print("else")

    return list_of_problems


if __name__ == '__main__':
    data_out = divide(input_file)

    data_out = pd.DataFrame(data_out)
    print(data_out)
    data_out.to_csv('data/data_out.csv')

    # elif element.startswith('Korrekte Antwort'):
    # answers.append(element)
    # elif element.startswith('Richtige Antwort'):
    #     answers.append(element)
    # elif element.startswith('Richtig'):
    #     answers.append(element)
    # elif element.startswith('Falsch'):
    #     answers.append(element)

# print(len(answers))
# print(len(questions))
# question_df = pd.DataFrame(questions)
# answer_df = pd.DataFrame(answers)
# question_df.to_csv(questions_file)
# answer_df.to_csv(answers_file)
