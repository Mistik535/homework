# **Вывести четные числа от 2 до N по 5 в строку

n = int(input("Введите число: "))
count = 0
for i in range(2, n + 1):
    if i % 2 == 0:
        print(i, end=" ")
        count += 1
        if count == 5:
            print("")
            count = 0
