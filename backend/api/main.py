from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from api.upload import router as upload_router
from api.knowledge import router as knowledge_router

from database.database_instance import db
from database.document_registry import documents
from llm.ollama_client import OllamaClient

app = FastAPI(title="Nyrion AI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://my-own-ai-livid.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload_router)
app.include_router(knowledge_router)

db.add_document(
    """
Python is a programming language.
FastAPI is a modern, fast (high-performance) web framework.
Ollama runs LLMs locally.
""",
    "notes",
)

llm = OllamaClient()


class ChatRequest(BaseModel):
    message: str


@app.get("/")
def root():
    return {"status": "Nyrion AI Running"}


@app.get("/system/info")
def system_info():
    return {
        "status": "Online",
        "engine": "llama3.2",
        "version": "1.0",
        "name": "Nyrion AI",
    }


@app.get("/documents")
def get_documents():
    return {
        "documents": documents,
        "count": len(documents),
    }


@app.delete("/documents/{doc_id}")
def delete_document(doc_id: int):

    for doc in documents:
        if doc["id"] == doc_id:
            documents.remove(doc)
            return {
                "message": "Document deleted"
            }

    return {
        "message": "Document not found"
    }


@app.post("/chat")
def chat(req: ChatRequest):

    search = db.search(req.message, 3)

    context = "\n\n".join(
        r["metadata"]
        for r in search["results"]
    )

    prompt = f"""
You are Nyrion AI.

Answer ONLY from the context below.

If the answer is not present, reply:

I don't have enough knowledge about that yet.

Context:
{context}

Question:
{req.message}

Answer:
"""

    answer = llm.generate(prompt)

    return {
        "answer": answer,
        "context": search["results"],
    }