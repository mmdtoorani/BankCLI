"""
1.Registration
2.Remove
"""

from models import User, Account
from utils import make_hash, generate_token


def registration(username: str, password: str):
    hashed_pass = make_hash(password)
    user = User(username=username, password=hashed_pass)
    user.save()
    account = Account(
        user=user,
        address=generate_token(),
    )
    account.save()


def is_user_exist(username: str):
    if User.objects(username=username):
        return True

    return False


def is_user_valid(username, password):
    if User.objects.get(username=username).password == make_hash(password):
        return True

    return False


def is_name_valid(name: str) -> bool:
    alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
    chars = [i for i in name]
    result_list = [True if i in alphabet_lower or i in alphabet_upper else False for i in chars]
    if all(result_list):
        return True

    return False


def collect_user_info(username, first_name, last_name, age):
    user = User.objects.get(username=username)
    user.update(first_name=first_name, last_name=last_name, age=age)
