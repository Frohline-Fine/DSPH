# -*- coding: utf-8 -*-
# Import extract_text function from the pdfminer.six library
import pandas as pd
from pdfminer.high_level import extract_text

# Specify the PDF file you want to extract text from
pdf_file = 'datei.pdf'

# Extract text from the PDF
text = extract_text(pdf_file)

# Removing any empty lines in the document
# Split the text into lines and filter out empty lines
lines = [line.strip() for line in text.splitlines() if line.strip()]

# Join the non-empty lines back together with newline characters
cleaned_text = '\n'.join(lines)

with open('cleaned_datei.txt', 'w', encoding='utf-8') as f:
    for line in cleaned_text.splitlines():
        f.write(line + '\n')

# # Print the cleaned text
# print(cleaned_text)
