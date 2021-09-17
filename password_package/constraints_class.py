
class Constraints:

    def __init__(self, fname, lname, birthdate, password):
        self.fname = fname
        self.lname = lname
        self.birthdate = birthdate
        self.password = password

    def length(self):
        counter = True
        if len(self.password) < 8 or len(self.password) > 18:
            counter = False
#            print("Password length should be between 8 and 18")
            return "- Password length is not between 8 and 18", '!'

        return f"- Password length is {len(self.password)}"

    def numbers(self):
        counter = True
        if not any(char.isdigit() for char in self.password):
            counter = False
#            print("Password should have at least one numeral")
            return "- Password does not contain any numbers", '!'

        return "- Password contains numbers"

    def letters(self):
        counter = True
        if not any(char.isupper() for char in self.password):
            counter = False
            return "- Password does not contain any upper case letters", '!'
        if not any(char.islower() for char in self.password):
            counter = False
            return "- Password does not contain any lower case letters", counter

        return "- Password contains a mix of upper and lower case letters"

    def symbols(self):
        counter = True
        special_sym = ["!", "_", "$", "@", "*", "&", "#", "~", "?", "|", ":", "^", "+"]
        if not any(char in special_sym for char in self.password):
            counter = False

            return "- Password does not contain any symbols", '!'

        return "- Password contains symbols"

    def password_username(self):
        counter = True
        password_lower = self.password.lower()
        fname_lower = self.fname.lower()
        lname_lower = self.lname.lower()

        if fname_lower in password_lower or lname_lower in password_lower or str(self.birthdate) in self.password:
            counter = False
            return "- Password contains name or birthdate", '!'

        return "- Password does not contain name or birthdate"

    def common_passwords(self):
        counter = True
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

        common_password_character_checker = any(item in self.password for item in most_common_passwords)

        if self.password in most_common_passwords:
            counter = False
            return "- Your password is a commonly used password", '!'

        elif common_password_character_checker == True:
            counter = False
            return "- Your password contains characters from a commonly used password", '!'

        return "- Your password is not commonly used"

    # def report(self):
    #     if not self.length():
    #         return "Password length is not between 8 and 18"
    #     if not self.numbers():
    #         return "Password does not contain numbers"
    #     if not self.letters():
    #         return "Password does not contain a mix of upper and lower case letters"
    #     if not self.symbols():
    #         return "Password does not contain symbols"
    #     if not self.password_username():
    #         return "Password contains your name and/or birthdate"
    #     if not self.common_passwords():
    #         return "Your password is a commonly used password"
    #
    #     if not self.length() or not self.numbers() or not self.letters() or not self.symbols() or not self.password_username() or not self.common_passwords():
    #         return "Password = WEAK"
    #
    #     else:
    #         return "Password = Strong"


    def strength_report(self):
        passwd = f"Your Password is: {self.password}"
        intro = "If one constraint is not met your password will be deemed WEAK"

        print(intro)
        print(passwd)
        print(self.length())
        print(self.numbers())
        print(self.letters())
        print(self.symbols())
        print(self.password_username())
        print(self.common_passwords())

        if '!' in self.length() or '!' in self.numbers() or '!' in self.letters() or '!' in self.symbols() or '!' in self.password_username() or '!' in self.common_passwords():
             strength = "Password = WEAK"
             print(strength)
        else:
             strength = "Password = STRONG"
             print(strength)

        return passwd, intro, self.length(), self.numbers(), self.letters(), self.symbols(), self.password_username(), self.common_passwords(), strength













# def main():
#         constraints_object = Constraints(fname, lname, birthdate, password)
#         constraints_object.password_constraints()
#         constraints_object.password_username()
#         constraints_object.common_passwords()
#         print(constraints_object.password_strength())
