# Newspaper Opinion/Editorial Extractor

## Overview

This project automates the extraction of **Opinion/Editorial pages** from multiple English newspaper PDFs and merges them into a single consolidated PDF.

**Key Features:**
- Automatically extracts PDFs from a ZIP file
- Detects opinion/editorial pages using **keyword scoring** and **author detection**
- Supports scanned PDFs using **OCR** (`pytesseract` + `pdf2image`)
- Merges all selected pages into a single PDF (`merged_opinions.pdf`)
- Fully automated workflow with **minimal human intervention**

---

## Motivation

The task demonstrates:
- Ability to **programmatically solve real-world problems**
- Effective use of multiple Python libraries and tools
- Automation of a multi-step workflow (ZIP → scan → extract → merge)
- Responsible usage of **LLMs** (ChatGPT & Claude) for learning and debugging

---

## Installation

1. **Clone the repository:**
   ```bash
   git clone <your-repo-link>
   cd <repo-folder>
   ```

2. **Create a virtual environment (optional but recommended):**
   
   **Windows:**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```
   
   **Linux / Mac:**
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install Tesseract OCR:**
   - **Windows:** [Download Tesseract](https://github.com/UB-Mannheim/tesseract/wiki)
   - **Mac:** `brew install tesseract`
   - **Linux:** `sudo apt install tesseract-ocr`

5. **Install Poppler (required for PDF → image conversion):**
   - **Windows:** [Download Poppler](https://poppler.freedesktop.org/)
   - **Mac:** `brew install poppler`
   - **Linux:** `sudo apt install poppler-utils`

6. **Update paths in `extract_opinion_pages.py` if needed:**
   ```python
   ZIP_FILE = r"<path-to-newspapers.zip>"
   INPUT_DIR = r"<path-to-extracted-folder>"
   TEMP_DIR = r"<path-to-temp-folder>"
   OUTPUT_PDF = r"<path-to-output-merged.pdf>"
   ```

---

## Usage

1. Place `newspapers.zip` in the designated folder
2. Run the script:
   ```bash
   python extract_opinion_pages.py
   ```

**What the script does:**
- Extracts ZIP file automatically
- Scans PDFs page by page for editorial content
- Uses OCR for scanned PDFs
- Scores pages based on keywords, author patterns, and word count
- Extracts selected pages into temporary PDFs
- Merges all extracted pages into `merged_opinions.pdf`

---

## Workflow

1. **Unzip** the newspaper ZIP file
2. **Scan PDFs** page by page:
   - Extract text using `pypdf`
   - Apply OCR if page is scanned or empty
   - Score pages to detect opinion/editorial content
3. **Extract pages** to temporary PDFs
4. **Merge** all pages into a single consolidated PDF

---

## LLM Assistance

- **ChatGPT:** Explored library functions (`pypdf`, `pdf2image`, `pytesseract`) and planned OCR integration
- **Claude:** Helped troubleshoot errors and optimize code snippets

**Note:** LLMs were used only for learning and debugging. All core logic, scoring, automation, and decision-making were implemented manually.

---

## Dependencies

- Python ≥ 3.9
- `pypdf`
- `pdf2image`
- `Pillow`
- `pytesseract`
- `tqdm`

---

## Outcome

- Fully automated extraction of opinion/editorial pages from multiple newspapers
- Consolidated PDF ready for submission
- Demonstrates problem-solving, automation skills, and responsible LLM usage

---

## File Structure

```
├── extract_opinion_pages.py   # Main script
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
├── newspapers.zip             # Input ZIP file (not in repo)
├── extracted-newspapers/      # Temp folder for opinion pages
└── merged_opinions.pdf        # Final merged PDF
```
