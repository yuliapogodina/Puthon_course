'''Дана последовательность из N целых чисел и число
K. Необходимо сдвинуть всю последовательность
(сдвиг - циклический) на K элементов вправо, K –
положительное число.
Input: [1, 2, 3, 4, 5] k = 3
Output: [4, 5, 1, 2, 3]'''

numbers = [1, 2, 3, 4, 5]
k = int(input('сдвиг: '))
k = k % len(numbers)
'''Если кол-во сдвигов больше длины массива, то зачем
делать несколько кгругов, сдвиг только на остаток, чтобы была 1 итерация'''

# Вариант [1] - Modified
list_result = []
len_list = len(numbers)
for i in range(len_list - k, len_list):
    list_result.append(numbers[i])
for i in range(len_list - k):
    list_result.append(numbers[i])
print(list_result)

# Вариант 2
list_result = []
for i in range(len(numbers)):
    list_result.append(numbers[-k + i])
print(list_result)

for _ in range(k):
    numbers.insert(0, numbers.pop())
# pop забирает удаляет последний элемент из массива,
# insert вставляет элемент на позицию указанную в  1 параметре функции
print(numbers)


print(numbers[-k:]+numbers[:-k])