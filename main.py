from auth import *
from envvar import *

print(TITLE)
print(LICENCE + "\n")
print("-----Welcome To The Main Menu-----\n")

print(OPTIONS + "\n\n")

choice = int(input("Enter your choice:\n"))

if choice == 1:
    username = input("Enter your username:")
    password = input("Enter your password:")
    user = UserAuthentication(username, password)
    user.registration()

elif choice == 2:
    username = input("Enter your username:")
    password = input("Enter your password:")
    user = UserAuthentication(username, password)

    if user.is_authenticated:
        user.first_name = input("enter your first name: ")
        user.last_name = input("enter your last name: ")
        user.age = input("enter your age: ")
        user.collect_user_info()

elif choice == 3:
    pass

elif choice == 4:
    username = input("Enter your username:")
    password = input("Enter your password:")
    user = UserAuthentication(username, password)
    user.show_info()

elif choice == 5:
    username = input("Enter your username:")
    password = input("Enter your password:")
    user = UserAuthentication(username, password)
    user.remove()

elif choice == 6:
    print(users_list())

elif choice == 7:
    exit()

else:
    msg = "Invalid input! Try again later"
    print(msg)
