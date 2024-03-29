# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:  для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


N = int(input('Введите число: '))

def fib(n):
    if n == 0:
        return 0
    elif n == -2:
        return -1
    elif n in (-1, 1, 2):
        return 1
    elif n < -2:
        return fib(n+2) - fib(n+1)
    else:
        return fib(n-1)+fib(n-2)

a=[int(fib(n)) for n in range(-N, N+1)]
print(a)
