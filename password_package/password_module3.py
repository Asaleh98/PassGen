import getpass

def get_pass():
     print("Password must be between 8 and 18 characters long")
     print("Password must contain at least one upper case letter, and one lower case letter")
     print("Password must contain at least one integer, and one special character from [!_@$#*+-?~]")
     password = getpass.getpass("Please enter password: ")
     return password

# Has to meet constraints to be valid password

#make it so you can re-enter password if constraint not met

def password_constraints(password):
    special_sym = ["!", "_", "$", "@", "*", "&", "#", "~", "?"]

    if len(password) < 8:
        print("Password length should be at least 8")

    elif len(password) > 18:
        print("Password length should be not be greater than 18")

    elif not any(char.isdigit() for char in password):
        print("Password should have at least one numeral")

    elif not any(char.isupper() for char in password):
        print("Password should have at least one uppercase letter")

    elif not any(char.islower() for char in password):
        print("Password should have at least one lowercase letter")

    elif not any(char in special_sym for char in password):
        print("Password should have at least one of the symbols [!_@$#*+-?~]")

    else:
        return password


def password_username(password, fname, lname, birthdate):
    password_lower = password.lower()
    fname_lower = fname.lower()
    lname_lower = lname.lower()

    if fname_lower in password_lower or lname_lower in password_lower:
        print("Password can not contain first or last name!")

    elif str(birthdate) in password:
        print("Password can not contain birth date!")
    else:
        return password


def common_passwords(password):
    most_common_passwords = (
    'password',
    '123456',
    '12345678',
	'1234',
	'qwerty',
	'12345',
	'dragon',
	'baseball',
	'football',
    'letmein',
	'monkey',
	'696969',
	'abc123',
	'mustang',
    'michael',
	'shadow',
	'jennifer',
	'111111',
    '2000',
    'jordan',
	'superman',
	'harley',
	'1234567',
    '1234567',
    'hunter',
    'ranger',
    'thomas',
    'trigger',
	'robert',
	'soccer',
	'batman',
	'test',
	'pass',
	'hockey',
    'george',
	'charlie',
	'andrew',
	'michelle',
	'love',
    'sunshine',
	'jessica',
	'pepper',
	'daniel',
    'access',
    '123456789',
	'654321',
	'joshua',
	'maggie',
    'starwars',
    'silver',
)

#    print(most_common_passwords[0])

# def password_checker():
#     password = input("\nEnter in your password: ")
#     print(f"\nYour password is {password}.\n")

    common_password_character_checker = any(item in password for item in most_common_passwords)

    if password == password in most_common_passwords:
        print("Your password has been rejected, because it is a commonly used password")
        exit()
    elif common_password_character_checker == True:
        print("Your password has been rejected, because it contains characters from a commonly used password.")
        exit()
    else:
        print("Your password has been accepted")
        return password

# error if password contains item from common list




#can remove some if the minimum valid password is 8 char long





def password_strength(password):
    if len(password) > 12:
        result = "Your password strength is strong. Password strength is usually measured in terms of information entropy. The length of a password is by far the largest determinant of entropy. The longer a password is, the higher the entropy, and thus the less likely it is to succumb to brute-force searches. Passwords chosen by humans tend to be more easily brute-forced than entropy suggests, since they often contain commonly used phrases, as well as information relating to the user's name or birth date. This programme automatically rejects such passwords for this very reason.  "
        return result

    elif len(password) > 10 and len(password) <= 12:
        result = "Your password strength is medium. Password strength is usually measured in terms of information entropy. The length of a password is by far the largest determinant of entropy. The longer a password is, the higher the entropy, and thus the less likely it is to succumb to brute-force searches. Passwords chosen by humans tend to be more easily brute-forced than entropy suggests, since they often contain predictable phrases and information relating to the user's name or birth date. This programme automatically rejects such passwords for this very reason. "
        return result
    else:
        result = "Your password strength is weak. Password strength is usually measured in terms of information entropy. The length of a password is by far the largest determinant of entropy. The longer a password is, the higher the entropy, and thus the less likely it is to succumb to brute-force searches. Passwords chosen by humans tend to be more easily brute-forced than entropy suggests, since they often contain predictable phrases and information relating to the user's name or birth date. This programme automatically rejects such passwords for this very reason. "
        return result
