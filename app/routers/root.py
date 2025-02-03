# app/routers/root.py
from fastapi import APIRouter, Depends, Security
from app.dependencies import get_logger
from app.utils.api_key import get_api_key

router = APIRouter()

@router.get("/api/v1")
async def root(
  api_key: str = Security(get_api_key),
  logger=Depends(get_logger)
):
  logger.info("Root endpoint accessed")
  return {"message": "Welcome to the FastAPI starter app!"}