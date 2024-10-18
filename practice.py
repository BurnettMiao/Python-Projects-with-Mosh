<<<<<<< HEAD:practice.py
# def read_words():
#     try:
#         with open('words.txt', 'r') as file:
#             words = file.read().splitlines()
#             return words
#     except FileExistsError:
#         print('words.txt does not exist.')
#         return []

# def read_words():
#     try:
#         with open('words.txt', 'r') as file:
#             words = file.read().splitlines()
#             return words
#     except FileExistsError:
#         print('Words.txt does not exist.')
#         return []

def read_words():
    try:
        with open('word.txt', 'r') as file:
            words = file.read().splitlines()
            return words
    except FileNotFoundError:
        print('Words.txt does not exist.')
        return []

def main():
    words = read_words()
    print(words)


if __name__ == '__main__':
    main()


=======
>>>>>>> 0315646907d1ef396d4b3f9ba792b9c66a6e8981:test.py
