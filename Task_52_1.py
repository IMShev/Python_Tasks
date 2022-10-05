# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Тот, кто берет последнюю конфету - проиграл.

# игра с компьютером

import random

player = input('Игрок, как Вас зовут: ')
print(f'{player}, с Вами играет компьютер.')
n = int(input('Введите общее количество конфет: '))
k = int(input('Сколько конфет можно взять за один ход: '))
ocher = random.randint(1, 2)

if ocher == 1:
    print('Начинает компьютер')
else:
    print('Начинаете Вы')

while True:
    if ocher == 2:
        skolko2 = int(input('Сколько Вы берете? '))
        if skolko2 == 0 or skolko2 > k:
            print(f'Неправильно! Возьмите конфет не более {k} и не менее 1 ! ')
            skolko2 = int(input('Сколько Вы берете? '))
        n = n - skolko2
    else:
        if n >= k:
            skolko1 = random.randint(1, k)
            print(f'Комьютер взял {skolko1}')
        else:
            skolko1 = random.randint(1, n)
            print(f'Комьютер взял {skolko1}')
        n = n - skolko1
    if n == 0:
        print('Игра закончена!')
        if ocher == 2:
            print('Вы проиграли.')
        else:
            print('Поздравляем! Вы выиграли!')
        break
    else:
        print(f'осталось конфет - {n}')
        if ocher == 1:
            ocher = 2
        else:
            ocher = 1
