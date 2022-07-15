# Реализуйте алгоритм перемешивания списка.


def randomize(rand_list: list) -> list:
    import random
    r = int
    for i in range(0, len(rand_list)-1):
        r = random.randint(0, i) - 1
        temp = rand_list[i]
        rand_list[i] = rand_list[r]
        rand_list[r] = temp
    return rand_list


num = int(input('Введите количество элементов списка: '))

origin_position_list = []
for i in range(1, num+1):
    origin_position_list.append(i)
print(origin_position_list)
print(randomize(origin_position_list))

# способ средствами Python:

# import random
# random.shuffle(origin_position_list)
# print(origin_position_list)
