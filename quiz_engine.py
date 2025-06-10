import PyPDF2
import random

def extract_text_from_pdf(uploaded_file):
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def generate_quiz(uploaded_file):
    if uploaded_file.name.endswith(".pdf"):
        text = extract_text_from_pdf(uploaded_file)
    else:
        text = uploaded_file.read().decode("utf-8")
    
    sentences = text.split(".")
    quiz_questions = random.sample([s.strip() + "?" for s in sentences if len(s) > 40], k=min(5, len(sentences)))
    return quiz_questions
