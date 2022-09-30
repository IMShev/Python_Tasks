# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

with open('polynom_1.txt', 'r') as p1:  #вывод в консоль для наглядности
    print(p1.read())

with open('polynom_2.txt', 'r') as p2:  #вывод в консоль для наглядности
    print(p2.read())

with open('polynom_1.txt', 'r') as f1:
    pol_1 = str(f1.readline()).replace('*', '+').replace(' ', '').replace('=0', '').split('+')

with open('polynom_2.txt', 'r') as f2:
    pol_2 = str(f2.readline()).replace('*', '+').replace(' ', '').replace('=0', '').split('+')

sum_pol = [(int(pol_1[i])+int(pol_2[i])) for i in range(0, len(pol_1), 2)]

sum_pol_x = [pol_1[i] for i in range(1, len(pol_1), 2)]

with open('sum_polynom.txt', 'w') as f3:
    res = ''
    for i in range(0, len(sum_pol_x)):
        res += str(sum_pol[i]) + '*' + sum_pol_x[i] + ' + '
    result = res + str(sum_pol[-1]) + ' = 0'
    print(result, file=f3)

print(result)   #вывод в консоль для наглядности 


