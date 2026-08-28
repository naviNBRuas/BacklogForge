import os

from cryptography.fernet import Fernet


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-only-insecure-key")
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", "sqlite:///backlogforge.sqlite3"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ENCRYPTION_KEY = os.environ.get("ENCRYPTION_KEY") or Fernet.generate_key().decode()
    ADMIN_EMAIL = os.environ.get("ADMIN_EMAIL")
    ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD")
    WTF_CSRF_ENABLED = True
    FORCE_HTTPS = os.environ.get("FORCE_HTTPS", "false").lower() == "true"


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    WTF_CSRF_ENABLED = False
    ENCRYPTION_KEY = Fernet.generate_key().decode()
