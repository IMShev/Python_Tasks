# Вычислить число c заданной точностью d
# Пример:  при d = 0.001, π = 3.141.    10^{-1} ≤ d ≤10^{-10}

import math
from random import randint


a = randint(0, 100)
b = randint(0, 100)

d = float(input('Введите точность числа от 0,1 до 0,00000000001: '))
num_precision = 0
while d < 1:
    d *= 10
    num_precision += 1

print('Pi = ', round(math.pi, num_precision))
print('e = ', round(math.e, num_precision))
print('number = ', round(a/b, num_precision))
