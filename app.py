from flask import Flask, request, render_template_string
from pdf2image import convert_from_path
import pytesseract, re, os, tempfile, shutil

app = Flask(__name__)

HTML = """
<!doctype html>
<html lang="en">
<head>
  <title>OCR Name Search Tool</title>
  <style>
    body { font-family: Arial, sans-serif; margin: 40px; background: #f5f6fa; }
    form { background: #fff; padding: 20px; border-radius: 10px; box-shadow: 0 2px 6px #ccc; }
    input, button { margin: 10px 0; padding: 10px; border-radius: 5px; border: 1px solid #ddd; width: 100%; }
    button { background: #007bff; color: white; border: none; cursor: pointer; }
    button:hover { background: #0056b3; }
    .results { background: #fff; padding: 20px; border-radius: 10px; margin-top: 20px; box-shadow: 0 2px 6px #ccc; }
    .match { background: #eaffea; padding: 5px; border-radius: 4px; margin-bottom: 5px; display: block; }
    .nomatch { color: #999; }

    /* Loader styles */
    #loader {
      display: none;
      position: fixed;
      top: 0; left: 0; width: 100%; height: 100%;
      background: rgba(255,255,255,0.8);
      z-index: 9999;
      justify-content: center;
      align-items: center;
      flex-direction: column;
      font-size: 18px;
      color: #333;
    }

    .spinner {
      border: 6px solid #f3f3f3;
      border-top: 6px solid #007bff;
      border-radius: 50%;
      width: 60px;
      height: 60px;
      animation: spin 1s linear infinite;
      margin-bottom: 10px;
    }

    @keyframes spin {
      0% { transform: rotate(0deg); }
      100% { transform: rotate(360deg); }
    }
  </style>

  <script>
    // Show loader on form submit
    function showLoader() {
      document.getElementById("loader").style.display = "flex";
    }
  </script>
</head>

<body>
  <h2>Hindi + English OCR Name Search</h2>
  <form method="POST" enctype="multipart/form-data" onsubmit="showLoader()">
    <label>Upload PDF file:</label>
    <input type="file" name="file" accept="application/pdf" required>
    <label>Enter name or word to search:</label>
    <input type="text" name="query" placeholder="e.g. शमीम / Shamim / Mansoori" required>
    <button type="submit">Search</button>
  </form>

  <!-- Loader overlay -->
  <div id="loader">
    <div class="spinner"></div>
    <div>Processing your PDF... Please wait.</div>
  </div>

  {% if results %}
  <div class="results">
    <h3>Results for "{{ query }}"</h3>
    {% if matches %}
      {% for m in matches %}
        <div class="match">📄 Page {{ m[0] }} → {{ m[1] }}</div>
      {% endfor %}
    {% else %}
      <p class="nomatch">❌ No matches found.</p>
    {% endif %}
  </div>
  {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    results = False
    matches = []
    query = ""

    if request.method == "POST":
        pdf_file = request.files.get("file")
        query = request.form.get("query", "").strip()

        if pdf_file and query:
            temp_dir = tempfile.mkdtemp()
            temp_pdf = os.path.join(temp_dir, pdf_file.filename)
            pdf_file.save(temp_pdf)

            try:
                pages = convert_from_path(temp_pdf, dpi=150)
                pattern = re.compile(re.escape(query), re.IGNORECASE)

                for i, page in enumerate(pages, start=1):
                    text = pytesseract.image_to_string(page, lang="hin+eng")
                    for line in text.splitlines():
                        if pattern.search(line):
                            matches.append((i, line.strip()))
                results = True
            finally:
                shutil.rmtree(temp_dir, ignore_errors=True)

    return render_template_string(HTML, results=results, matches=matches, query=query)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
