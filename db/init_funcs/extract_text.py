"""

This class extracts text from pdf and transfers to dataframe
without unnecessary blank lines

"""

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
    cleaned_text = '<br>\n'.join(lines)

    # Transfer cleaned_text into Dataframe
    tlist = []
    for line in cleaned_text.splitlines():
        tlist.append(line)

    df = pd.DataFrame(tlist, columns=['Question'])

    print("data extracted")

    return df
