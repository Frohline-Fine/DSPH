"""
This class extracts text from source file and transfers it to csv file
"""
# imports
import pandas as pd
from pdfminer.high_level import extract_pages, extract_text
from pdfminer.layout import LTTextContainer

from helper.paths import src_file


def extract_data():
    data = []
    for page_layout in extract_pages(src_file):
        for element in page_layout:
            if isinstance(element, LTTextContainer):
                data.append([element.get_text()])

    df = pd.DataFrame(data, columns=['Question'])

    return df
