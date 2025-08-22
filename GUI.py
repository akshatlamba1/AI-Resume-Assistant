from Resume_Analysis import OCR
from Resume_Analysis import text_from_pdf
from Resume_Analysis import resume_analyser
from Resume_Analysis import prompt_definition

import streamlit as st
st.set_page_config(page_title="Resume Analyzer", layout="wide")
# Title
st.title("AI Resume Analyzer")
st.write("Analyze your resume and match it with job descriptions using Google Gemini AI.")

col1 , col2 = st.columns(2)
with col1:
    uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])
with col2:
    job_description = st.text_area("Enter Job Description:", placeholder="Paste the job description here...")

if uploaded_file is not None:
    st.success("Resume uploaded successfully!")
else:
    st.warning("Please upload a resume in PDF format.")

st.markdown("<div style= 'padding-top: 10px;'></div>", unsafe_allow_html=True)
if uploaded_file:
    # Save uploaded file locally for processing
    with open("uploaded_resume.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())
    # Extract text from PDF
    resume_text = text_from_pdf("uploaded_resume.pdf")
    prompt = prompt_definition(job_description, resume_text)
    if st.button("Analyze Resume"):
        with st.spinner("Analyzing resume..."):
            try:
                # Analyze resume
                # analysis = resume_analyser(prompt)
                st.success("Analysis complete!")
                # st.write(analysis)
                st.write(resume_text)
            except Exception as e:
                st.error(f"Analysis failed: {e}")