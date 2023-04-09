import logging
from uuid import UUID

from fastapi import Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.app.auth.models import User
from src.app.auth.schemas import AuthIn, AuthOut
from src.app.auth.token import create_token
from src.app.auth.password import get_password_hash, verify_password
from src.misc.dependencies import get_async_session

logger = logging.getLogger(__name__)


class AuthService:
    def __init__(self,
                 db: AsyncSession = Depends(get_async_session)):
        self.db = db

    async def get_user(self, user_id: UUID) -> User:
        stmt = select(User).where(User.id == user_id)
        user = (await self.db.execute(stmt)).scalar_one_or_none()

        if not user:
            raise HTTPException(status_code=404, detail="This user doesn't exist")

        return user

    async def get_user_by_username(self, username: str) -> User:
        stmt = select(User).where(User.username == username)
        user = (await self.db.execute(stmt)).scalar_one_or_none()

        if not user:
            raise HTTPException(status_code=404, detail="This user doesn't exist")

        return user
    
    async def create_user(self, **kwargs) -> User:
        user = User(**kwargs)
        self.db.add(user)
        await self.db.commit()

        return user

    async def authenticate(self, payload: AuthIn) -> AuthOut:
        user = await self.get_user_by_username(payload.username)

        if not verify_password(payload.password, user.hashed_password):
            raise HTTPException(status_code=403, detail="Invalid password")

        return AuthOut(access_token=create_token(str(user.id)))
    
    async def register(self, payload: AuthIn) -> AuthOut:
        user = await self.create_user(
            username=payload.username,
            hashed_password=get_password_hash(payload.password))

        return AuthOut(access_token=create_token(str(user.id)))
