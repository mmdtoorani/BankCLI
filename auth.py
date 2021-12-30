from models import User, Account
from utils import make_hash, generate_token


def registration(username: str, password: str):
    """Creation a user and then his/her account"""

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
    """Check for correct password entry by the user"""
    if User.objects.get(username=username).password == make_hash(password):
        return True

    return False


def is_name_valid(name: str) -> bool:
    """
    Check for first name or last name validation.
    for each letter of the word entered by the user as a name,
    it must be only uppercase and lowercase letters, otherwise it's invalid

    """
    alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    alphabet_lower = "abcdefghijklmnopqrstuvwxyz"

    chars = [i for i in name]
    result_list = [True if i in alphabet_lower or i in alphabet_upper else False for i in chars]

    if all(result_list):  # This will be True, if all the indexes in the result_list are True
        return True

    return False


def user_authenticated(username, password):
    if is_user_exist(username):
        if is_user_valid(username, password):
            return True
        else:
            msg = "Invalid password!"
    else:
        msg = "You have not registered!"

    return False, msg


def collect_user_info(username, first_name, last_name, age):
    user = User.objects.get(username=username)
    user.update(first_name=first_name, last_name=last_name, age=age)
