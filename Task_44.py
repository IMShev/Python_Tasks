# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:  k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint


k = int(input('Введите степень многочлена: '))
deg = [i for i in range(k, -1, -1)]
ind = [randint(0, 100) for i in range(0, k+1)]

polyn = list()
for i in range(len(ind)):
    if ind[i] == 0 and deg[i] != 0:    # проверка на нулевой коэффициент
        i += 1
    elif ind[i] == 0 and deg[i] == 0:  #  проверка на последний нулевой элемент
        polyn.append(' = 0')
    elif deg[i] == 1:
        polyn.append(f'{ind[i]}*x + ')
    elif deg[i] == 0:
        polyn.append(f'{ind[i]} = 0')
    else:
        polyn.append(f'{ind[i]}*x^{deg[i]} + ')

str_polyn = ''.join(polyn)
print(str_polyn)


f = open('file.txt', 'a')
f.write(str_polyn+'\n')
f.close()
