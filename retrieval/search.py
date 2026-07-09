"""
===========================================
Qdrant Search Engine
===========================================
"""

from config import (
    COLLECTION_NAME,
    TOP_K
)

from database.qdrant import qdrant_database
from utils.helper import debug, success, error


class SearchEngine:

    def search(self, vector):

        try:

            debug("Searching Qdrant")

            results = qdrant_database.client.query_points(
                collection_name=COLLECTION_NAME,
                query=vector,
                limit=TOP_K
            )

            success("Search Completed")

            context = []

            for point in results.points:
                context.append({
                    "chunk": point.payload["text"],
                    "score": point.score
                })

            return context

        except Exception as e:

            error(e)
            return []


search_engine = SearchEngine()