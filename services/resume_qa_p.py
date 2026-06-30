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

from retrieval.retrieve import retriever
from llm.generator import generator

from utils.helper import debug


class ResumeQAPipeline:

    def ask(self, question):

        debug("Starting Question Answering")

        chunks = retriever.get_context(question)

        context = "\n\n".join(chunks)

        answer = generator.generate(

            question=question,

            context=context

        )

        return {

            "question": question,

            "answer": answer,

            "chunks_used": len(chunks)

        }


resume_qa_pipeline = ResumeQAPipeline()


def ask(self, question):

    start = time.perf_counter()

    t1 = time.perf_counter()
    chunks = retriever.get_context(question)
    print(f"Retrieval: {time.perf_counter() - t1:.2f}s")

    context = "\n\n".join(chunks)

    t2 = time.perf_counter()
    answer = generator.generate(
        question=question,
        context=context
    )
    print(f"LLM: {time.perf_counter() - t2:.2f}s")

    print(f"Total: {time.perf_counter() - start:.2f}s")

    return {
        "question": question,
        "answer": answer,
        "chunks_used": len(chunks)
    }