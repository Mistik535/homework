# Дан список чисел, необходимо для каждого элемента посчитать сумму его соседей,
# для крайних чисел одним из соседей является число с противоположной стороны списка

def calculating(number_list):
    counted_list = []
    length = len(number_list)
    for i in range(length):
        left_border = number_list[(i - 1) % length]
        right_border = number_list[(i + 1) % length]
        summary = left_border + right_border
        counted_list.append(summary)
    return counted_list


random_list = [3, 5, 4, 54, 232, 78, 11, 23, 7, 65, 23, 1000]
summary = calculating(random_list)
print(summary)


