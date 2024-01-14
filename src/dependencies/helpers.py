import bcrypt


def hash_password(password: str) -> bytes:
    """
    password converting password to array of bytes
    """
    # converting password to array of bytes
    _byte: bytes = password.encode("utf-8")
    salt = bcrypt.gensalt()

    hash = bcrypt.hashpw(_byte, salt)
    return hash
