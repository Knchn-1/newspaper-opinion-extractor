import os
import re
import zipfile
from pypdf import PdfReader, PdfWriter
from pdf2image import convert_from_path
from PIL import Image
import pytesseract
from tqdm import tqdm

# ===== CONFIGURE TESSERACT & POPPLER =====
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
POPPLER_PATH = r"C:\Users\kanch\Downloads\Release-25.07.0-0\poppler-25.07.0\Library\bin"

# ===== PATHS =====
ZIP_FILE = r"C:\Users\kanch\Downloads\newspapers.zip"
INPUT_DIR = r"C:\Users\kanch\Downloads\newspapers"
TEMP_DIR = r"C:\Users\kanch\Downloads\extracted-newspapers"
OUTPUT_PDF = r"C:\Users\kanch\Downloads\merged_opinions.pdf"

# ===== KEYWORDS TO DETECT OPINION PAGES =====
KEYWORDS = ['opinion', 'editorial', 'op-ed', 'op ed', 'viewpoint', 'letters to the editor', 'commentary']

# ===== STEP 1: UNZIP FILE =====
os.makedirs(INPUT_DIR, exist_ok=True)
with zipfile.ZipFile(ZIP_FILE, 'r') as zip_ref:
    zip_ref.extractall(INPUT_DIR)

print(f" ZIP file extracted to {INPUT_DIR}")
print("Files found:", os.listdir(INPUT_DIR))

# Create temp folder if not exists
os.makedirs(TEMP_DIR, exist_ok=True)

# ===== HELPER FUNCTIONS =====
def score_page_text(text):
    t = (text or '').lower()
    score = 0.0
    for k in KEYWORDS:
        if k in t:
            score += 3.0
    if re.search(r'\bby\s+[A-Z][a-zA-Z\-\.\']+', text or ''):
        score += 1.0
    if len(t.split()) > 200:
        score += 0.5
    return score

def extract_opinion_pages(pdf_path):
    print(f"\nProcessing PDF: {pdf_path}")
    reader = PdfReader(pdf_path)
    selected_pages = []

    for i, page in enumerate(tqdm(reader.pages, desc="Scanning pages")):
        text = page.extract_text()

        # Fallback to OCR if text is empty
        if not text or len(text.strip()) < 20:
            images = convert_from_path(
                pdf_path, first_page=i+1, last_page=i+1, dpi=200, poppler_path=POPPLER_PATH
            )
            text = pytesseract.image_to_string(images[0], lang='eng', config='--psm 1')

        score = score_page_text(text)
        if score >= 3.0:
            print(f"Page {i+1} selected (score={score})")
            selected_pages.append(i)

    print(f"Selected pages for this PDF: {selected_pages}")
    return selected_pages

# ===== MAIN PROCESS =====
all_selected_pages = []

for pdf_file in os.listdir(INPUT_DIR):
    if pdf_file.lower().endswith(".pdf"):
        pdf_path = os.path.join(INPUT_DIR, pdf_file)
        selected = extract_opinion_pages(pdf_path)
        if selected:
            reader = PdfReader(pdf_path)
            writer = PdfWriter()
            for i in selected:
                writer.add_page(reader.pages[i])
            temp_path = os.path.join(TEMP_DIR, f"{os.path.splitext(pdf_file)[0]}_opinions.pdf")
            with open(temp_path, "wb") as f:
                writer.write(f)
            all_selected_pages.append(temp_path)

# Merge all extracted pages
final_writer = PdfWriter()
for pdf_path in all_selected_pages:
    reader = PdfReader(pdf_path)
    for page in reader.pages:
        final_writer.add_page(page)

with open(OUTPUT_PDF, "wb") as f:
    final_writer.write(f)

print("\n Finished!")
print(f"Total PDFs processed: {len(all_selected_pages)}")
print(f"Final merged PDF saved as: {OUTPUT_PDF}")
