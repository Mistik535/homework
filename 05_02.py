# Сделать калькулятор: у пользователя спрашивается число, потом действие и второе число

first_number = float(input("Введите первое число"))
choice = int(input("Выберите действие:\n 1. Сложение\n 2. Вычитание\n 3. Умножение\n 4. Деление"))
second_number = float(input("Введите второе число"))
if choice == 1:
    plus = first_number + second_number
    print("Ваш результат сложения", plus)
elif choice == 2:
    minus = first_number - second_number
    print("Ваш результат вычитания", minus)
elif choice == 3:
    multiple = first_number * second_number
    print("Ваш результат умножения", multiple)
elif choice == 4:
    division = first_number // second_number
    print("Ваш результат деления", division)
