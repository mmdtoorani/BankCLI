import hashlib
import secrets


def make_hash(password):
    return hashlib.md5(str.encode(password)).hexdigest()


def generate_token():
    return secrets.token_hex(16)
