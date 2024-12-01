"""
Provides random exercise from dataframe
"""


# get rid of unwanted characters
def cutter(string):
    cut = string.strip(r'["').strip("['").strip(r'"]')
    clean_cut = cut.replace(r"\\n", "<br>")

    return clean_cut


# provide cleaned strings for QLabelWidgets
def clean_exercise(problem):
    cleaned_problem = {'question': [], 'answer': [], 'explanation': []}

    cleaned_problem['question'].append(cutter(str(problem['question'])))
    cleaned_problem['answer'].append(cutter(str(problem['answer'])))
    cleaned_problem['explanation'].append(cutter(str(problem['explanation'])))

    return cleaned_problem
