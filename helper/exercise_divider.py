"""
Helper functions for divide_exercises.py
"""


# separate question and answer
def get_question(seperator, string):
    words = string.split(seperator)
    qu = words[0]
    ans = f"{seperator}{words[1]}"

    return qu, ans


# separate answer and explanation
def get_explanation(string):
    words = string.split('Erklärung')
    ans = words[0]
    e = f"Erklärung{words[1]}"

    return ans, e


# split element in three parts (question, answer and explanation)
def split_element(seperator, string):
    exercise = {'question': [], 'answer': [], 'explanation': []}

    q, a = get_question(seperator, string)
    an, ex = get_explanation(a)

    exercise['question'].append(q)
    exercise['answer'].append(an)
    exercise['explanation'].append(ex)

    return exercise
