import os

from cryptography.fernet import Fernet


INSECURE_DEFAULT_SECRET_KEY = "dev-only-insecure-key"


class Config:
    DEBUG = os.environ.get("FLASK_DEBUG", "false").lower() == "true"
    SECRET_KEY = os.environ.get("SECRET_KEY", INSECURE_DEFAULT_SECRET_KEY)
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", "sqlite:///backlogforge.sqlite3"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # None outside debug/testing forces create_app() to fail fast rather than
    # generate a throwaway key that can't decrypt data from a previous run.
    ENCRYPTION_KEY = os.environ.get("ENCRYPTION_KEY") or (
        Fernet.generate_key().decode() if DEBUG else None
    )
    ADMIN_EMAIL = os.environ.get("ADMIN_EMAIL")
    ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD")
    WTF_CSRF_ENABLED = True
    FORCE_HTTPS = os.environ.get("FORCE_HTTPS", "false").lower() == "true"


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    WTF_CSRF_ENABLED = False
    ENCRYPTION_KEY = Fernet.generate_key().decode()
