from fastapi import APIRouter, status, HTTPException
import sqlalchemy


router = APIRouter()

@router.get(/)
async def visualizar():
    pass