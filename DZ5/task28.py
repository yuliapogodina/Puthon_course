'''
Напишите рекурсивную функцию sum(a, b),
возвращающую сумму двух целых неотрицательных
чисел. Из всех арифметических операций
допускаются только +1 и -1. Также нельзя использовать циклы.
*Пример:*
2 2
4
'''


def sum_of_numbers(a, b):
    if a == 0:
        return b
    else:
        sumn = sum_of_numbers(a-1, b+1)
    return sumn


numa, numb = map(int, input('Введите 2 числа через пробел: ').split())
print(sum_of_numbers(numa, numb))
