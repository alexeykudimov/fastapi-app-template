import logging
from uuid import UUID

import jwt
from fastapi import Depends, Security, HTTPException
from fastapi.security import APIKeyHeader
from pydantic import ValidationError

from src.config.settings import settings

ALGORITHM = "HS256"

logger = logging.getLogger(__name__)


auth_header_dep = APIKeyHeader(
    name='Authorization', auto_error=True,
    description='Standard header with a Bearer token')


def get_auth_token(auth_header: str = Security(auth_header_dep)) -> str:
    scheme, _, token = auth_header.partition(' ')
    if scheme == auth_header:
        raise HTTPException(
                status_code=401, detail='Invalid Authorization header')
    if scheme.lower() != 'bearer':
        raise HTTPException(
                status_code=401, detail='Invalid Authorization scheme')

    return token


async def auth_user_id(token: str = Depends(get_auth_token)) -> UUID:
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[ALGORITHM, ])
    except (jwt.InvalidTokenError, ValidationError) as e:
        logger.error("Error validating token!")
        raise HTTPException(
                status_code=401, detail='Error validating token')

    return UUID(hex=payload['user_id'])
