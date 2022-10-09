# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
#  [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


import random

# оптимизация кода с использованием list comprehension и enumerate

a = [random.randint(0, 10) for i in range(random.randint(3, 10))]
print(a)
b = sum([x for i, x in enumerate(a) if i % 2])
print(f'Сумма элементов списка, стоящих на нечётных позициях равна {b}')


# прежний вариант кода

# a = []
# for i in range(random.randint(3, 10)):
#     a.append(random.randint(0, 10))
# print(a)

# summ = 0
# for i in range(1, len(a), 2):
#     summ += a[i]
# print(f'Сумма элементов списка, стоящих на нечётных позициях равна {summ}')
