# app/routers/root.py
from fastapi import APIRouter, Security
from app.dependencies import get_logger
from app.utils.api_key import get_api_key

logger = get_logger()

router = APIRouter()

@router.get("/api/v1")
async def root(api_key: str = Security(get_api_key)):
    return {"message": "Welcome to the FastAPI starter app!"}