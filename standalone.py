# === PRE-REQ ====
#pip install pytesseract pdf2image pillow
#sudo apt install tesseract-ocr tesseract-ocr-hin
#alternatviely  forr tesseract
#brew install tesseract
#brew install tesseract-lang
#pip install pytesseract pdf2image pillow
#brew install poppler  # required for pdf2image on macOS
#to confirm --> tesseract --version
# to run --> python find_name_in_pdf.py
#NOTE: THIS WORKS ON SINGLE FILE, BUT CAN BE EASILY EXTENDED TO PROCESS MULTIPLE FILES

import pytesseract
from pdf2image import convert_from_path
import re
import os

# === CONFIGURATION ===
PDF_PATH = "/Users/sohaib/Downloads/AC312P211.pdf"   # Change this to your file name
LANGUAGES = "hin+eng"        # Hindi + English OCR
DPI = 150                    # Adjust for clarity vs speed

# === NAME VARIATIONS TO SEARCH ===
patterns = [
    r"शमीम", r"समीम", r"शमिम", r"समिम"
]

# === CONVERT PDF TO IMAGES ===
print("Converting PDF pages to images...")
pages = convert_from_path(PDF_PATH, dpi=DPI)
print(f"Total pages: {len(pages)}\n")

# === OCR EACH PAGE AND SEARCH ===
matches_found = []

for i, page in enumerate(pages, start=1):
    text = pytesseract.image_to_string(page, lang=LANGUAGES)
    for line in text.splitlines():
        for pattern in patterns:
            if re.search(pattern, line, flags=re.IGNORECASE):
                matches_found.append((i, line.strip()))
                break  # avoid duplicate hits per line

# === SHOW RESULTS ===
if matches_found:
    print("\n✅ POSSIBLE MATCHES FOUND:\n")
    for page_no, line in matches_found:
        print(f"[Page {page_no}] {line}")
else:
    print("\n❌ No matches found for Shamim/Samim/Mansoori (in Hindi or English).")

# === OPTIONAL: SAVE RESULTS ===
if matches_found:
    with open("ocr_matches.txt", "w", encoding="utf-8") as f:
        for page_no, line in matches_found:
            f.write(f"[Page {page_no}] {line}\n")
    print("\nResults saved to: ocr_matches.txt")
