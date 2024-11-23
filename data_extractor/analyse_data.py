import re

from pandas.core.dtypes.inference import is_float
from pdfminer.high_level import extract_pages

# Specify the PDF file you want to extract text from
# pdf_file = 'datei.pdf'
input = 'cleaned_datei.txt'
output = 'questions.txt'
pattern = r"[0-9]+\.([A-Za-z0-9äßüö]+( [A-Za-z0-9äßüö]+)+)\?"
pattern2 = r"[0-9]+\. ([A-Za-z0-9äßüö]+( [A-Za-z0-9äßüö]+)+)\?"
result_list = []


with open(input, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        result = re.findall(pattern, line)
        result2 = re.findall(pattern2, line)
        if result:
            result_list.append(result)
        elif result2:
            result_list.append(result2)

for item in result_list:
    print(item)

# with open(output, 'w', encoding='utf-8') as f:
#     for line in result_list:
#         print(line, file=f)
#         # f.write(line + '\n')
#
# print(len(result_list))






# for page_layout in extract_pages(pdf_file):
#     for element in page_layout:
#         print(element)
