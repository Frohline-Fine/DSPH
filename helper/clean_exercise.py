"""
Provides random exercise from dataframe
"""
from pathlib import Path

# imports
import pandas as pd


# get rid of unwanted characters
def cutter(string):
    cut = string.strip(r'["').strip("['").strip(r'"]')
    clean_cut = cut.replace(r"\\n", "<br>")

    return clean_cut


# provide cleaned strings for QLabelWidgets
def clean_exercise(df: pd.DataFrame):
    e = df.sample()
    i = e.index[0]

    question = cutter(str(df['question'][i]))
    answer = cutter(str(df['answer'][i]))
    explanation = cutter(str(df['explanation'][i]))

    return question, answer, explanation
