# Пользователь вводит 3 числа, сказать сколько из них положительных и сколько отрицательных

a = float(input("Введите число"))
b = float(input("Введите число"))
c = float(input("Введите число"))

count_pos = (a > 0) + (b > 0) + (c > 0)
count_neg = 3 - count_pos

print(f"Здесь {count_neg} отрицательных и {count_pos} положительных чисел")
