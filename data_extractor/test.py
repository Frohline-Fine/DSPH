import re
import pandas as pd


input_file = 'data.csv'
questions_file = 'questions.csv'
answers_file = 'answers.csv'

pattern = "Korrekte Antwort"
questions = []
answers = []

df = pd.read_csv(input_file, encoding='utf-8', index_col=False)

for element in df['Question']:
    if element[0].isdigit():
        questions.append(element)
    elif element.startswith('Korrekte Antwort'):
        answers.append(element)
    elif element.startswith('Richtige Antwort'):
        answers.append(element)
    elif element.startswith('Richtig'):
        answers.append(element)
    elif element.startswith('Falsch'):
        answers.append(element)

print(len(answers))
question_df = pd.DataFrame(questions)
answer_df = pd.DataFrame(answers)
question_df.to_csv(questions_file)
answer_df.to_csv(answers_file)

