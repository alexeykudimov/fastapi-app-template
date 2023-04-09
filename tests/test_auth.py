from httpx import AsyncClient

VALID_CREDS = {"username": "test_user", "password": "test_pass"}
INVALID_USER_CREDS = {"username": "invalid_user", "password": "invalid_pass"}
INVALID_PASS_CREDS = {"username": "test_user", "password": "invalid_pass"}

async def test_register(ac: AsyncClient):
    response = await ac.post("v1/auth/register", json=VALID_CREDS)
    assert response.status_code == 201

async def test_login(ac: AsyncClient):
    response = await ac.post("v1/auth/login", json=VALID_CREDS)
    assert response.status_code == 200

async def test_invalid_user_login(ac: AsyncClient):
    response = await ac.post("v1/auth/login", json=INVALID_USER_CREDS)
    assert response.status_code == 404

async def test_invalid_pass_login(ac: AsyncClient):
    response = await ac.post("v1/auth/login", json=INVALID_PASS_CREDS)
    assert response.status_code == 403

async def test_valid_access_token(ac: AsyncClient):
    from src.app.auth.security import auth_user_id

    response = await ac.post("v1/auth/login", json=VALID_CREDS)
    
    access_token = response.json().get('access_token')
    assert access_token

    user_id = await auth_user_id(access_token)
    assert user_id
