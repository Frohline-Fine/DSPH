"""
This class converts PDF files into HTML pages.
"""
# imports
from pdfminer.high_level import extract_text_to_fp
from io import BytesIO


def convert_pdf_to_html(pdf_path, html_path):
    output_buffer = BytesIO()
    with open(pdf_path, 'rb') as pdf_file:
        extract_text_to_fp(pdf_file, output_buffer, output_type='html')

    html_content = output_buffer.getvalue().decode('utf-8')

    with open(html_path, 'w', encoding='utf-8') as html_file:
        html_file.write(html_content)
