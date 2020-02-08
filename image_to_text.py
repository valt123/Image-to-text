from PIL import ImageGrab, Image, ImageEnhance, ImageOps
import pytesseract as tess
import pyperclip

tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

image = ImageGrab.grabclipboard()
image.format = "PNG"
image = ImageEnhance.Sharpness(image).enhance(10)
image = ImageOps.grayscale(image)

text = tess.image_to_string(image)

pyperclip.copy(text)
