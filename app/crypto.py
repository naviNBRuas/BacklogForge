from cryptography.fernet import Fernet
from flask import current_app
from sqlalchemy.types import String, TypeDecorator


class EncryptedString(TypeDecorator):
    """Transparently encrypts/decrypts a string column at rest with Fernet."""

    impl = String
    cache_ok = True

    def process_bind_param(self, value, dialect):
        if value is None:
            return None
        fernet = Fernet(current_app.config["ENCRYPTION_KEY"].encode())
        return fernet.encrypt(value.encode()).decode()

    def process_result_value(self, value, dialect):
        if value is None:
            return None
        fernet = Fernet(current_app.config["ENCRYPTION_KEY"].encode())
        return fernet.decrypt(value.encode()).decode()
