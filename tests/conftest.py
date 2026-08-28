import pytest

from app import create_app
from app.extensions import db
from config import TestConfig


@pytest.fixture
def app():
    app = create_app(TestConfig)
    yield app
    with app.app_context():
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


def signup_and_login(client, email="user@example.com", password="password123"):
    client.post("/auth/signup", data={
        "email": email, "password": password, "confirm_password": password,
    })
    client.post("/auth/login", data={"email": email, "password": password})
