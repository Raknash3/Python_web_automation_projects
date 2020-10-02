import pytesseract
from PIL import Image

text_file = open("1.txt", "w")
n = text_file.write(pytesseract.image_to_string(Image.open('C:/Users/ravi/Desktop/IG/assignment 6s/1.jpg')))
text_file.close()