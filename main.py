from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import pdfplumber

app = FastAPI()

@app.post("/parse")
async def parse_resume(resume: UploadFile = File(...)):
    with pdfplumber.open(resume.file) as pdf:
        text = "\n".join(page.extract_text() or "" for page in pdf.pages)

    # Simulated simple extraction (you can use spaCy, OpenAI, etc. later)
    return JSONResponse(content={
        "name": "Extracted from resume manually or with AI",
        "skills": ["Python", "React", "SQL"],  # Stubbed, extract with NLP
        "experience": "2 years at ABC Inc",
        "education": "BTech AI & Robotics"
    })
