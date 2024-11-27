# -*- coding: utf-8 -*-
# imports
from pathlib import Path
from data_extractor.pdf_to_csv import extract_elements
from data_extractor.separate_exercises import separate
from data_extractor.divide_exercises import divide

path_to_pdf = Path(__file__).parent / 'data_extractor' / 'data' / 'datei.pdf'
path_to_csv = Path(__file__).parent / 'data_extractor' / 'data' / 'test.csv'

if __name__ == '__main__':
    df_page = extract_elements(path_to_pdf)
    df_separated = separate(df_page)
    df_divided = divide(df_separated)
    df_divided.to_csv(path_to_csv, encoding='utf-8', index=False)
