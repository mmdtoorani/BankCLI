import datetime

from models import User, Account
import hashlib


def make_hash(password):
    """Convert user's password to hash using md5 algorithm."""

    hash_obj = hashlib.md5(str.encode(password))  # <md5 hash object>
    hexdigest = hash_obj.hexdigest()
    return hexdigest


def is_name_valid(name: str) -> bool:
    """
    Check for first name or last name validation.
    for each letter of the word entered by the user as a name,
    it must be only uppercase and lowercase letters, otherwise it's invalid

    """
    alphabet_uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    alphabet_lowercase = "abcdefghijklmnopqrstuvwxyz"

    chars = [i for i in name]
    result_list = [True if i in alphabet_lowercase or i in alphabet_uppercase else False for i in chars]

    if all(result_list):  # This will be True, if all the indexes in the result_list are True
        return True
    return False


class UserAuthentication:
    """
    Management and handling all about user authentication as registration, collection, removing
    and checking for validations;
    and the main usage of this Class is communication
    between the models and file main.py .

    """

    def __init__(self, username, password=None, age=None, first_name=None, last_name=None):
        self.username = username
        self.password = password
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    @property
    def is_user_exist(self):
        if User.objects(username=self.username):
            return True
        return False

    def registration(self):
        """Creation a user and then his/her account"""

        if not self.is_user_exist:
            if self.password:
                if not len(self.password) < 6:
                    hashed_pass = make_hash(self.password)
                    user = User(
                        username=self.username,
                        password=hashed_pass
                    )
                    user.save()

                    account = Account(
                        user=user
                    )
                    account.save()
                    msg = "You registered successfully!"
                else:
                    msg = "Your password is too short!"
            else:
                msg = "password does not entered!"
        else:
            msg = "ERROR: User already exists...!"

        print(msg)

    @property
    def is_user_valid(self):
        """Check for correct password entry by the user"""

        if self.password:
            if User.objects.get(username=self.username).password == make_hash(self.password):
                return True

        return False

    @property
    def is_authenticated(self):
        if self.is_user_exist:
            if self.is_user_valid:
                return True
            else:
                print("Invalid password!")
        else:
            print("You have not registered!")

        return False

    def collect_user_info(self):
        """
        Completing information about the user
        Update user's document in database

        """

        if is_name_valid(self.first_name) and is_name_valid(self.last_name):
            try:
                int(self.age)
                msg = ""
            except ValueError:
                msg = "Invalid input! Try again"

            if msg is not "Invalid input! Try again":
                user = User.objects.get(username=self.username)
                user.update(
                    first_name=self.first_name,
                    last_name=self.last_name,
                    age=self.age
                )
                msg = 'your account has been updated!'
        else:
            msg = "Invalid input! Try again"

        print(msg)

    def get_info_from_db(self):
        if self.is_authenticated:
            user_by_username = User.objects.get(username=self.username)
            self.first_name = user_by_username.first_name
            self.last_name = user_by_username.last_name
            self.age = user_by_username.age

    def show_info(self):
        self.get_info_from_db()
        user_id = User.objects.get(username=self.username).id
        account = Account.objects.get(user=user_id)
        print(f"\nusername: {self.username}\n")

        # each item is "Not set" if it is null in database
        if self.first_name:
            print(f"First name: {self.first_name}\n")
        else:
            print("First name: Not set\n")

        if self.last_name:
            print(f"Last name: {self.last_name}\n")
        else:
            print("Last name: Not set\n")

        if self.age:
            print(f"Age: {self.age}\n")
        else:
            print("Age: Not set\n")

        print(
            f"finance: {account.finance}\n\n"
            f"number of transactions: {account.number_of_transactions}\n\n"
            f"date of last transaction: {account.date_of_last_transaction}"
        )

    def remove(self):
        if self.is_authenticated:
            user = User.objects.get(username=self.username)
            user.delete()
            print("User has been removed successfully!")


def users_list():
    return User.objects.all()


class Transactions:
    def __init__(self, amount=None, src_account=None, dest_account=None):
        self.amount = amount
        self.src_account = src_account
        self.dest_account = dest_account

    @staticmethod
    def get_user_by_username(username):
        return User.objects.get(username=username).id

    def set_source_account(self, username):
        src_user = self.get_user_by_username(username)
        src_account = Account.objects.get(user=src_user)
        return src_account

    def set_destination_account(self, username):
        dest_user = self.get_user_by_username(username)
        dest_account = Account.objects.get(user=dest_user)
        return dest_account

    @property
    def is_amount_valid(self):
        """
        Checks that the amount must be converted to float
        and be less than the asset

        """

        try:
            self.amount = float(self.amount)
            if self.amount < self.src_account.finance:
                return True
            else:
                print("Your assets are less than the amount entered")

        except ValueError:
            return False

    def subtract(self):
        src_user_final_finance = self.src_account.finance - self.amount
        self.src_account.update(finance=src_user_final_finance)

    def add(self):
        dest_user_final_finance = self.dest_account.finance + self.amount
        self.dest_account.update(finance=dest_user_final_finance)

    def add_num_of_trx(self, username):
        user = self.get_user_by_username(username)
        count = Account.objects.get(user=user).number_of_transactions
        return count + 1

    def transfer(self, src_username, dest_username):
        """
        For transfer from source account to destination account,
        amount must subtract from source account and add to destination account.
        """

        self.src_account = self.set_source_account(src_username)
        self.dest_account = self.set_destination_account(dest_username)
        if self.is_amount_valid:
            self.subtract()
            self.add()

            self.src_account.update(
                date_of_last_transaction=datetime.datetime.now(),
                number_of_transactions=self.add_num_of_trx(src_username)
            )

            self.dest_account.update(
                date_of_last_transaction=datetime.datetime.now(),
                number_of_transactions=self.add_num_of_trx(dest_username)
            )

            print("The transaction was successful")
        else:
            print("Invalid input! Try again")
