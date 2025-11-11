# 🧠 OCR Name Search Tool (Hindi + English)

A Flask web app that performs OCR on uploaded PDFs (Hindi/English) and searches for any name or keyword inside the recognized text.  

Includes Tesseract + Poppler in a lightweight Docker container for easy deployment on Render.com.

## To run locally use --> standalone.py

---

## 🚀 Deploy on Render (Free)

1. Push this repo to your GitHub account.
2. Visit [https://render.com](https://render.com).
3. Click **New Web Service** → **Build from Dockerfile**.
4. Select your repo.
5. Click **Deploy** 🚀

Render will automatically:
- Build the Docker image (including Tesseract + Poppler)
- Install all Python requirements
- Expose port 8080

Once deployed, open your Render URL — you’ll see the web UI.

---

## 🧰 Local Development

### Setup
```bash
git clone https://github.com/yourusername/ocr-name-search.git
cd ocr-name-search
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

