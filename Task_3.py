#  Напишите программу, которая принимает на вход координаты точки (X и Y),
#  причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
#  в которой находится эта точка (или на какой оси она находится).

x = int(input('Введите значение координаты X: '))
y = int(input('Введите значение координаты Y: '))

if (x > 0 and y > 0):
    print('Точка находится в 1 четверти плоскости')
elif (x < 0 and y > 0):
    print('Точка находится в 2 четверти плоскости')
elif (x < 0 and y < 0):
    print('Точка находится в 3 четверти плоскости')
elif (x > 0 and y < 0):
    print('Точка находится в 4 четверти плоскости')
elif (x == 0 and y == 0):
    print('Точка находится на пересечении осей координат')
elif (x == 0 and y != 0):
    print('Точка находится на оси Х')
elif (x != 0 and y == 0):
    print('Точка находится на оси Y')
