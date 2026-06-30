"""
===========================================
Convert User Question Into Vector
===========================================
"""

from models.ollama_embedding import embedding_model
from utils.helper import debug, success, error


class QueryEmbedder:


    def encode(self, question):

        try:

            debug("Creating Query Embedding")

            vector = embedding_model.encode(question)

            success("Query Embedded")

            return vector


        except Exception as e:

            error(e)

            return None



query_embedder = QueryEmbedder()