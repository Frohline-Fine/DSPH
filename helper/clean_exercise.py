"""
Provides random exercise from dataframe
"""
from pathlib import Path

# imports
import pandas as pd


# get rid of unwanted characters
def cutter(string):
    cut = string.strip(r'["').strip("['").strip(r'"]')
    return cut.replace(r"\\n", "<br>")


# provide cleaned strings for QLabelWidgets
def clean_exercise(df: pd.DataFrame):
    e = df.sample()
    i = e.index[0]

    question = cutter(df['question'][i])
    answer = cutter(df['answer'][i])
    explanation = cutter(df['explanation'][i])

    return question, answer, explanation
