"""

This Class separates the exercises and gets rid of unimportant text

"""
# imports
import pandas as pd


# determine exercise number
def check_number(element) -> int:
    if element[0].isdigit():
        if element[1].isdigit():
            if element[2].isdigit():
                return int(element[0] + element[1] + element[2])
            return int(element[0] + element[1])
        return int(element[0])


# separate exercises from each other
def separate(df_in: pd.DataFrame) -> pd.DataFrame:
    list_of_problems = []
    exercise = []
    next_nr = 1

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

    print("exercises separated")

    return df_out
