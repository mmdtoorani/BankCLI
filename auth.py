"""
1.Registration
2.Remove
"""

from models import User


def registration(username: str, password: int):
    user = User(username=username, password=password)
    user.save()
