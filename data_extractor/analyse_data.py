from pdfminer.high_level import extract_pages

# Specify the PDF file you want to extract text from
pdf_file = 'datei.pdf'

for page_layout in extract_pages(pdf_file):
    for element in page_layout:
        print(element)
