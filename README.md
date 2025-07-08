## 🧠 AI Resume Analyzer

AI Resume Analyzer is a Streamlit-based web app that analyzes resumes using **Google Gemini AI**. Upload your resume (PDF) and paste a job description — the app compares them and provides feedback, insights, and an ATS (Applicant Tracking System) score to help optimize your resume.

---

## 🚀 Features

- 📄 Upload your resume in PDF format
- 📋 Paste a job description
- 🧠 Get AI-powered analysis using Google Gemini
- 🗒️ Supports text extraction from PDFs (including OCR fallback for scanned/image-based resumes)
- ✅ Instant feedback, suggestions, and ATS scoring

---

## 🛠️ Tech Stack

- Python  
- [Streamlit](https://streamlit.io/) for the GUI  
- [Google Gemini API](https://ai.google.dev/) for resume analysis  
- pdfplumber for text extraction from PDFs  
- pytesseract and pdf2image for OCR fallback  
- python-dotenv for environment variable handling  

---

## 📦 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/akshatlamba1/AI-Resume-Assistant.git
cd AI-Resume-Assistant
````

### 2. Install Dependencies

Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Install required packages:

```bash
pip install -r requirements.txt
```

### 3. Setup Environment Variables

Create a `.env` file in the project root and add your Gemini API key:

```
Api_gemini=your_google_gemini_api_key_here
```

### 4. Run the App

```bash
streamlit run gui_file_name.py
```

Replace `gui_file_name.py` with the name of your Streamlit GUI file.

---

## 📁 Project Structure

```
.
├── Resume_Analysis.py         # Core functions (text extraction, prompt design, Gemini analysis)
├── gui_file_name.py           # Streamlit GUI interface
├── .env                       # Stores your Gemini API key (not to be shared)
├── requirements.txt           # List of dependencies
└── README.md                  # Project documentation
```

---

## ✅ To-Do / Improvements

* [ ] Add support for DOCX resumes
* [ ] Display resume score and suggestions in a formatted way
* [ ] Support batch analysis of multiple resumes
* [ ] Export feedback as PDF

---

## 📄 License

MIT License

---

## 🤝 Contributions

Feel free to fork the repo, submit issues, or open pull requests. Feedback is always welcome!

---

## 💡 Acknowledgements

* [Google Gemini AI](https://ai.google.dev/)
* [Streamlit](https://streamlit.io/)
* [pytesseract](https://pypi.org/project/pytesseract/)
* [pdfplumber](https://pypi.org/project/pdfplumber/)
