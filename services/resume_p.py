"""
===========================================
Resume Ingestion Pipeline
===========================================

Pipeline

PDF
 ↓
Load PDF
 ↓
Split Text
 ↓
Create Embeddings
 ↓
Store In Qdrant
"""

from ingestion.pdf_loader import PDFLoader
from ingestion.text_splitter import TextSplitter
from ingestion.vector_store import VectorStore

from utils.helper import debug


class ResumePipeline:

    def ingest(self, pdf_path):

        debug("Starting Resume Ingestion")

        loader = PDFLoader(pdf_path)

        text = loader.load()

        if not text:

            return 0

        splitter = TextSplitter()

        chunks = splitter.split(text)

        store = VectorStore()

        store.store(chunks)

        return len(chunks)


resume_pipeline = ResumePipeline()