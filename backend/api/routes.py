from fastapi import APIRouter

router = APIRouter()


@router.get("/system/info")
async def system_info():
    return {
        "name": "Nyrion AI",
        "version": "2.0.0",
        "engine": "Python",
        "status": "Online",
    }