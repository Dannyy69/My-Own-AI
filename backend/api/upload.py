from fastapi import APIRouter, UploadFile, File
from pathlib import Path
from pypdf import PdfReader

from database.database_instance import db
from database.document_registry import documents

router = APIRouter()

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)


@router.post("/upload")
async def upload(file: UploadFile = File(...)):

    path = UPLOAD_DIR / file.filename

    with open(path, "wb") as f:
        f.write(await file.read())

    text = ""

    if file.filename.endswith(".pdf"):

        reader = PdfReader(path)

        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

    elif file.filename.endswith(".txt"):

        text = path.read_text(
            encoding="utf-8"
        )

    chunk_ids = db.add_document(
        text,
        file.filename
    )

    documents.append(
        {
            "id": len(documents) + 1,
            "filename": file.filename,
            "chunks": len(chunk_ids),
            "size": len(text)
        }
    )

    return {
        "message": "Uploaded successfully",
        "filename": file.filename
    }