"""
A Script to extract data from a pdf file
"""
# imports
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer

# Specify the PDF file you want to extract text from
pdf_file = 'datei.pdf'

for page_layout in extract_pages(pdf_file):
    for element in page_layout:
        if isinstance(element, LTTextContainer):
            print(element.get_text())

