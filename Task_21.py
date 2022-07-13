# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
#  6782 -> 23
#  0,56 -> 11

number = input('Введите вещественное число: ')

def summ_digit(n):
    summ = 0
    for digit in n:
        if digit.isdigit():
            summ += int(digit)
    return summ
 
print(f'Сумма цифр числа {number} равна: ', summ_digit(number))

 

