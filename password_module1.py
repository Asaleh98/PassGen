
# Has to meet constraints to be valid password

def password_constraints(password):
    special_sym = ["!", "_", "$", "@", "*", "&", "#", "~", "?"]

    if len(password) < 8:
        print("Password length should be at least 8")

    if len(password) > 18:
        print("Password length should be not be greater than 18")

    if not any(char.isdigit() for char in password):
        print("Password should have at least one numeral")

    if not any(char.isupper() for char in password):
        print("Password should have at least one uppercase letter")

    if not any(char.islower() for char in password):
        print("Password should have at least one lowercase letter")

    if not any(char in special_sym for char in password):
        print("Password should have at least one of the symbols [!_@$#*+-?~]")
    else:
        return password

# Valid passport can not contain the users name or birthdate

def password_user_name(password, fname, lname, birthdate):
    password_lower = password.lower()
    fname_lower = fname.lower()
    lname_lower = lname.lower()

    if fname_lower in password_lower or lname_lower in password_lower:
        print("Password can not contain first or last name!")

    elif str(birthdate) in password:
        print("Password can not contain birth date!")
    else:
        return password

# Determines password strength based on length

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
