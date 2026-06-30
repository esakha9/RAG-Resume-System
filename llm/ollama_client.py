import ollama

from config import OLLAMA_MODEL
from config import OLLAMA_HOST

from utils.helper import debug
from utils.helper import success
from utils.helper import error


class OllamaClient:

    def __init__(self):

        self.client = ollama.Client(
            host=OLLAMA_HOST
        )

    def generate(self, prompt):

        try:

            debug("Sending Prompt To Ollama...")

            response = self.client.chat(

                model=OLLAMA_MODEL,

                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]

            )

            success("Response Generated.")

            return response["message"]["content"]

        except Exception as e:

            error(e)

            return "Unable to generate response."


ollama_client = OllamaClient()


# ============================================================
# Testing
# ============================================================

import time

if __name__ == "__main__":

    start = time.perf_counter()

    answer = ollama_client.generate(
        "What is Python? Answer in one sentence."
    )

    end = time.perf_counter()

    print(answer)
    print(f"\nTime: {end - start:.2f} seconds")