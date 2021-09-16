from password_package import password_module2
import getpass
import sqlite3
from contextlib import closing

"""
Password Policy:

- Password must be at least 8 characters long
- Password must contain at least one upper case letter, and one lower case letter
- Password must contain at least one integer
- Password must contain at least one special character from [!_@$#*+-?~]

"""

def user_input():
    global fname
    global lname
    global birthdate

    fname = input("Please enter first name: ")
    lname = input("Please enter last name: ")
    birthdate = input("Please enter birthdate (yyyy): ")
    birthdate = int(birthdate)

    print(f"Your name is {fname} {lname}")
    print(f"Your birthdate is {birthdate}")

    confirmation = input("Are your details correct? (y/n): ")
    confirmation = confirmation.lower()

    if confirmation == 'y':
        return fname, lname, birthdate

    elif confirmation == 'n':
        cont = input("Would you like to continue? (y/n): ")
        cont = cont.lower()

        if cont == 'y':
            return user_input()
        else:
            exit()

def user_choice():
    global choice

    choice = input("Press 1 to create own password. Press 2 to use password generator. Press 3 to exit: ")
    choice = int(choice)


try:
    user_input()
    user_choice()

    if choice == 1:
        password = password_module2.get_pass()
        password_valid = password_module2.password_constraints(password, fname, lname, birthdate)
        print(password_module2.password_strength(password_valid))

    elif choice == 2:
        pass

    elif choice == 3:
        pass

    else:
        user_choice()

#     export_file = input("Would you like to export results to a text file? y/n: ")
#     export_file = export_file.lower()
#
#     if export_file == "y":
#         file = open("result.txt", "w")
#         data = file.write(results)
#         file.close()
#
#     elif export_file == "n":
#         print("Goodbye!")
#
#
except Exception as e:
    print("Error! Try again")
#
# user_input()
#
# user_choice()
#
# if choice == 1:
#     password = password_module2.get_pass()
#     password_valid = password_module2.password_constraints(password, fname, lname, birthdate)
#     print(password_module2.password_strength(password_valid))
# elif choice == 2:
#     pass
# elif choice == 3:
#     pass
# else:
#     user_choice()
