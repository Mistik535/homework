# Пользователь вводит Имя, Возраст и Город, сформировать
# приветственное сообщение путем форматирования 3-мя способами

name = str(input("Введите имя"))
age = int(input("Введите возраст"))
city = input("Введите название города")

print("Привет! Меня зовут %s. Мне %s лет. Я из города %s." % (name, age, city))
print("Привет! Меня зовут {}. Мне {} лет. Я из города {}.".format(name, age, city))
print(f"Привет! Меня зовут {name}. Мне {age} лет. Я из города {city}.")