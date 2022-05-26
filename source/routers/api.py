from fastapi import APIRouter
from app.routers import login

router = APIRouter()
router.include_router(login.router, tags=["login"], prefix="/users")
router.include_router()
