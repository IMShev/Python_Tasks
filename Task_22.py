# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

number = int(input("Введите число: "))


def factorial(n: int):
    fact = 1
    a = []
    for i in range(1, n+1):
        fact = fact*i
        i = fact
        a.append(i)
    return a


print(factorial(number))
