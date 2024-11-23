# Import required classes from the pdfminer.six library
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator

# Open the PDF file
with open('datei.pdf', 'rb') as pdf_file:
    # Create a PDFParser
    pdf_parser = PDFParser(pdf_file)

    # Create a PDFDocument
    pdf_document = PDFDocument(pdf_parser)

    # Create a PDFResourceManager
    pdf_resource_manager = PDFResourceManager()

    # Create a PDFDevice
    pdf_device = PDFPageAggregator(pdf_resource_manager)

    # Create a PDFPageInterpreter
    pdf_page_interpreter = PDFPageInterpreter(pdf_resource_manager, pdf_device)

    # Initialize a set to store unique font information
    unique_fonts = set()

    # Iterate through the pages in the PDF
    for page in PDFPage.create_pages(pdf_document):
        pdf_page_interpreter.process_page(page)

        layout = pdf_device.get_result()

        # Iterate through layout elements
        for element in layout:
            print(type(element))
        #     if hasattr(element, "text"):
        #
        #     #     font_name = element.fontname.split('+', 1)
            #     font_info = f"Font Name: {font_name[1]}"
            #     if hasattr(element, "size"):
            #         font_info += f", Font Size: {int(element.size)}"
            #
            #     # Check if we haven't seen this font before
            #     if font_info not in unique_fonts:
            #         print(font_info)
            #         unique_fonts.add(font_info)

# Close the PDF file
pdf_file.close()