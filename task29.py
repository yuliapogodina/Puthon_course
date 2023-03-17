numbers = [1, 5, 2, 3, 6, 9, 0, 5, 4, 7, 0, 6, 5, 8, 0, 5, 8, 7, 4, 2, 3, 6]
print(numbers)
max = float('-inf')
i = 0
while numbers[i] != 0:
    if numbers[i] > max:
        max = numbers[i]
    i += 1
print(max)
