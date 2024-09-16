import os

# def main():
#     directory = r'C:\Users\burnett\Desktop\a發音'
#     file_count = 0  # 初始化檔案數量的計數器
    
#     for filename in os.listdir(directory):
#         f = os.path.join(directory, filename)
#         if os.path.isfile(f):
#             file_count += 1  # 每當找到一個檔案，計數器加一

#     print(f"資料夾裡有 {file_count} 個檔案")


# def main():
#     directory = r'C:\Users\burnett\Desktop\a發音'
#     file_count = 0

#     for dirpath, dirname, filenames in os.walk(directory):
#         print(f"1 {dirpath}")
#         print(f"2 {dirname}")
#         print(f"3 {filenames}")
#         file_count += len(filenames)
    
#     print(f"資料夾裡面有{file_count}個檔案")

# def main():
#     directory = r'C:\Users\burnett\Desktop\a發音'

#     for filename in os.listdir(directory):
#         file_path = os.path.join(directory, filename)
#         if os.path.isfile(file_path):
#             file_name_without_extension, extension = os.path.splitext(filename)
#             print(file_name_without_extension)

def main():
    print(os.getcwd())


if __name__ == '__main__':
    main()