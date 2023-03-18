'''Дан список чисел. Определите, сколько в нем
встречается различных чисел.
Input: [1, 1, 2, 0, -1, 3, 4, 4]
Output: 6'''

import random
# numbers = [1, 2, 3, 1, 1, 5, 10, 20, 20, 30]
numbers = [random.randint(0, 100) for _ in range(10)]

result = []
for num in numbers:
    if num not in result:
        result.append(num)  #append добавляет элемент в конец списка(массива)
print(result)
print(len(result))

numbers = [
    1, 2, 3, 1, 1, 5, 10, 20, 20, 30
]  #удаление повторяющихся элементов с сохранением начального массива в копии
for num in numbers.copy():
    while numbers.count(num) != 1:
        numbers.remove(num)
print(numbers)

print(len(set(    numbers)))  #set функция оставляет только уникальные элементы в множестве
