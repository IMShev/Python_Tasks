# Напишите программу для проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

X = input('Введите значение X: ')
Y = input('Введите значение Y: ')
Z = input('Введите значение Z: ')

A = [X, Y, Z]

firstPart = not (A[0] or A[1] or A[2])
secondPart = not A[0] and not A[1] and not A[2]

result = firstPart == secondPart

if result == True:
    print('Утверждение истинно')
else:
    print('Утверждение ложно')
