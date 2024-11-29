"""
todo: deprecated (to be deleted?)

This class extracts text from a pdf and transfers it to a csv file
but without unnecessary blank lines
"""
# -*- coding: utf-8 -*-
# Import extract_text function from the pdfminer.six library
import pandas as pd
from pathlib import Path
from pdfminer.high_level import extract_text


def extract(path_to_pdf: Path) -> pd.DataFrame:
    # Extract text from the PDF
    text = extract_text(path_to_pdf)

    # Removing any empty lines in the document
    # Split the text into lines and filter out empty lines
    lines = [line.strip() for line in text.splitlines() if line.strip()]

    # Join the non-empty lines back together with newline characters
    cleaned_text = '\n'.join(lines)

    # Transfer cleaned_text into Dataframe and csv
    tlist = []
    for line in cleaned_text.splitlines():
        tlist.append(line)

    x = {'Question': tlist}
    df = pd.DataFrame(x)

    print("data extracted")

    return df
