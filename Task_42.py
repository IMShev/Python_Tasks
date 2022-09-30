# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


number = int(input("Введите натуральное число N: "))


def simple_mult(num):
    rezult = []

    for i in range(2, num):
        while num % i == 0:
            num /= i
            rezult.append(i)
    return rezult


if simple_mult(number) == []:
    print(f'Это простое число -  [1, {number}] !')
else:
    print(f'Список простых множителей числа {number} : {simple_mult(number)}')
