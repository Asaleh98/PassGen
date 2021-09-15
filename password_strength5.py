from password_package import password_module1
import getpass

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
        pass
    elif confirmation == 'n':
        user_input()

#Hide password

def user_choice():
    global choice
    global password

    choice = input("Press 1 to create own password. Press 2 to use password generator. Press 3 to exit: ")
    choice = int(choice)

    if choice == 1:
        print("Password must be between 8 and 18 characters long")
        print("Password must contain at least one upper case letter, and one lower case letter")
        print("Password must contain at least one integer, and one special character from [!_@$#*+-?~]")
        password = getpass.getpass("Please enter password: ")

    elif choice == 2:
        pass

    elif choice == 3:
        exit()
    else:
        user_choice()

try:
    user_input()
    user_choice()

    password = password_module1.password_constraints(password)

    password = password_module1.password_user_name(password, fname, lname, birthdate)

    print(password_module1.password_strength(password))

    results = password_module1.password_strength(password)

    export_file = input("Would you like to export results to a text file? y/n: ")
    export_file = export_file.lower()

    if export_file == "y":
        file = open("result.txt", "w")
        data = file.write(results)
        file.close()

    elif export_file == "n":
        print("Goodbye!")


except Exception as e:
    print("Error! Try again")
