import ollama

from config import EMBEDDING_MODEL
from config import OLLAMA_HOST

from utils.helper import debug
from utils.helper import success
from utils.helper import error


class OllamaEmbedding:

    def __init__(self):

        self.client = ollama.Client(
            host=OLLAMA_HOST
        )

    def encode(self, text):

        try:

            debug("Generating Embedding...")

            response = self.client.embed(

                model=EMBEDDING_MODEL,

                input=text

            )

            success("Embedding Created.")

            return response["embeddings"][0]

        except Exception as e:

            error(e)

            return []


embedding_model = OllamaEmbedding()