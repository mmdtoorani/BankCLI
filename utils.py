import hashlib


def make_hash(password):
    return hashlib.md5(str.encode(password)).hexdigest()


# def is_valid_password(password):
#     if isinstance
#         return True
#
#     return False
