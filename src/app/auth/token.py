import logging

import jwt
from datetime import datetime, timedelta

from src.config.settings import settings

ALGORITHM = "HS256"
access_token_jwt_subject = "access"

logger = logging.getLogger(__name__)


def create_token(user_id: str):
    return create_access_token(
            data=dict(user_id=user_id), 
            expires_delta=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES))


def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    expire = datetime.utcnow() + expires_delta if expires_delta else timedelta(minutes=15)
    to_encode = dict(**data, exp=expire, sub=access_token_jwt_subject)
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=ALGORITHM)
