from llm.ollama_client import OllamaClient
from database.vector_db import VectorDB


class DocumentDB:

    def __init__(self):

        self.vector_db = VectorDB(768)

        self.ollama = OllamaClient()

    def split_text(

        self,

        text,

        chunk_size=500,

        overlap=50

    ):

        chunks = []

        start = 0

        while start < len(text):

            end = min(

                len(text),

                start + chunk_size

            )

            chunks.append(

                text[start:end]

            )

            start += (

                chunk_size - overlap

            )

        return chunks

    def add_document(

        self,

        text,

        category="default"

    ):

        chunks = self.split_text(text)

        ids = []

        for chunk in chunks:

            embedding = self.ollama.embed(chunk)

            ids.append(

                self.vector_db.insert(

                    metadata=chunk,

                    category=category,

                    embedding=embedding

                )

            )

        return ids

    def search(

        self,

        query,

        k=5

    ):

        embedding = self.ollama.embed(query)

        return self.vector_db.search(

            embedding,

            k,

            "cosine",

            "hnsw"

        )