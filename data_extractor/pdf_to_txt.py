# -*- coding: utf-8 -*-
# Import extract_text function from the pdfminer.six library
import pandas as pd
from pdfminer.high_level import extract_text

# Specify the PDF file you want to extract text from
pdf_file = 'data/datei.pdf'

# Extract text from the PDF
text = extract_text(pdf_file)

# Removing any empty lines in the document
# Split the text into lines and filter out empty lines
lines = [line.strip() for line in text.splitlines() if line.strip()]

# Join the non-empty lines back together with newline characters
cleaned_text = '\n'.join(lines)

tlist = []
for line in cleaned_text.splitlines():
    tlist.append(line)

x = {'Question': tlist}
df = pd.DataFrame(x)
df.to_csv('data/cleaned_datei.csv', index=False)

