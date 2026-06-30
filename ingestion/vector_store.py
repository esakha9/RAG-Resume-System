"""
===========================================
Vector Store
===========================================
"""

import uuid

from qdrant_client.models import PointStruct

from config import COLLECTION_NAME

from models.ollama_embedding import embedding_model

from database.qdrant import qdrant_database

from utils.helper import debug
from utils.helper import success
from utils.helper import error


class VectorStore:

    def store(self, chunks):

        try:

            debug("Creating Embeddings")

            points = []

            for chunk in chunks:

                vector = embedding_model.encode(chunk)

                point = PointStruct(

                    id=str(uuid.uuid4()),

                    vector=vector,

                    payload={

                        "text": chunk

                    }

                )

                points.append(point)

            debug("Uploading To Qdrant")

            qdrant_database.client.upsert(

                collection_name=COLLECTION_NAME,

                points=points

            )

            success("Vectors Stored Successfully")

        except Exception as e:

            error(e)