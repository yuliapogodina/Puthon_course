'''Напишите программу для печати всех уникальных
значений в словаре.
Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
{"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
":" S007 "}]
Output: {'S005', 'S002', 'S007', 'S001', 'S009'}'''

list_1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
{"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII":" S007 "}]

# Вариант 1 - original
unique_kyes = set()
for value in list_1:
    for key in value:
        unique_kyes.add(value[key])
print(unique_kyes)

# Вариант 2
unique_kyes = set()
for value in list_1:
    unique_kyes.update(value.values())
print(unique_kyes)


list_dicts = [{'Alex': 21, 'Dima': 25, 'Sveta': 27}, {'Alex': 'Cv', 'Dima': 'NLP', 'Sveta': "ML"}]
print(list_dicts[1]['Sveta'])
print(list_dicts[0]['Sveta'])
