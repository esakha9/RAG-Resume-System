"""
===========================================
RAG Resume System
===========================================

Pipeline

PDF
 ↓
Chunks
 ↓
Embeddings
 ↓
Qdrant
 ↓
Question
 ↓
Embedding
 ↓
Similarity Search
 ↓
Prompt
 ↓
Qwen2.5
 ↓
Answer
"""

from ingestion.pdf_loader import PDFLoader
from ingestion.text_splitter import TextSplitter
from ingestion.vector_store import VectorStore

from retrieval.retrieve import retriever

from llm.generator import generator

from config import UPLOAD_FOLDER

from utils.helper import print_title
from utils.helper import debug


# ==========================================================
# INGESTION
# ==========================================================

def ingest_resume(path):

    debug("Starting Resume Ingestion")

    loader = PDFLoader(path)

    text = loader.load()

    if not text:

        print("No text extracted from PDF")

        return

    splitter = TextSplitter()

    chunks = splitter.split(text)

    store = VectorStore()

    store.store(chunks)

    print("\nResume stored successfully.\n")


# ==========================================================
# QUESTION ANSWERING
# ==========================================================

def ask_question():

    while True:

        question = input(
            "\nAsk about resume (type exit): "
        )

        if question.lower() == "exit":

            break

        # ------------------------
        # Retrieve Context
        # ------------------------

        chunks = retriever.get_context(question)

        context = "\n\n".join(chunks)

        print("\n========== RETRIEVED CONTEXT ==========\n")

        print(context)

        # ------------------------
        # LLM
        # ------------------------

        answer = generator.generate(

            question=question,

            context=context

        )

        print("\n========== ANSWER ==========\n")

        print(answer)


# ==========================================================
# MAIN
# ==========================================================

def main():

    print_title(
        "RAG Resume System"
    )

    resume = (
        UPLOAD_FOLDER /
        "uploaded_resume.pdf"
    )

    ingest_resume(resume)

    ask_question()


if __name__ == "__main__":

    main()