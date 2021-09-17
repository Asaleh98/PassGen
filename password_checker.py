from password_package import constraints_class
from password_package import generate_class
import sqlite3
from contextlib import closing

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

    confirmation = input("Are your details correct? (y/n): ")
    confirmation = confirmation.lower()

    if confirmation == 'y':
        return fname, lname, birthdate

    elif confirmation == 'n':
        cont = input("Would you like to retry? (y/n): ")
        cont = cont.lower()

        if cont == 'y':
            return user_input()
        else:
            exit()

def get_pass():
     print("Password must be between 8 and 18 characters long")
     print("Password must contain at least one upper case letter, and one lower case letter")
     print("Password must contain at least one integer, and one special character from [!_@$#*+-?~|^]")
     password = input("Please enter password: ")
     return password

if __name__ == "__main__":
    try:
        user_choice()

        if choice == 1:
            user_input()
            password = get_pass()

            constraints_object = constraints_class.Constraints(fname, lname, birthdate, password)
            result = str(constraints_object.strength_report())
            result = result.replace(', ', '\n')

        elif choice == 2:
             generate_object = generate_class.Generate_password()
             result = str(generate_object.generate_password())
        elif choice == 3:
             exit()
        else:
            user_choice()

        export_file = input("Would you like to export results to a text file? y/n: ")
        export_file = export_file.lower()

        if export_file == "y":
            file = open("result.txt", "a+")
            data = file.write('\n' + result + '\n')
            file.close()
            print("Results successfuly exported to a text file")
        elif export_file == "n":
            pass

    except Exception as e:
        print(e)
        print("Error! Try again")
