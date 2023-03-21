"""Последовательностью Фибоначчи называется последовательность 
чисел a0, a1, ..., an, ..., где 
a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
0 1 1 2 3 5 8 11 19 30 
Требуется найти N-е число Фибоначчи"""


# def fib_rec(n):
#     if n <= 1:
#         return 1
#     else:
#         return fib_rec(n - 1) + fib_rec(n - 2)

# print(fib_rec(0))


cahce = {0: 0}
# My - Memo
def fib_rec_cache(n):
    if n not in cahce:
        cahce[n] = n if n <= 1 else fib_rec_cache(n - 1) + fib_rec_cache(n - 2)
    print(cahce)
    return cahce[n]

print(fib_rec_cache(10))
