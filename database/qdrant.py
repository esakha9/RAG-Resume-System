"""
============================================================
File: qdrant.py

Purpose:
    Connect to Qdrant Database.

Author:
    Esa Khan
============================================================
"""

from qdrant_client import QdrantClient
from qdrant_client.models import Distance
from qdrant_client.models import VectorParams

from config import (
    QDRANT_HOST,
    QDRANT_PORT,
    COLLECTION_NAME,
    VECTOR_SIZE
)

from utils.helper import debug
from utils.helper import success
from utils.helper import warning
from utils.helper import error


class QdrantDatabase:

    def __init__(self):

        try:

            debug("Connecting to Qdrant...")

            self.client = QdrantClient(
                host=QDRANT_HOST,
                port=QDRANT_PORT
            )

            success("Connected to Qdrant.")

        except Exception as e:

            error(f"Connection Error: {e}")
            raise

    # -------------------------------------------------

    def create_collection(self):

        try:

            collections = self.client.get_collections()

            names = [
                collection.name
                for collection in collections.collections
            ]

            # Collection exists
            if COLLECTION_NAME in names:

                info = self.client.get_collection(COLLECTION_NAME)

                current_size = (
                    info.config.params.vectors.size
                )

                if current_size == VECTOR_SIZE:

                    success("Collection already exists.")
                    return

                warning(
                    f"Vector size mismatch "
                    f"({current_size} != {VECTOR_SIZE})"
                )

                warning("Recreating collection...")

                self.client.delete_collection(
                    collection_name=COLLECTION_NAME
                )

            # Create new collection
            self.client.create_collection(

                collection_name=COLLECTION_NAME,

                vectors_config=VectorParams(

                    size=VECTOR_SIZE,

                    distance=Distance.COSINE

                )

            )

            success("Collection created successfully.")

        except Exception as e:

            error(e)

    # -------------------------------------------------

    def delete_collection(self):

        try:

            self.client.delete_collection(
                collection_name=COLLECTION_NAME
            )

            success("Collection deleted.")

        except Exception as e:

            error(e)

    # -------------------------------------------------

    def list_collections(self):

        try:

            collections = self.client.get_collections()

            print("\n========== Collections ==========\n")

            for collection in collections.collections:

                print(collection.name)

        except Exception as e:

            error(e)


# ============================================================
# Singleton
# ============================================================

qdrant_database = QdrantDatabase()


# ============================================================
# Testing
# ============================================================

if __name__ == "__main__":

    qdrant_database.create_collection()

    qdrant_database.list_collections()