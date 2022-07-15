# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# позиции задаются с клавиатуры через пробел.

def list_Input(N:int) -> list:
    a = []
    from random import randint
    for i in range(0, N):
        i = randint(-N, N)
        a.append(i)
    return a


num = int(input('Введите количество элементов списка: '))
user_list = list_Input(num)
print(user_list)

position_list = []
for i in range(num):
    position_list.append(i)


find_list = input(f'Укажите интересующие позиции элементов через пробел {position_list}:  ').split()
for i in range(len(find_list)):
    find_list[i] = int(find_list[i])

res = 1
for i in range(len(user_list)):
    for j in range(len(find_list)):
        if i == find_list[j]:
            res *= user_list[i]

print(f'Произведение элементов на указанных позициях равно: {res}')
