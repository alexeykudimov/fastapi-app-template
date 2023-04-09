import os
from typing import Optional

from pydantic import BaseSettings, PostgresDsn, RedisDsn


class Settings(BaseSettings):
    APP_NAME: str
    APP_VERSION: str

    API_PREFIX: str = "/v1"

    SECRET_KEY: str

    LOGGING_LEVEL: str = 'INFO'

    SERVER_PORT: int = 8000
    SERVER_WORKER_NUMBER: int = 4

    DATABASE_URL: Optional[PostgresDsn] = None
    TEST_DATABASE_URL: Optional[PostgresDsn] = None
    REDIS_URL: Optional[RedisDsn] = None

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24
    RESET_TOKEN_EXPIRE_MINUTES: int = 60 * 4
    VERIFY_CODE_EXPIRE_MINUTES: int = 60 * 4

    ENABLE_SQL_ECHO: Optional[bool] = True
    ENABLE_WEB_SERVER_AUTORELOAD: Optional[bool] = True

    class Config:
        env_file_encoding = 'utf-8'


settings = Settings()
