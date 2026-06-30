
"""
============================================================
Prompt Builder
============================================================
"""


class PromptBuilder:

    def build(self, question, context):

        prompt = f"""
You are a resume assistant.

Answer ONLY from the resume context.

If the answer is not found, reply:

"I couldn't find that information in the resume."

==========================
Resume
==========================

{context}

==========================
Question
==========================

{question}

==========================
Answer
==========================
"""

        return prompt


prompt_builder = PromptBuilder()


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
Computer Vision
NLP
"""

    prompt = prompt_builder.build(
        question,
        context
    )

    print(prompt)