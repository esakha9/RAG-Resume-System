"""
===========================================
Qdrant Search Engine
===========================================
"""

from qdrant_client.models import PointStruct

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


            chunks = []


            for point in results.points:

                chunks.append(
                    point.payload["text"]
                )


            return chunks


        except Exception as e:

            error(e)

            return []



search_engine = SearchEngine()