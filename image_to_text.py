from PIL import ImageGrab, Image, ImageEnhance, ImageOps
import pytesseract as tess
import pyperclip

tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

image = ImageGrab.grabclipboard()
image.format = "PNG"
image = ImageEnhance.Sharpness(image).enhance(10)
image = ImageOps.grayscale(image)

dark_pixels = 0
total_pixels = 0
for pixel in image.getdata():
    total_pixels += 1
    
    if pixel <= 150:
        dark_pixels += 1
        
print "{} dark pixels out of {} pixels".format(dark_pixels, total_pixels)

if dark_pixels >= total_pixels / 4 * 3:
    image = ImageOps.invert(image)

text = tess.image_to_string(image)
pyperclip.copy(text)
