from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routes import router as system_router
from api.vector_routes import router as vector_router

app = FastAPI(title="Nyrion AI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(system_router)
app.include_router(vector_router)


@app.get("/")
async def root():
    return {
        "message": "Nyrion AI Backend Running"
    }