import array
import random

def generate_password:
    password = ""
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    lowerchar = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']
    uppperchar =['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<', '}', '{', '^', '&', '_', '-', '+', '!']

    combined = digits + lowerchar + uppperchar + symbols

    ran_digit = random.choice(digits)
    ran_lowercase = random.choice(lowerchar)
    ran_uppercase = random.choice(uppperchar)
    ran_symbols = random.choice(symbols)

    required = ran_digit + ran_symbols + ran_lowercase + ran_uppercase

    length = 8

    for x in range(length - 4):
        required = required + random.choice(combined)
        pass_array = array.array('u', required)
        random.shuffle(pass_array)

    for x in pass_array:
        password = password + x

    print(password)
