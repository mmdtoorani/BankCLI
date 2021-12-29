import hashlib
import secrets


def make_hash(password):
    """Convert user's password to hash using md5 algorithm."""

    hash_obj = hashlib.md5(str.encode(password))  # <md5 hash object>
    hexdigest = hash_obj.hexdigest()
    return hexdigest


def generate_token():
    return secrets.token_hex(16)
