library = {
    '我是書名': {'author': '我是作者', 'is_read': False},
    'book one': {'author': 'author', 'is_read': False},
}

# 顯示選單
def show_menu():
    print("\n===== 個人圖書館 =====")
    print("1. 新增書籍")
    print("2. 標記書籍為已讀")
    print("3. 刪除書籍")
    print("4. 查看所有書籍")
    print("5. 退出")

# 確認使用者輸入狀態
def check_user_input(prompt):
    while True:
        name = input(prompt)
        # 移除多餘空白，並檢查是否為空
        if not name or not name.strip():
            print('invalid string')
            continue
        # 將連續多個空格壓縮成單個空格
        name = " ".join(name.split())
        return name

# 新增書籍
def add_book():
    check_book_prompt = "輸入書名: "
    book_name = check_user_input(check_book_prompt)
    # print(book_name)
    check_author_prompt = "請輸入作者: "
    author = check_user_input(check_author_prompt)
    # print(author)
    library[book_name] = {'author': author, 'is_read': False}

    print(f"\n書名: {book_name}已新增")

# 標記書籍為已讀
def mark_as_read():
    check_book_prompt = "輸入要標記為已讀的書名: "
    book_name = check_user_input(check_book_prompt)

    if book_name in library:
        library[book_name]['is_read'] = True
        print(f"\n{book_name}標記為已讀")
    else:
        print('\n找不到相關書名')

# 刪除書籍
def delete_book():
    check_book_prompt = "輸入要刪除的書名: "
    book_name = check_user_input(check_book_prompt)

    if book_name in library:
        del library[book_name]
        print(f"\n{book_name}已刪除")
    else:
        print('\n找不到相關書籍')

# 查看所有書籍
def view_books():
    if not library:
        print('\n目前沒有收藏的書籍')
    else:
        print('===== 書籍清單 =====')
        for name, details in library.items():
            status = "已讀" if details['is_read'] else "未讀"
            print(f"\n書名: {name}, 作者: {details['author']}, 狀態: {status}")

# 確認使用者是否輸入正確操作數字
def check_input_number():
    operator_number = ('1', '2', '3', '4', '5')
    while True:
        user_input = input('\n選擇操作(1-5): ').strip()
        if user_input not in operator_number:
            print('請輸入正確數字(1-5)')
            continue
        else:
            return user_input
        
# 主程式迴圈
def main():
    while True:
        show_menu()
        choice = check_input_number()
        if choice == '1':
            add_book()
        elif choice == '2':
            mark_as_read()
        elif choice == '3':
            delete_book()
        elif choice == '4':
            view_books()
        else:
            print("\n退出圖書館管理系統")
            break

if __name__ == '__main__':
    main()

        





# # GPT 給的練習範例

# # 初始化一個空的圖書館字典
# library = {}

# # 顯示選單
# def show_menu():
#     print("\n==== 個人圖書館 ====")
#     print("1. 新增書籍")
#     print("2. 標記書籍為已讀")
#     print("3. 刪除書籍")
#     print("4. 查看所有書籍")
#     print("5. 退出")

# # 新增書籍
# def add_book():
#     name = input("輸入書名: ")
#     author = input("輸入作者: ")
#     library[name] = {'author': author, 'read': False}
#     print(f"書籍 '{name}' 已新增。")

# # 標記書籍為已讀
# def mark_as_read():
#     name = input("輸入要標記為已讀的書名: ")
#     if name in library:
#         library[name]['read'] = True
#         print(f"書籍 '{name}' 已標記為已讀。")
#     else:
#         print("書籍不存在。")

# # 刪除書籍
# def delete_book():
#     name = input("輸入要刪除的書名: ")
#     if name in library:
#         del library[name]
#         print(f"書籍 '{name}' 已刪除。")
#     else:
#         print("書籍不存在。")

# # 查看所有書籍
# def view_books():
#     if not library:
#         print("圖書館目前沒有書籍。")
#     else:
#         print("\n==== 書籍清單 ====")
#         for name, details in library.items():
#             status = "已讀" if details['read'] else "未讀"
#             print(f"書名: {name}, 作者: {details['author']}, 狀態: {status}")

# # 主程式迴圈
# while True:
#     show_menu()
#     choice = input("選擇操作 (1-5): ")
#     if choice == '1':
#         add_book()
#     elif choice == '2':
#         mark_as_read()
#     elif choice == '3':
#         delete_book()
#     elif choice == '4':
#         view_books()
#     elif choice == '5':
#         print("退出圖書館管理系統。")
#         break
#     else:
#         print("無效的選擇，請重新輸入。")
