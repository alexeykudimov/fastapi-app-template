from pydantic import BaseModel


class AuthIn(BaseModel):
    username: str
    password: str


class AuthOut(BaseModel):
    access_token: str
