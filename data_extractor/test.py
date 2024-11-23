import re
import pandas as pd

input_file = 'data.csv'
i = 1
pattern = r"[0-9]+\."
questions = []

df = pd.read_csv(input_file, encoding='utf-8', index_col=False)

question = []

for element in df['Question']:
    if element[0].isdigit():
        print(element)
    # else:
    #     print(element)


# print(len(questions))
# df2 = pd.DataFrame(questions)
# print(df2)
