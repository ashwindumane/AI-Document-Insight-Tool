import PyPDF2
import requests

def extract_pdf_text(path):
    text = ""
    with open(path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() or ""
    return text

def get_ai_insight(text):
    try:
        # Replace with actual Sarvam AI API details
        response = requests.post(
            "https://sarvam.ai/api/summarize",
            json={"text": text},
            timeout=10
        )
        if response.status_code == 200:
            return response.json().get("summary")
    except Exception:
        pass
    return None

def fallback_insight(text):
    from collections import Counter
    words = [w.lower() for w in text.split()]
    most_common = Counter(words).most_common(5)
    return "Top 5 words: " + ", ".join([f"{w}({c})" for w, c in most_common])
