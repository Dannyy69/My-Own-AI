import os
import sys

sys.path.append(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)

from database.document_db import DocumentDB

db = DocumentDB()

db.add_document(
    """
Python is a programming language.

It supports AI.

It supports web development.

FastAPI is written in Python.

Ollama allows local LLM inference.
""",
    "notes"
)

print()

result = db.search(

    "What is FastAPI?"

)

print(result)