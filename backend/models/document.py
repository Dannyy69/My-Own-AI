from pydantic import BaseModel
from typing import List


class Document(BaseModel):
    id: int
    text: str
    embedding: List[float]