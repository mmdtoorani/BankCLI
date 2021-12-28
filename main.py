from auth import registration

print("Custom Account Banking Management System")
print("Created By MohamadHosein Toorani & Maede Naderloo\n")
print("-----Welcome To The Main Menu-----\n")

print("1.Create new account")
print("2.Update information of existing account")
print("3.For transactions")
print("4.Check the details of existing account")
print("5.Removing existing account")
print("6.View customer's list")
print("7.Exit\n\n")

choice = input("Enter your choice:\n")

if choice == 1:
    username = input("Enter your username:")
    password = int(input("Enter your password:"))
    registration(username, password)

elif choice == 2:
    pass
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
