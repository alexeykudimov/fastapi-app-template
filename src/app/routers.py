from fastapi import APIRouter

from src.app.auth.endpoints import router as auth_router

api_router = APIRouter()

api_router.include_router(auth_router, prefix='/auth', tags=['Auth'])
