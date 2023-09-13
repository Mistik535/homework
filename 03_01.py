# Пользователь вводит предложение, заменить все пробелы на "-" 2-мя способами

# 1 способ
user_01 = input("Введите любой текст")
auto_split = user_01.split(" ")
auto_change = "-".join(auto_split)
print(auto_change)

# 2 способ
user_02 = input("Введите любой текст")
print(user_02.replace(" ", "-"))
