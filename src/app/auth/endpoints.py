import logging
from uuid import UUID
from fastapi import APIRouter, Depends
from src.app.auth.schemas import AuthIn, AuthOut
from src.app.auth.service import AuthService

logger = logging.getLogger(__name__)
router = APIRouter()


@router.post(
        "/login", 
        status_code=200,
        response_model=AuthOut)
async def login(
        payload: AuthIn,
        auth_service: AuthService = Depends()):
    '''
    Login. Return access token.
    '''
    return await auth_service.authenticate(payload)


@router.post(
        "/register", 
        status_code=201,
        response_model=AuthOut)
async def register(
        payload: AuthIn,
        auth_service: AuthService = Depends()):
    '''
    Register. Return access token.
    '''
    return await auth_service.register(payload)
