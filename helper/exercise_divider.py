"""
Helper functions for divide_exercise.py
"""


def replace_chars(str_element):
    str_element1 = str_element.replace("', '", " ")
    str_element2 = str_element1.replace(r"\'", "'")
    str_element3 = str_element2.replace("', \"", "")
    str_element4 = str_element3.replace("\",'", "")
    str_element5 = str_element4.replace('", "', "")
    str_element6 = str_element5.replace("\", '", "")

    return str_element6


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
    q, a = get_question(seperator, string)
    an, ex = get_explanation(a)

    return q, an, ex
