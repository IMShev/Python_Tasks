# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

num = int(input("Введите число: "))

# Улучшенный код с помощью lambda и list comprehension

factorial_1 = lambda num: num * factorial_1(num-1) if (num>1) else 1
a = [factorial_1(i) for i in range(1, num +1)]
print(a)

#для примера - использование функции map()

a_1 = list(map(lambda x : x*2, a))
print(a_1)

# # прежнее решение 

# def factorial(n: int):
#     fact = 1
#     a = []
#     for i in range(1, n+1):
#         fact = fact*i
#         i = fact
#         a.append(i)
#     return a
# print(factorial(num))