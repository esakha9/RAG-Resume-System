"""
============================================================
Generator
============================================================
"""

from llm.prompt import prompt_builder
from llm.ollama_client import ollama_client

from utils.helper import debug


class Generator:

    def generate(self, question, context):

        debug("Building Prompt")

        prompt = prompt_builder.build(
            question,
            context
        )

        debug("Generating Answer")

        answer = ollama_client.generate(prompt)

        return answer


generator = Generator()


# ============================================================
# Testing
# ============================================================

if __name__ == "__main__":

    question = "What skills does Esa have?"

    context = """
Esa Khan is an AI Engineer.

Skills:

Python
Machine Learning
Deep Learning
Computer Vision
Natural Language Processing
"""

    answer = generator.generate(
        question,
        context
    )
    print("=" * 80)
    print(prompt)
    print("=" * 80)
    print("\n")
    print("=" * 60)
    print(answer)
    print("=" * 60)