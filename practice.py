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


# practice
# def read_words():
#     try:
#         with open('word.txt', 'r') as file:
#             words = file.read().splitlines()
#             return words
#     except FileNotFoundError:
#         print('Words.txt does not exist.')
#         return []

# def main():
#     words = read_words()
#     print(words)


# if __name__ == '__main__':
#     main()

def main():
    try:
        value = int(input('請輸入一個數字: '))
        result = 10 / value
        print(result)
    except Exception as e:
        print(f'發生錯誤: {e}')


# def main():
#     value = int(input('請輸入一個數字: '))
#     result = 10 / value
#     print(result)
    

if __name__ == '__main__':
    main()