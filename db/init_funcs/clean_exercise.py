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
    question = cutter(str(problem[0]))
    answer = cutter(str(problem[1]))
    explanation = cutter(str(problem[2]))

    return question, answer, explanation
