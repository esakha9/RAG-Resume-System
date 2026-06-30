# AI Debugging Context - RAG Resume System


## Project Purpose

This project is a RAG (Retrieval Augmented Generation) Resume System.

Flow:

PDF Resume
    |
    v
PDF Loader
    |
    v
Text Chunks
    |
    v
Embedding Model
    |
    v
Vector Database (Qdrant)
    |
    v
User Question
    |
    v
Query Embedding
    |
    v
Similarity Search
    |
    v
Relevant Resume Context
    |
    v
LLM (Ollama)
    |
    v
Answer


## Tech Stack

Python:
3.12

Virtual Environment:
.venv

Embedding:
sentence-transformers/all-MiniLM-L6-v2

Vector Database:
Qdrant (Docker)

LLM:
Ollama (later)


## Project Structure

RAG-Resume-System/

app.py

config.py

database/
    qdrant.py

models/
    embedding_model.py

ingestion/
    pdf_loader.py
    text_splitter.py
    vector_store.py

retrieval/
    embed_query.py
    search.py
    retrieve.py

llm/
    prompt.py
    ollama_client.py
    generator.py

utils/
    helper.py
    logger.py


## Current Stage

Currently testing:

PDF
+
Embedding
+
Qdrant
+
Retrieval

LLM is disabled.


## Debugging Rules

When fixing an error:

1. Explain the reason first.

2. Tell which file caused it.

3. Explain why that file exists.

4. Give the smallest possible fix.

5. Do not rewrite the entire project unless necessary.


## Error Information

Paste:

Error:

[PUT ERROR HERE]


Command Used:

[PUT COMMAND HERE]


File:

[PUT FILE NAME HERE]


Expected Behavior:

[WHAT SHOULD HAPPEN]


Actual Behavior:

[WHAT HAPPENED]