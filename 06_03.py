# Дан список чисел и на вход поступает число N, необходимо сместить список на
# указанное число, пример: [1,2,3,4,5,6,7] N=3 ответ: [5,6,7,1,2,3,4]


ready_list = [1, 2, 3, 4, 5, 6, 7]


def list_moving(ready_list, steps):
    if steps < 0:
        steps = abs(steps)
        for i in range(steps):
            ready_list.append(ready_list.pop(0))
    else:
        for i in range(steps):
            ready_list.insert(0, ready_list.pop())


list_moving(ready_list, 3)
print(ready_list)
