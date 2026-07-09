import shutil

from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from config import UPLOAD_FOLDER

from services.resume_p import resume_pipeline
from services.resume_qa_p import resume_qa_pipeline


app = FastAPI(
    title="RAG Resume API",
    version="1.0.0"
)
# ==========================================================
# CORS Configuration
# ==========================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5501",
        "http://127.0.0.1:5501",
        "http://localhost:5173",
        "http://localhost:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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
async def upload_resume(resume: UploadFile = File(...)):

    # Check that a file was actually selected
    if not resume.filename:
        raise HTTPException(
            status_code=400,
            detail="No file selected."
        )

    # Allow .PDF, .Pdf, etc.
    if not resume.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )

    file_path = UPLOAD_FOLDER / "uploaded_resume.pdf"

    try:

        # Save uploaded file
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(resume.file, buffer)

        # Process resume
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

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Resume processing failed: {str(e)}"
        )

# ==========================================================
# Ask Question
# ==========================================================

@app.post("/ask")
async def ask_question(request: QuestionRequest):

    response = resume_qa_pipeline.ask(

        request.question

    )

    return response