"""
===========================================
Resume Question Answering Pipeline
===========================================

Pipeline

Question
    ↓
Retrieve Context
    ↓
Build Prompt
    ↓
Generate Answer
"""

import time

from retrieval.retrieve import retriever
from llm.generator import generator

from utils.helper import debug


class ResumeQAPipeline:

    def ask(self, question):

        debug("Starting Question Answering")

        start = time.perf_counter()

        # =====================================
        # Retrieve relevant resume chunks
        # =====================================
        retrieval_start = time.perf_counter()

        chunks = retriever.get_context(question)

        print(
            f"Retrieval Time: {time.perf_counter() - retrieval_start:.2f} seconds"
        )

        # Join chunks for the LLM prompt
        context = "\n\n".join(
        item["chunk"] for item in chunks
         )

        # =====================================
        # Generate answer
        # =====================================
        llm_start = time.perf_counter()

        answer = generator.generate(
            question=question,
            context=context
        )

        print(
            f"LLM Time: {time.perf_counter() - llm_start:.2f} seconds"
        )

        print(
            f"Total Time: {time.perf_counter() - start:.2f} seconds"
        )

        # =====================================
        # Prepare context for frontend
        # =====================================
        context_response = []

        for chunk in chunks:
            context_response.append({
                "chunk": chunk,
                "score": 1.0
            })

        # =====================================
        # API Response
        # =====================================
        return {
            "question": question,
            "answer": answer,
            "chunks_used": len(chunks),
            "context": context_response
        }


resume_qa_pipeline = ResumeQAPipeline()