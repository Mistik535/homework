# Дан список рандомных чисел, необходимо отсортировать его в виде, сначала четные, потом нечётные


def sorting(numbers):
    return numbers % 2, numbers


random_list = [4, 5, 3, 3434, 67, 3, 7878, 6, 14, 46, 1123, 13, 17, 673, 324]
sorted_list = sorted(random_list, key=sorting)
print(sorted_list)
