# Generate a secret number with unique digits
# Loop
#   Ask the user to make a guess
#   Validate the guess (4 digits - unique)
#   If invalid
#       Print an error
#       Continue
#   Else
#       Calculate cows and bulls
#           For each digit in the guess
#               If digit exists in the same position in the secret
#                   Increment bulls
#               If digit exists in the secret
#                   Increment cows
#       Print cows and bulls
#       If bulls == 4
#           Print message
#           Break

import random

def generate_secret():
    digits = list(range(10))
    random.shuffle(digits)

    return ''.join([str(digit) for digit in digits[:4]])



def calculate_cows_and_bulls(secret, guess):
    bulls = sum([1 for i in range(4) if guess[i] == secret[i]])
    cows = sum([1 for i in range(4) if guess[i] == secret]) - bulls

    return cows, bulls


def main():
    secret = generate_secret()
    while True:
        guess = input('Guess: ')
        if len(guess) == 4 and guess.isdigit() and len(set(guess)) == 4:
            cows, bulls = calculate_cows_and_bulls(secret, guess)
            print(f'{cows} cows, {bulls} bulls')

            if bulls == 4:
                print('Congratulations! You guessed the current number')
                break
        
        else:
            print('Invalid guess. Please enter a 4-digit number with unique digits.')


if __name__ == '__main__':
    main()