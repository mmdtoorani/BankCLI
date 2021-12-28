"""
1.Registration
2.Remove
"""

from models import User
from utils import make_hash


def registration(username: str, password: str):
    hashed_pass = make_hash(password)
    user = User(username=username, password=hashed_pass)
    user.save()
