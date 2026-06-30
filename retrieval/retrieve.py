"""
===========================================
Retriever Pipeline
===========================================
"""

from retrieval.embed_query import query_embedder
from retrieval.search import search_engine


from utils.helper import debug



class Retriever:


    def get_context(self, question):


        debug("Retrieving Context")


        vector = query_embedder.encode(
            question
        )


        results = search_engine.search(
            vector
        )


        return results



retriever = Retriever()