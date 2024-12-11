"""

This class divides the exercises into individual parts

"""

import pandas as pd
from helper.strings import replace_chars, sort_by_separator
from helper.clean_exercise import clean_exercise


# split exercises into parts and update dataframe
def divide(df_in: pd.DataFrame) -> pd.DataFrame:
    exercises = []
    i = 0
    for element in df_in['Exercise']:
        name = f"Übung {i + 1}"

        str_element = str(element)
        str_element1 = replace_chars(str_element)

        problem = sort_by_separator(str_element1)
        cleaned_problem = clean_exercise(problem)

        if len(problem) > 0:
            exercises.append({'id': i,
                              'name': name,
                              'question': cleaned_problem[0],
                              'answer': cleaned_problem[1],
                              'explanation': cleaned_problem[2],
                              })
        print(f"Übung {i + 1} bearbeitet")
        i += 1

    df_out = pd.DataFrame(exercises)

    print("exercises divided")

    return df_out
