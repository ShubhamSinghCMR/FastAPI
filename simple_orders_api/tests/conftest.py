import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from dotenv import load_dotenv
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database import Base, get_db
from app.main import app
from tests.fixtures.customers import create_sample_customers
from tests.fixtures.orders import create_sample_orders
from tests.fixtures.products import create_sample_products

load_dotenv(".env.test")
TEST_DATABASE_URL = os.getenv("TEST_DATABASE_URL")

engine = create_engine(TEST_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="function")
def db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    create_sample_customers(db)
    create_sample_products(db)
    create_sample_orders(db)
    yield db
    db.close()


@pytest.fixture
def client(db):
    app.dependency_overrides[get_db] = lambda: db
    with TestClient(app) as c:
        yield c
    app.dependency_overrides.clear()


@pytest.fixture
def auth_token(client):
    user = {
        "username": "testuser",
        "email": "testuser@example.com",
        "password": "testpass123",
    }
    client.post("/api/v1/auth/register", json=user)
    res = client.post(
        "/api/v1/auth/login",
        data={"username": user["username"], "password": user["password"]},
    )
    token = res.json()["access_token"]
    return f"Bearer {token}"


@pytest.fixture
def client_with_auth(client, auth_token):
    def _client_with_auth():
        client.headers.update({"Authorization": auth_token})
        return client

    yield _client_with_auth()
