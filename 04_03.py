# Заполнить словарь где ключами будут выступать числа от 0 до n, а
# значениями вложенный словарь с ключами "name" и "email", а значения
# для этих ключей будут браться с клавиатуры

n = int(input("Введите число: "))
user_dict = {main_dict:
                 {"name": input("Введите name: "), "email": input("Введите email: ")}
             for main_dict in range(0, n)}
print(user_dict)
