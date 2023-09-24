# Вывести первые N чисел кратные M и больше K

n = int(input("Введите первое число"))
m = int(input("Введите второе число"))
k = int(input("Введите третье число"))

s = k
while n != 0:
    if s % m == 0 and s > k:
        n -= 1
        print(s, end=" ")

    s += 1
