# Read the list of words from a file (words.txt)
# Choose a random word
# Attempts = 6
# Loop attempts > 0
#   Display word
#       For each letter in secret word
#           If user guess that letter
#               Print it
#           Else
#               Print _
#   Ask the user to enter a letter
#   Validate input
#       Single character
#       Only a - z
#       Not duplicate
#   If letter is in the secret word
#       Print good guess
#       Check if word is guessed
#           For each letter in secret word
#               If letter is not in the list of guessed letters
#                   The word is not guessed
#           Print congratulations
#           Break
#   Else
#       Print wrong guess
#       Decrement attempts

import random

def read_words():
    try:
        with open('words.txt', 'r') as file:
            words = file.read().splitlines()
            return words
    except FileExistsError:
        print('words.txt does not exist.')
        return []


def main():
    words = read_words()
    secret_word = random.choice(words)
    print(secret_word)


if __name__ == '__main__':
    main()