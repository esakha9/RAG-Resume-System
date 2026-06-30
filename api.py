import shutil

from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel

from config import UPLOAD_FOLDER

from services.resume_p import resume_pipeline
from services.resume_qa_p import resume_qa_pipeline


app = FastAPI(
    title="RAG Resume API",
    version="1.0.0"
)


# ==========================================================
# Request Model
# ==========================================================

class QuestionRequest(BaseModel):

    question: str


# ==========================================================
# Home
# ==========================================================

@app.get("/")
def home():

    return {

        "message": "RAG Resume API is running"

    }


# ==========================================================
# Health Check
# ==========================================================

@app.get("/health")
def health():

    return {

        "status": "healthy"

    }


# ==========================================================
# Upload Resume
# ==========================================================

@app.post("/upload")
async def upload_resume(file: UploadFile = File(...)):

    if not file.filename.endswith(".pdf"):

        raise HTTPException(

            status_code=400,

            detail="Only PDF files are allowed."

        )

    file_path = UPLOAD_FOLDER / "uploaded_resume.pdf"

    with open(file_path, "wb") as buffer:

        shutil.copyfileobj(file.file, buffer)

    chunks = resume_pipeline.ingest(file_path)

    if chunks == 0:

        raise HTTPException(

            status_code=400,

            detail="No text could be extracted from the PDF."

        )

    return {

        "message": "Resume uploaded successfully.",

        "chunks": chunks

    }


# ==========================================================
# Ask Question
# ==========================================================

@app.post("/ask")
async def ask_question(request: QuestionRequest):

    response = resume_qa_pipeline.ask(

        request.question

    )

    return response