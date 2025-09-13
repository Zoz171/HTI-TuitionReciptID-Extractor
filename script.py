from PIL import Image
import pytesseract
import re
import sys

if len(sys.argv) > 2:
    print(r"Error: Please provide only one image{path} at the moment.")

image = Image.open(sys.argv[1])

data_str = pytesseract.image_to_string(image)

match_ID = re.search(r'320\d{5}', data_str)

print(match_ID.group())

# with open('test.pdf', 'w+b') as f:
#     f.write(pdf)

