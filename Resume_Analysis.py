# Resume Analyser

#OCR function is used if simple text extraction does not work and the resume is in image form
def OCR(pdf_path):
    import pytesseract
    from pdf2image import convert_from_path
    try:
        images = convert_from_path(pdf_path)
        for image in images:
            page_text = pytesseract.image_to_string(image)
            text += page_text + "\n"
        return text
    except Exception as e:
        print(f"Text extraction failed: {e}")

#This function is used to extract text from pdf. This is simple extraction without OCR
def text_from_pdf(pdf_path):
    import pdfplumber
    text=""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text
        if text.strip():
            return text.strip()
    except Exception as e:
        OCR(pdf_path)

# Use Gemini's API
def resume_analyser(prompt_with_resume):
    import os
    from dotenv import load_dotenv
    import google.generativeai as gen_ai
    load_dotenv()
    Api = os.getenv("Api_gemini")
    gen_ai.configure(api_key=Api)
    model = gen_ai.GenerativeModel(model_name="gemini-1.5-flash")
    resume_analysis = model.generate_content(prompt_with_resume)
    return resume_analysis.text

# Designing prompt for Gemini
def prompt_definition(job_desc, resume):
    prompt = "Please look at the job description:\n" + job_desc + "Now please analyze this resume in reference to this job description and give insights with ATS score:\n" + resume
    return prompt