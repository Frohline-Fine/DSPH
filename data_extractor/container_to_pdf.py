# imports
import re
import pandas as pd
from pdfminer.high_level import extract_pages, extract_text
from pdfminer.layout import LTTextContainer

# Specify the PDF file you want to extract text from
pdf_file = 'data/datei.pdf'
csv_file = 'data/data.csv'
out = 'question.txt'
data = []
# pattern = r"[0-9]+\.([A-Za-z0-9äßüö]+( [A-Za-z0-9äßüö]+)+)\?"
# pattern2 = r"[0-9]+\. ([A-Za-z0-9äßüö]+( [A-Za-z0-9äßüö]+)+)\?"


def write_into_file(question):
    with open(out, 'w', encoding='utf-8') as f:
        f.write(question + '\n')


for page_layout in extract_pages(pdf_file):
    for element in page_layout:
        if isinstance(element, LTTextContainer):
            data.append([element.get_text()])

df = pd.DataFrame(data, columns=['Question'])
print(df.head())
df.to_csv(csv_file, index=False)
