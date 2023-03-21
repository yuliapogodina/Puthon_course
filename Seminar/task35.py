"""Даны два целых числа A и В. 
Выведите все числа от A до B включительно, в порядке возрастания, 
если A < B, или в порядке убывания, если A > B """

def print_number(a, b):
    if a == b:
        return a
    if a > b:
        return f"{a}, {print_number(a - 1, b)}"
    if a < b:
        return f"{a}, {print_number(a + 1, b)}"


print(print_number(5, 1))
