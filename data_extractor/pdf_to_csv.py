"""
This class extracts text from a pdf and transfers it to a csv file
"""
# imports
import pandas as pd
from pdfminer.high_level import extract_pages, extract_text
from pdfminer.layout import LTTextContainer


def extract_elements(pdf_file):
    data = []
    for page_layout in extract_pages(pdf_file):
        for element in page_layout:
            if isinstance(element, LTTextContainer):
                data.append([element.get_text()])

    df = pd.DataFrame(data, columns=['Question'])

    return df
