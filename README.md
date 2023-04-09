## :zap: Starter template for your FastAPI application with simple JWT authorization

### :dart: Technologies
* Python 3.11
* FastAPI
* Async SQLAlchemy 2.0
* Async Alembic
* Async Pytest
### :dart: Environment
    APP_NAME=<your app name>
    APP_VERSION=<your app version>

    SECRET_KEY=<your secret key>

    DATABASE_URL=postgresql+asyncpg://<db_user>:<db_pass>@<db_host>:<db_port>/<db_name>
    TEST_DATABASE_URL=postgresql+asyncpg://<db_user>:<db_pass>@<db_host>:<db_port>/<db_name>
### :dart: Build
    docker build -t server:latest .
### :dart: Run
    docker run -d -p 8000:8000 --name server --volume .:/app --env-file .env server:latest 
### :dart: Migrate
    docker exec -it server alembic upgrade heads
### :dart: Tests
    docker exec -it server pytest -v -s tests
### :dart: Let's go!
    http://localhost:8000/docs/