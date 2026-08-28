from app.crypto import EncryptedString


def test_encrypted_string_roundtrip(app):
    with app.app_context():
        column = EncryptedString(200)
        ciphertext = column.process_bind_param("secret notes", dialect=None)
        assert ciphertext != "secret notes"
        assert column.process_result_value(ciphertext, dialect=None) == "secret notes"
