"""
Provides random exercise from dataframe
"""


# get rid of unwanted characters
def cutter(string):
    cut = string.strip(r'["').strip("['").strip(r'"]')
    clean_cut = cut.replace(r"\n", "<br>")

    return clean_cut


# provide cleaned strings for QLabelWidgets
def clean_exercise(problem):
    # cleaned_problem = {'question': [], 'answer': [], 'explanation': []}
    question = cutter(str(problem[0]))
    answer = cutter(str(problem[1]))
    explanation = cutter(str(problem[2]))

    # cleaned_problem['question'].append(cutter(str(problem[0])))
    # cleaned_problem['answer'].append(cutter(str(problem[1])))
    # cleaned_problem['explanation'].append(cutter(str(problem[2])))

    return question, answer, explanation
    # return cleaned_problem
