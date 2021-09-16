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

print(most_common_passwords[0])

def password_checker():
    password = input("\nEnter in your password: ")
    print(f"\nYour password is {password}.\n")

    common_password_character_checker = any(item in password for item in most_common_passwords)

    if password == password in most_common_passwords:
        print("Your password has been rejected, because it is a commonly used password")
    elif common_password_character_checker == True:
        print("Your password has been rejected, because it contains characters from a commonly used password.")
    else:
        print("Your password has been accepted")

password_checker()