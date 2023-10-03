# Дан список чисел, необходимо его развернуть без использования метода reverse и
# функции reversed, а так же дополнительного списка и среза

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def number_reversed(number_list):
    start_point = 0
    end_point = len(number_list) - 1
    while start_point < end_point:
        number_list[start_point], number_list[end_point] = number_list[end_point], number_list[start_point]
        start_point += 1
        end_point -= 1
    return number_list


number_reversed(number_list)
print(number_list)
