"""
todo: deprecated (to be deleted?) [.split() not working properly]

This class separates the problem from options

"""

import re
from pathlib import Path

import pandas as pd

# patterns
LETTER_PATTERN = r"[A-Z]\)\s+"
HASH_PATTERN = r"#\s+[A-Z]"
DIGIT_PATTERN = r"[1-5].\s+"

test = Path(__file__).parent / "data" / "test.csv"
csv = pd.read_csv(test)
df = pd.DataFrame(csv)


def by_letter(question):
    options = []
    re.findall(LETTER_PATTERN, question)
    snippets = re.split(LETTER_PATTERN, question)

    return snippets


def by_hash(question):
    re.findall(HASH_PATTERN, question)
    snippets = re.split(HASH_PATTERN, question)

    for snippet in snippets:
        print(snippet)


def by_digit(question):
    re.findall(DIGIT_PATTERN, question)
    snippets = re.split(DIGIT_PATTERN, question)
    print(question)
    print(snippets[0])
    for snippet in snippets:
        print(snippet)
    # return snippets


if __name__ == '__main__':
    question = df['question'][58:65]

    for i in question:
        by_digit(i)
