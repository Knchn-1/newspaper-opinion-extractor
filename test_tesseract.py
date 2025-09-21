import pytesseract
from PIL import Image

# Tell Python where Tesseract is installed
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Test Tesseract version
print("Tesseract Version:", pytesseract.get_tesseract_version())

# Optional: Test OCR on a sample image
# Make sure you have sample.png in the same folder
try:
    text = pytesseract.image_to_string(Image.open("sample.png"))
    print("OCR Result:\n", text)
except FileNotFoundError:
    print("No sample image found, but Tesseract is working!")
