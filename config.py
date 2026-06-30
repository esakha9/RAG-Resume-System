"""
============================================================
File: config.py

Purpose:
    Store all project configuration settings in one place.

Author:
    Esa Khan
============================================================
"""

from pathlib import Path
import os

# ==========================================================
# PROJECT INFORMATION
# ==========================================================

APP_NAME = "RAG Resume System"
VERSION = "1.0.0"

# ==========================================================
# PROJECT PATHS
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent

UPLOAD_FOLDER = BASE_DIR / "uploads"
DATA_FOLDER = BASE_DIR / "data"
LOG_FOLDER = BASE_DIR / "logs"

LOG_FILE = LOG_FOLDER / "rag.log"

# ==========================================================
# DEBUG SETTINGS
# ==========================================================

DEBUG = True
VERBOSE = True
SHOW_TIME = True

# ==========================================================
# EMBEDDING MODEL
# ==========================================================

EMBEDDING_MODEL = os.getenv(
    "EMBEDDING_MODEL",
    "nomic-embed-text"
)

VECTOR_SIZE = 768

# ==========================================================
# TEXT SPLITTING
# ==========================================================

CHUNK_SIZE = 500
CHUNK_OVERLAP = 100

# ==========================================================
# RETRIEVAL
# ==========================================================

TOP_K = 3

# ==========================================================
# QDRANT SETTINGS
# ==========================================================

QDRANT_HOST = os.getenv(
    "QDRANT_HOST",
    "localhost"
)

QDRANT_PORT = int(
    os.getenv(
        "QDRANT_PORT",
        6333
    )
)

COLLECTION_NAME = os.getenv(
    "COLLECTION_NAME",
    "resume_vectors"
)

# ==========================================================
# OLLAMA SETTINGS
# ==========================================================

OLLAMA_HOST = os.getenv(
    "OLLAMA_HOST",
    "http://localhost:11434"
)

OLLAMA_MODEL = os.getenv(
    "OLLAMA_MODEL",
    "qwen2.5:7b"
)

# ==========================================================
# CREATE REQUIRED DIRECTORIES
# ==========================================================

UPLOAD_FOLDER.mkdir(parents=True, exist_ok=True)
DATA_FOLDER.mkdir(parents=True, exist_ok=True)
LOG_FOLDER.mkdir(parents=True, exist_ok=True)

# ==========================================================
# DEBUG TEST
# ==========================================================

if __name__ == "__main__":

    print("=" * 60)
    print(APP_NAME)
    print("=" * 60)

    print(f"Project Folder : {BASE_DIR}")
    print(f"Uploads Folder : {UPLOAD_FOLDER}")
    print(f"Data Folder    : {DATA_FOLDER}")
    print(f"Log File       : {LOG_FILE}")

    print()

    print(f"Embedding Model : {EMBEDDING_MODEL}")
    print(f"Vector Size     : {VECTOR_SIZE}")

    print()

    print(f"Qdrant Host     : {QDRANT_HOST}")
    print(f"Qdrant Port     : {QDRANT_PORT}")
    print(f"Collection Name : {COLLECTION_NAME}")

    print()

    print(f"Ollama Host     : {OLLAMA_HOST}")
    print(f"Ollama Model    : {OLLAMA_MODEL}")

    print()

    print(f"Chunk Size      : {CHUNK_SIZE}")
    print(f"Chunk Overlap   : {CHUNK_OVERLAP}")

    print()

    print(f"Debug Mode      : {DEBUG}")
    print(f"Verbose         : {VERBOSE}")
    print(f"Show Time       : {SHOW_TIME}")

    print("=" * 60)