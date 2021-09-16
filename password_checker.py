from password_package import password_module3
from password_package import password_generator
import getpass
import sqlite3
from contextlib import closing

"""
Password Policy:

- Password must be at least 8 characters long
- Password must contain at least one upper case letter, and one lower case letter
- Password must contain at least one integer
- Password must contain at least one special character from [!_@$#*+-?~<^>|]

"""

print("Welcome to the password stength checker / generator!")

def user_choice():
    global choice

    choice = input("Press 1 to create own password. Press 2 to use password generator. Press 3 to exit: ")
    choice = int(choice)

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


try:

    user_choice()

    if choice == 1:
        user_input()
        password = password_module3.get_pass()
        password = password_module3.password_constraints(password)
        password = password_module3.password_username(password, fname, lname, birthdate)
        password_valid = password_module3.common_passwords(password)
        print(password_module3.password_strength(password_valid))
        result = password_module3.password_strength(password_valid)
    elif choice == 2:
         password_generator.generate_password()
    elif choice == 3:
         pass
    else:
        user_choice()

    export_file = input("Would you like to export results to a text file? y/n: ")
    export_file = export_file.lower()

    if export_file == "y":
        file = open("result.txt", "w")
        data = file.write(result)
        file.close()
        print("Results successfuly exported to a text file")

    elif export_file == "n":
        print("Goodbye!")

except Exception as e:
    print("Error! Try again")


# user_choice()
#
# if choice == 1:
#     user_input()
#     password = password_module3.get_pass()
#     password = password_module3.password_constraints(password)
#     password = password_module3.password_username(password, fname, lname, birthdate)
#     password_valid = password_module3.common_passwords(password)
#     print(password_module3.password_strength(password_valid))
#     result = password_module3.password_strength(password_valid)
# elif choice == 2:
#      password_generator.generate_password()
# elif choice == 3:
#      pass
# else:
#     user_choice()
#
# export_file = input("Would you like to export results to a text file? y/n: ")
# export_file = export_file.lower()
#
# if export_file == "y":
#     file = open("result.txt", "w")
#     data = file.write(result)
#     file.close()
#     print("Results successfuly exported to a text file")
#
# elif export_file == "n":
#     print("Goodbye!")
