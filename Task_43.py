# Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.

list_inp = [100, 75, 100, 20, 75, 12, 75, 25, 35, 47, 53, 44, 53]
print(list_inp)

uniq = [i for i in list_inp if list_inp.count(i) == 1]
print(uniq)
