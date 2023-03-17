'''В настольной игре Скрабл (Scrabble) каждая буква
имеет определенную ценность. В случае с английским
алфавитом очки распределяются так:
AEIOULNSTR – 1 очко;
D, G – 2 очка; B, C, M, P – 3 очка;
F, H, V, W, Y – 4 очка; K – 5 очков;
J, X – 8 очков; Q, Z – 10 очков.
А русские буквы оцениваются так:
А, В, Е, И, Н, О, Р, С, Т – 1 очко;
Д, К, Л, М, П, У – 2 очка;
Б, Г, Ё, Ь, Я – 3 очка;
Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков;
Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков.
Напишите программу, которая вычисляет стоимость
введенного пользователем слова. Будем считать,
что на вход подается только одно слово,
которое содержит либо только английские,
либо только русские буквы.
*Пример:*
ноутбук
    12'''

alphabet_en = {
    'AEIOULNSTR': 1,
    'DG': 2,
    'BCMP': 3,
    'FHVWY': 4,
    'K': 5,
    'JX': 8,
    'QZ': 10
}
alphabet_ru = {
    'АВЕИНОРСТ': 1,
    'ДКЛМПУ': 2,
    'БГЁЬЯ': 3,
    'ЙЫ': 4,
    'ЖЗХЦЧ': 5,
    'ШЭЮ': 8,
    'ФЩЪ': 10
}

import re

text = str(input('Слово: ')).upper()
itog = 0
if re.search('[А-Я]', text):
    alphabet = alphabet_ru
else:
    alphabet = alphabet_en
for x in text:
    for k, v in alphabet.items():
        if x in k:
            itog = itog + v
print(itog)
