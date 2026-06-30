"""
===========================================
Text Splitter
===========================================
"""

from config import CHUNK_SIZE
from config import CHUNK_OVERLAP

from utils.helper import debug
from utils.helper import success


class TextSplitter:

    def split(self, text):

        debug("Splitting Text")

        chunks = []

        start = 0

        while start < len(text):

            end = start + CHUNK_SIZE

            chunk = text[start:end]

            chunks.append(chunk)

            start += CHUNK_SIZE - CHUNK_OVERLAP

        success(f"{len(chunks)} Chunks Created")

        return chunks