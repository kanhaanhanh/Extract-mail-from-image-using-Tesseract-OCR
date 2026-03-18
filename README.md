# Extract-mail-from-image-using-Tesseract-OCR

🚀 Project Overview

This project extracts email addresses from images using OCR (Optical Character Recognition). It is designed to process a dataset (Excel file) containing image URLs, apply OCR to each image, and automatically detect and clean email addresses.

This is especially useful for:

+ Real estate data scraping 📊

+ Lead generation 📩

+ Extracting contact info from non-text sources 🖼️

🧠 How It Works

+ Read image URLs from an Excel file

+ Download each image from the URL

+ Preprocess the image to improve OCR accuracy:

- Convert to grayscale

- Increase contrast

- Resize image (upscale)

- Run OCR using Tesseract

- Clean common OCR mistakes (e.g., gmai1.com → gmail.com)

- Extract email using Regex

- Save results back to a new Excel file

📁 Project Structure
project/
│
├── script.py                  # Main Python script
├── Commercial_with_emails.xlsx # Input dataset
├── output.xlsx                 # Output file with extracted emails
└── Tesseract-OCR/              # Tesseract OCR folder (local install)
⚙️ Requirements

Install dependencies:

+ pip install pandas pytesseract pillow requests openpyxl
🔧 Tesseract Setup (No Admin)

+ Download Tesseract OCR (portable or local version)

+ Place it inside your project folder:

Tesseract-OCR/tesseract.exe

+ Update path in code:

pytesseract.pytesseract.tesseract_cmd = r'..\Tesseract-OCR\tesseract.exe'
▶️ How to Run
python script.py
📊 Input Format

Excel file must contain a column:

email
image_url_1
image_url_2
📤 Output

The script generates:

output.xlsx

With a new column:

email	email_extracted
URL	detected@email.com
🛠️ Features

✅ OCR-based email extraction

✅ Automatic image enhancement

✅ Retry-safe HTTP requests

✅ Handles invalid URLs

✅ Fixes common OCR mistakes

✅ Rate limiting to avoid blocking

⚠️ Error Handling

Possible outputs:

+ None → No email found

+ Error: Timeout

+ Error: Request Failed

+ Error: <message>

💡 Example Use Case

+ This project is ideal for:

+ Scraping real estate listings (e.g., Khmer24)

+ Extracting agent contact info from images

+ Automating data cleaning pipelines

🚧 Future Improvements

+ Add multi-email extraction

+ Improve OCR accuracy using AI models

+ Parallel processing for speed

+ Support phone number extraction

👨‍💻 Author

Developed as part of a data extraction & BI workflow project.

⭐ Notes

+ OCR accuracy depends heavily on image quality

+ Small or blurry images may reduce performance

+ Increasing resize scale can improve results but slow down processing
