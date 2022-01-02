from auth import *
from envvar import *

print(TITLE)
print(LICENCE + "\n")
print("-----Welcome To The Main Menu-----\n")

print(OPTIONS)

choice = input("Enter your choice:\n")

if choice == '1':
    username = input("Enter your username:")
    password = input("Enter your password:")
    user = UserAuthentication(username, password)
    user.registration()

elif choice == '2':
    username = input("Enter your username:")
    password = input("Enter your password:")
    user = UserAuthentication(username, password)

    if user.is_authenticated:
        user.first_name = input("enter your first name: ")
        user.last_name = input("enter your last name: ")
        user.age = input("enter your age: ")
        user.collect_user_info()

elif choice == '3':
    username = input("Enter your username:")
    password = input("Enter your password:")
    user = UserAuthentication(username, password)

    if user.is_authenticated:
        dest_username = input("Enter the username of the destination account holder: ")
        dest_user = UserAuthentication(dest_username)

        if dest_user.is_user_exist:
            amount = input("Enter the amount: ")
            trx = Transactions(amount)
            trx.transfer(username, dest_username)
        else:
            print('This username does not exists!')

elif choice == '4':
    username = input("Enter your username:")
    password = input("Enter your password:")
    user = UserAuthentication(username, password)
    user.show_info()

elif choice == '5':
    username = input("Enter your username:")
    password = input("Enter your password:")
    user = UserAuthentication(username, password)
    user.remove()

elif choice == '6':
    print(users_list())

elif choice == '7':
    exit()

else:
    msg = "Invalid input! Try again later"
    print(msg)
