# Заполнить список степенями числа 2 (от 2^1 до 2^n)

user_number = int(input())
print([2 ** i for i in range(1, user_number, 1)])
