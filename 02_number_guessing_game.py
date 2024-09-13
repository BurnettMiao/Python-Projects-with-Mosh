# Generate a random number
# Loop
    # Ask the user to make a guess
    # If not a valid number
        # Print an error
    # If number < guess
        # Print too low
    # If number > guess
        # Print too high
    # Else
        # Print well done

import random

number_to_guess = random.randint(1, 100)

while True:
    try:
        guess = int(input('Guess the number between 1 and 100: '))

        if guess < number_to_guess:
            print('Too low!')
        elif guess > number_to_guess:
            print('Too High!')
        else:
            print(f'Congratulations! You guessed the number {number_to_guess}.')
            break

    except ValueError:
        print('Please enter a valid number')

