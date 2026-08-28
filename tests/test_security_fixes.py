import pytest

from app import _seed_admin, create_app
from app.extensions import db
from app.models import User
from config import TestConfig


def test_seed_admin_does_not_promote_pre_existing_account(app):
    with app.app_context():
        attacker = User(email="admin@example.com", password_hash="not-a-real-hash", role="user")
        db.session.add(attacker)
        db.session.commit()

        app.config["ADMIN_EMAIL"] = "admin@example.com"
        app.config["ADMIN_PASSWORD"] = "whatever-the-real-admin-typed"
        _seed_admin(app)

        refreshed = User.query.filter_by(email="admin@example.com").first()
        assert refreshed.role == "user"


def test_create_app_rejects_insecure_secret_key_outside_debug():
    class InsecureConfig(TestConfig):
        TESTING = False
        DEBUG = False

    with pytest.raises(RuntimeError):
        create_app(InsecureConfig)


def test_login_takes_similar_path_for_unknown_email_and_wrong_password(client):
    from tests.conftest import signup_and_login

    signup_and_login(client, email="known@example.com", password="correct-password")
    client.post("/auth/logout")

    resp_unknown = client.post(
        "/auth/login", data={"email": "unknown@example.com", "password": "whatever123"}
    )
    resp_wrong = client.post(
        "/auth/login", data={"email": "known@example.com", "password": "wrong-password"}
    )
    assert resp_unknown.status_code == resp_wrong.status_code == 200
