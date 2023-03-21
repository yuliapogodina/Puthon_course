'''
Напишите программу, которая на вход принимает
два числа A и B, и возводит число А в целую
степень B с помощью рекурсии.
*Пример:*
A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8
'''


def degree_number(number, degree):
    if degree == 1:
        return number
    result = number * degree_number(number, degree - 1)
    return result


a, b = map(int, input('Введите число и степень числа, через пробел: ').split())

print(degree_number(a, b))
