from fastapi import APIRouter
from pydantic import BaseModel

from database.database_instance import db


router = APIRouter()


class KnowledgeRequest(BaseModel):
    question: str
    answer: str
    category: str = "knowledge"


@router.post("/knowledge")
def add_knowledge(req: KnowledgeRequest):

    text = f"""
Question:
{req.question}

Answer:
{req.answer}
"""

    ids = db.add_document(
        text,
        req.category
    )

    return {
        "message": "Knowledge added successfully.",
        "chunks": len(ids)
    }