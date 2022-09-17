#Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между 
# максимальным и минимальным значением дробной части элементов.
#       Пример:  -   [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

list1 = [round(random.uniform(0, 20),2) for i in range(random.randint(2, 10))]
print(list1)

list2=[int(round((list1[i]-int(list1[i]))*100,2)) for i in range(len(list1))]

print(f'Разница между максимальным ({max(list2)}) и минимальным ({min(list2)}) значением дробных частей равна {max(list2)-min(list2)}')

