# Password Strength Checker
# Most common password list: Compile an updated list of the common passwords and check the entered password against this list
# The detailed reason(s) of this final result

most_common_passwords = {
    1: 'password',
    2: '123456',
    3: '12345678',
	4: '1234',
	5: 'qwerty',
	6: '12345',
	7: 'dragon',
	8: 'baseball',
	9: 'football',
    10: 'letmein',
	11: 'monkey',
	12: '696969',
	13: 'abc123',
	14: 'mustang',
    15: 'michael',
	16: 'shadow',
	17: 'jennifer',
	18: '111111',
    19: '2000',
    20: 'jordan',
	21: 'superman',
	22: 'harley',
	23: '1234567',
    24: '1234567',
    25: 'hunter',
    26: 'ranger',
    27: 'thomas',
    28: 'trigger',
	29: 'robert',
	30: 'soccer',
	31: 'batman',
	32: 'test',
	33: 'pass',
	34: 'hockey',
    35: 'george',
	36: 'charlie',
	37: 'andrew',
	38: 'michelle',
	39: 'love',
    40: 'sunshine',
	41: 'jessica',
	42: 'pepper',
	43: 'daniel',
    44: 'access',
    45: '123456789',
	46: '654321',
	47: 'joshua',
	48: 'maggie',
    49: 'starwars',
    50: 'silver',
}

print(most_common_passwords[45])

password_list = [list(most_common_passwords.values())]

print(password_list)

def password_checker():
    password = input("\nEnter in your password: ")
    print(f"\nYour password is {password}.\n")

    if password == password in most_common_passwords.values():
        print("Your password has been rejected, because it is a commonly used password")
    elif password == 'jord':
        print("Your password has still been rejected.")
    else:
        print("Your password has been accepted")

password_checker()


