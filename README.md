🧠 OCR Name Search Tool (Hindi + English)

A lightweight Flask web application that allows users to upload scanned PDFs in Hindi or English, automatically perform OCR using Tesseract, and search for any name or keyword (e.g., “शमीम”, “Shamim”, “Mansoori”) inside the text — all through a simple web interface.

Includes:

🔍 Full-text search (user-entered query, not fixed)

🧾 PDF to image conversion via Poppler

🧠 OCR using Tesseract (with Hindi + English models)

⚙️ Automatic cleanup of uploaded files

🌀 Loader animation while processing

🌐 Deployable on Render / Railway / PythonAnywhere

🚀 Features
Feature	Description
🧠 OCR Engine	Tesseract with Hindi (hin) + English (eng) recognition
🧾 PDF Conversion	Uses pdf2image + Poppler to extract images from PDFs
🔍 Search	User-entered term (case-insensitive, Unicode-supported)
🧹 Cleanup	Automatically deletes uploaded files after processing
💻 UI	Minimal responsive HTML with a spinner loader
☁️ Deploy Anywhere	Works on Render, Railway, Fly.io, PythonAnywhere, or locally
🗂️ Project Structure
ocr-name-search/
│
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation (this file)
└── (Optional) Dockerfile  # For container-based deployment

⚙️ Installation (Local Setup)
1️⃣ Clone the repository
git clone https://github.com/yourusername/ocr-name-search.git
cd ocr-name-search

2️⃣ Create a virtual environment
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Install system dependencies

You need:

tesseract-ocr (OCR engine)

poppler-utils (for PDF image conversion)

🧩 On macOS:
brew install tesseract poppler

🧩 On Ubuntu/Debian:
sudo apt-get update
sudo apt-get install -y tesseract-ocr poppler-utils

🧩 On Windows:

Download and install Tesseract → https://github.com/UB-Mannheim/tesseract/wiki

Download Poppler for Windows → https://blog.alivate.com.au/poppler-windows/

Add both to your system PATH.

5️⃣ (Optional) Add Hindi OCR model

If hin.traineddata is missing, download it manually:

sudo mkdir -p /usr/share/tesseract-ocr/4.00/tessdata
sudo curl -L -o /usr/share/tesseract-ocr/4.00/tessdata/hin.traineddata \
https://github.com/tesseract-ocr/tessdata_best/raw/main/hin.traineddata

▶️ Running Locally
python app.py


Then open in your browser:

http://127.0.0.1:8080

💡 How to Use

Upload a PDF file (scanned or text-based).

Enter a name or keyword you want to search (e.g., शमीम, Mansoori, Samim).

Click Search.

The app will:

Convert your PDF to images,

Run OCR using Tesseract (hin+eng),

Search the recognized text for your query,

Display all matching lines with page numbers.

The file is automatically deleted after processing.

🌀 Loader Animation

A smooth loader is shown when the form is submitted and OCR is running:

<div id="loader">
  <div class="spinner"></div>
  <div>Processing your PDF... Please wait.</div>
</div>


It is automatically hidden when the server responds.

☁️ Deployment Options
🚀 Option 1: Render.com (Recommended for Free Hosting)

Create a free account → https://render.com

Connect your GitHub repo.

Add a new Web Service.

In “Build Command”:

apt-get update && apt-get install -y tesseract-ocr poppler-utils && pip install -r requirements.txt


In “Start Command”:

gunicorn app:app


Deploy 🎉

🚆 Option 2: Railway.app

Create a free account → https://railway.app

Connect your GitHub repo.

Add a Procfile:

web: gunicorn app:app --bind 0.0.0.0:$PORT


Add a .railway file with:

apt-get update && apt-get install -y tesseract-ocr poppler-utils && pip install -r requirements.txt

🐍 Option 3: PythonAnywhere

Upload app.py and requirements.txt to /home/yourusername/ocr_app/.

Create a virtualenv:

cd ~/ocr_app
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt


Configure Web tab:

Working directory: /home/yourusername/ocr_app

Virtualenv path: /home/yourusername/ocr_app/venv

WSGI file:

import sys
path = '/home/yourusername/ocr_app'
if path not in sys.path:
    sys.path.append(path)
from app import app as application


Reload app.

🧾 Example Output

When you upload a file and search for “शमीम”, you’ll see:

Results for "शमीम"
📄 Page 2 → शमीम मंसूरी पुत्र अब्दुल हकीम
📄 Page 5 → शमीम अहमद निवासी वाराणसी


If no matches:

❌ No matches found.

📦 Requirements
flask
pdf2image
pytesseract
pillow

🧹 Auto Cleanup

Every uploaded file is stored in a temporary directory and deleted automatically after processing via:

shutil.rmtree(temp_dir, ignore_errors=True)


This ensures zero disk accumulation and full privacy for user uploads.

⚠️ Notes & Limitations

Accuracy depends on PDF scan quality and OCR model.

Large PDFs (10+ pages) may take 30–60 seconds.

Hindi text OCR requires hin.traineddata.

Works best on Render / Railway / local machine (PythonAnywhere free tier is too slow for OCR-heavy workloads).

🧑‍💻 Author & License

Developed by: [Mohd Sohaib / CurlSek Team]
License: MIT License

Feel free to fork and adapt this app for your own OCR or document intelligence projects!

🌟 Future Enhancements

 Downloadable OCR text report (PDF/CSV)

 Highlighting matches visually in the PDF

 Support for multiple language packs

 Progress bar with live updates

 REST API endpoint for programmatic use
