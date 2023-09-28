# Написать функцию перевода десятичного числа в двоичное и обратно, без использования функции int

def transform(number):
    binary = bin(number)
    return binary[2:]

print(transform(5))

def transform_2(number_2):
    decimal = ""
    while number_2 > 0:
        divide = number_2 % 2
        decimal = str(divide) + decimal
        number_2 = number_2 // 2
    return decimal if decimal else "0"

print(transform_2(5))

def binary_reverse(binary):
    decimal = 0
    binary = binary[::-1]
    for i in range(len(binary)):
        if binary[i] == '1':
            decimal += 2 ** i
    return decimal

print(binary_reverse(str(10111)))