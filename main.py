from auth import registration, is_user_exist, is_user_valid, collect_user_info, is_name_valid
from envvar import *

print(TITLE)
print(LICENCE + "\n")
print("-----Welcome To The Main Menu-----\n")

print(OPTIONS + "\n\n")

choice = int(input("Enter your choice:\n"))

if choice == 1:
    username = input("Enter your username:")
    password = input("Enter your password:")

    if not is_user_exist(username):
        registration(username, password)
        msg = "You registered successfully!"
    else:
        msg = "ERROR: User already exists...!"

    print(msg)


elif choice == 2:
    username = input("Enter your username:")
    password = input("Enter your password:")

    if is_user_exist(username):
        if is_user_valid(username, password):
            first_name = input("enter your first name: ")
            last_name = input("enter your last name: ")
            age = input("enter your age: ")
            if is_name_valid(first_name) and is_name_valid(last_name):
                try:
                    int(age)
                except ValueError:
                    msg = "Invalid input! Try again"

                collect_user_info(username, first_name, last_name, age)
                msg = 'your account has been updated!'

            else:
                msg = "Invalid input! Try again"
        else:
            msg = "Invalid password!"
    else:
        msg = "You have not registered!"

    print(msg)


elif choice == 3:
    pass

elif choice == 4:
    pass

elif choice == 5:
    pass

elif choice == 6:
    pass

elif choice == 7:
    pass
