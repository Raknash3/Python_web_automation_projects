import pytesseract 

from PIL import Image

f=Image.open('0103397000.tif').convert("RGBA")

#x=pytesseract.image_to_string(f)

#print(x)
text_file = open("41.txt", "w")
text_file.write(pytesseract.image_to_string(f))
text_file.close()