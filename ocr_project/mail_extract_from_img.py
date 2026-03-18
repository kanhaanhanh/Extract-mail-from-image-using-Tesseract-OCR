import pandas as pd
import pytesseract
from PIL import Image, ImageEnhance
import requests
from io import BytesIO
import re
import time

# ✅ Set Tesseract path
pytesseract.pytesseract.tesseract_cmd = r'..\Tesseract-OCR\tesseract.exe'

# ✅ Setup session with retry
session = requests.Session()
headers = {
    "User-Agent": "Mozilla/5.0"
}

def clean_email(text):
    """Fix common OCR mistakes"""
    text = text.replace(" ", "")
    text = text.replace("gmai1.com", "gmail.com")
    text = text.replace("gmial.com", "gmail.com")
    text = text.replace("yaho0.com", "yahoo.com")
    return text

def extract_email_from_image(url):
    if pd.isna(url) or not str(url).startswith('http'):
        return None

    try:
        # ✅ Request with better settings
        response = session.get(url, headers=headers, timeout=30)
        response.raise_for_status()

        img = Image.open(BytesIO(response.content))

        # ✅ Convert to grayscale
        img = img.convert('L')

        # ✅ Increase contrast
        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(2)

        # ✅ Resize (important for small text)
        img = img.resize(
            (img.width * 3, img.height * 3),
            resample=Image.Resampling.LANCZOS
        )

        # ✅ Try OCR with different configs
        text = pytesseract.image_to_string(img, config='--oem 3 --psm 7')

        if not text.strip():
            text = pytesseract.image_to_string(img, config='--oem 3 --psm 6')

        # ✅ Clean text
        clean_text = clean_email(text)

        # ✅ Extract email
        emails = re.findall(r"[a-zA-Z0-9.\-_%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", clean_text)

        return emails[0] if emails else None

    except requests.exceptions.Timeout:
        return "Error: Timeout"
    except requests.exceptions.RequestException:
        return "Error: Request Failed"
    except Exception as e:
        return f"Error: {str(e)}"


# --- MAIN EXECUTION ---
file_path = "Commercial_with_emails.xlsx"
df = pd.read_excel(file_path, sheet_name="Service")

print("🚀 Processing emails... please wait.")

results = []
for i, url in enumerate(df['email']):
    print(f"Processing {i+1}/{len(df)}")
    
    result = extract_email_from_image(url)
    results.append(result)

    # ✅ Avoid blocking / rate limit
    time.sleep(1)

df['email_extracted'] = results

# ✅ Save result
output_file = "output.xlsx"
df.to_excel(output_file, index=False)

print(f"✅ Done! Saved to {output_file}")