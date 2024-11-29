# -*- coding: utf-8 -*-
# imports
from pathlib import Path
from data_extractor.create_csv import create_csv
from data_extractor.separate_exercises import separate
from data_extractor.divide_exercises import divide

from helper.paths import csv_file

if __name__ == '__main__':
    df_page = create_csv()
    df_separated = separate(df_page)
    df_divided = divide(df_separated)
    df_divided.to_csv(csv_file, encoding='utf-8', index=False)
