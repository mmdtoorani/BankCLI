from models import User, Account
from utils import make_hash, generate_token


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


def users_list():
    return User.objects.all()


class UserAuthentication:
    """
    Management and handling all about user authentication as registration, collection, removing
    and checking for validations;
    and the main usage of this Class is communication
    between the models and file main.py .

    """

    def __init__(self, username, password, age=None, first_name=None, last_name=None):
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
            if not len(self.password) < 6:
                hashed_pass = make_hash(self.password)
                user = User(
                    username=self.username,
                    password=hashed_pass
                )
                user.save()

                account = Account(
                    user=user,
                    address=generate_token(),
                )
                account.save()
                msg = "You registered successfully!"
            else:
                msg = "Your password is too short!"
        else:
            msg = "ERROR: User already exists...!"

        print(msg)

    @property
    def is_user_valid(self):
        """Check for correct password entry by the user"""

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

    def show_info(self):
        if self.is_authenticated:
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
                f"Your Token address: {account.address}\n\n"
                f"date of last transaction: {account.date_of_last_transaction}"
            )

    def remove(self):
        if self.is_authenticated:
            user = User.objects.get(username=self.username)
            user.delete()
            print("User has been removed successfully!")
