import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"

a=pytesseract.image_to_string(Image.open('t4.png'))

print(a)