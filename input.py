from password_package import constraints_class
from password_package import generate_class
from password_package import file_export

print("Welcome to the password stength checker / generator!")

def user_input():
    global result
    user_choice = None
    while True:

        while True:
            option = input("Press 1 to create own password. Press 2 to use password generator. Press 3 to exit: ")
            if option in ('1', '2', '3'):
                user_choice = option
                break
            else:
                print("Choose a valid option")

        if user_choice == '3':
            break

        fname = input("Please enter first name: ")
        lname = input("Please enter last name: ")

        birthdate = input("Please enter birthdate (yyyy): ")
        birthdate = int(birthdate)

        if user_choice == '1':
            print("------------------------------ PASSWORD POLICY ------------------------------")
            print("Password must be between 8 and 18 characters long")
            print("Password must contain at least one upper case letter, and one lower case letter")
            print("Password must contain at least one integer, and one special character from [!_@$#*+-?~|^]")
            print("------------------------------ ENTER PASSWORD -------------------------------")
            password = input("Please enter password: ")

            constraints_object = constraints_class.Constraints(fname, lname, birthdate, password)
            result = str(constraints_object.strength_report())
            result = result.replace(', ', '\n')

            file_object = file_export.Export()
            file_object.export_file(result)

        elif user_choice == '2':
            generate_object = generate_class.Generate_password()
            result = str(generate_object.generate_password())

            file_object = file_export.Export()
            file_object.export_file(result)

if __name__ == "__main__":

    user_input()
