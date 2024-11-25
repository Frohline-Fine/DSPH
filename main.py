# imports
from pathlib import Path
from data_extractor import pdf_to_txt, separate_exercises, divide_exercises

path_to_pdf = Path(__file__).parent / 'data_extractor' / 'data' / 'datei.pdf'
path_to_csv = Path(__file__).parent / 'data_extractor' / 'data' / 'test.csv'

if __name__ == '__main__':
    df_page = pdf_to_txt.extract(path_to_pdf)
    df_separated = separate_exercises.separate(df_page)
    df_divided = divide_exercises.divide(df_separated)
    df_divided.to_csv(path_to_csv, encoding='utf-8', index=False)

