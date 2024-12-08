"""

Helper functions for String objects

"""
import re

from helper.constants import CORRECT, R_ANSWERS, R_ANSWER, SOLUTION, RIGHT, WRONG


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
def split_element(separator, string):
    q, a = get_question(separator, string)
    an, ex = get_explanation(a)

    return q, an, ex


# sort text by separator for split_element
def sort_by_separator(str_element):
    problem = []
    if re.findall(CORRECT, str_element):
        problem = split_element(CORRECT, str_element)
    elif re.findall(R_ANSWERS, str_element):
        problem = split_element(R_ANSWERS, str_element)
    elif re.findall(R_ANSWER, str_element):
        problem = split_element(R_ANSWER, str_element)
    elif re.findall(SOLUTION, str_element):
        problem = split_element(SOLUTION, str_element)
    elif re.findall(RIGHT, str_element):
        problem = split_element(RIGHT, str_element)
    elif re.findall(WRONG, str_element):
        problem = split_element(WRONG, str_element)

    return problem


# provide answer for exam mode
def sort_answers_for_exam(element):
    answer = []
    if re.findall(CORRECT, element):
        answer = element.strip(CORRECT)[slice(-4)]
    elif re.findall(R_ANSWERS, element):
        answer = element.strip(R_ANSWERS)[slice(-4)]
    elif re.findall(R_ANSWER, element):
        answer = element.strip(R_ANSWER)[slice(-4)]
    elif re.findall(SOLUTION, element):
        answer = element[8]
    elif re.findall(RIGHT, element):
        answer = RIGHT
    elif re.findall(WRONG, element):
        answer = WRONG

    return answer
