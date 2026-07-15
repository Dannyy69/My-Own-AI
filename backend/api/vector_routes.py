from fastapi import APIRouter

from algorithms.vector_db import VectorDB
from models.document import Document

router = APIRouter(prefix="/vector")

db = VectorDB()


@router.post("/add")
async def add_document(document: Document):
    db.add_document(document)

    return {
        "success": True,
        "count": db.count()
    }


@router.get("/documents")
async def documents():
    return db.get_documents()