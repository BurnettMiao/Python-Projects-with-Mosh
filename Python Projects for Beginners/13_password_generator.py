import string
import random


def generate_password(length, include_uppercase, include_numbers, includes_special):
    if length < (include_uppercase + include_numbers + includes_special):
        raise ValueError('Password length is too short for the specified criteria.')

    password = ''

    if include_uppercase:
        password += random.choice(string.ascii_uppercase)
        print(f'Password include uppercase: {password}')
    if include_numbers:
        password += random.choice(string.digits)
        print(f'Password include number: {password}')
    if includes_special:
        password += random.choice(string.punctuation)
        print(f'Password include special: {password}')
    
    # Fill the remaining length with any allowed characters


    # abcd...zABCD...Z1234...9!@#$%^&*()
    characters = string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if includes_special:
        characters += string.punctuation

    for _ in range(length - len(password)):
        password += random.choice(characters)

    password_list = list(password)
    random.shuffle(password_list)
    return ''.join(password_list)



def main():
    length = int(input('Enter password length: '))
    include_uppercase = input('Include uppercase letters? (y/n): ').lower() == 'y'
    include_numbers = input('Include numbers? (y/n): ') == 'y'
    include_special = input('Include special characters? (y/n): ') == 'y'

    try:
        password = generate_password(length, include_uppercase, include_numbers, include_special)
        print(password)
    except ValueError as e:
        print(e)


if __name__ == '__main__':
    main()