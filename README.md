# RAG Resume System

A Retrieval-Augmented Generation (RAG) application that allows users to upload a resume in PDF format and ask natural language questions about its contents. The system extracts text, generates embeddings, stores them in a Qdrant vector database, retrieves the most relevant information for a query, and uses a local Large Language Model (Qwen2.5 via Ollama) to generate accurate answers.

---

# Features

* Upload resumes in PDF format
* Extract text from PDF documents
* Split text into chunks
* Generate embeddings using `nomic-embed-text`
* Store embeddings in Qdrant
* Retrieve relevant resume sections using semantic search
* Generate answers using Qwen2.5 through Ollama
* REST API built with FastAPI
* Dockerized application with Docker Compose support

---

# Tech Stack

## Backend

* Python 3.12
* FastAPI
* Uvicorn

## Vector Database

* Qdrant

## Embedding Model

* nomic-embed-text (Ollama)

## Large Language Model

* Qwen2.5:7B (Ollama)

## Containerization

* Docker
* Docker Compose

---

# Project Structure

```
RAG-Resume-System/
│
├── api.py
├── app.py
├── config.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
│
├── services/
│   ├── resume_p.py
│   └── resume_qa_p.py
│
├── ingestion/
├── retrieval/
├── llm/
├── database/
├── models/
├── utils/
│
├── uploads/
├── logs/
└── data/
```

---

# Architecture

```
User
│
▼
Website / Swagger UI
│
▼
FastAPI
│
├── POST /upload
│      │
│      ▼
│   Resume Pipeline
│      │
│      ▼
│   PDF Loader
│      ▼
│   Text Splitter
│      ▼
│   Embedding Model
│      ▼
│   Qdrant
│
└── POST /ask
       │
       ▼
   QA Pipeline
       │
       ▼
Question Embedding
       ▼
Similarity Search
       ▼
Retrieved Context
       ▼
Prompt Builder
       ▼
Qwen2.5 (Ollama)
       ▼
Generated Answer
```

---

# Installation

## Clone the repository

```bash
git clone <repository-url>
cd RAG-Resume-System
```

---

# Install Ollama

Download and install Ollama.

Pull the required models:

```bash
ollama pull qwen2.5:7b
ollama pull nomic-embed-text
```

Verify the models:

```bash
ollama list
```

---

# Run with Docker

Build and start the application:

```bash
docker compose up --build
```

Stop the application:

```bash
docker compose down
```

---

# API Documentation

After the application starts:

Swagger UI

```
http://localhost:8000/docs
```

---

# API Endpoints

## Health Check

```
GET /health
```

---

## Upload Resume

```
POST /upload
```

Upload a PDF resume.

---

## Ask Question

```
POST /ask
```

Example request:

```json
{
  "question": "Who is Esa Khan?"
}
```

Example response:

```json
{
  "question": "Who is Esa Khan?",
  "answer": "...",
  "chunks_used": 5
}
```

---

# RAG Pipeline

## Resume Ingestion

```
PDF
↓
PDF Loader
↓
Text Splitter
↓
Embedding Model
↓
Qdrant
```

## Question Answering

```
Question
↓
Embedding Model
↓
Qdrant Similarity Search
↓
Relevant Chunks
↓
Prompt Builder
↓
Qwen2.5
↓
Answer
```

---

# Future Improvements

* Multi-user support
* Authentication
* Multiple resume management
* Streaming responses
* Cloud deployment
* CI/CD pipeline
* Hybrid retrieval
* Metadata filtering

---

# Author

**Esa Khan**

Software Engineer | AI Engineer

---
