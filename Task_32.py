# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
#  [2, 3, 4, 5, 6] => [12, 15, 16];
#  [2, 3, 5, 6] => [12, 15]

import random

a = []
for i in range(random.randint(3, 15)):
    a.append(random.randint(0, 10))
print(a)
print(f'длинна списка равна {len(a)}')

b = []

i = 0
j = -1
if (len(a)%2 != 0):
    while  (a[i] != a[j]) or (i != len(a)//2): 
      x = a[i]*a[j]
      b.append(x)
      i += 1
      j -= 1
    else:
     x = a[i]**2
     b.append(x)
else:
    while (i != (len(a)/2)):
        x = a[i]*a[j]
        b.append(x)
        i += 1
        j -= 1



print(b)

