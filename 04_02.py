# Без использования collections, написать программу, которая будет
# создавать словарь для подсчитывания количества вхождений каждой
# буквы в текст введенный с клавиатуры

user_text = input("Введите текст")
user_dict = {char: user_text.count(char) for char in user_text}
print(user_dict)
