from data_create import name_data, surname_data, phone_data, address_data


def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(
        input(f"В каком формате Вы хотите записать данные?\n\n"
              f"1 Вариант:\n\n"
              f"{name}\n"
              f"{surname}\n"
              f"{phone}\n"
              f"{address}\n\n"
              f"2 Вариант:\n\n"
              f"{surname};{name};{phone};{address}\n\n"
              f"Выберите номер варианта: "))

    while var != 1 and var != 2:
        print('Ты дурак?! Даю тебе последний шанс')
        var = int(input("Введите номер варианта: "))

    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name}\n{surname}\n{phone}\n{address}\n\n')
    else:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name};{surname};{phone};{address}\n\n')


def print_data():
    print('Вывожу данные для Вас из 1-го файла\n')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
        data_first = file.readlines()
        data_first_version_second = []
        # data_middle = ''
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                data_first_version_second.append(''.join(data_first[j:i + 1]))
                j = i + 1
        data_first = data_first_version_second

        for i in range(len(data_first)):
            print(f'Запись № {i+1}\n{data_first[i]}')
        # print(''.join(data_first))
        # print(*data_first, sep='')

    print('вывожу даннык для Вас из 2-го файла\n')
    with open('data_second_variant.csv', 'r', encoding='utf-8') as file:
        data_second = list(file.readlines())
        print(f'Запись № 1\n{data_second[0]}')
        for i in range(1, len(data_second)):
            print(f'Запись № {i+1}\n{data_second[i]}')
        # print(*data_second)

    return data_first, data_second


def put_data():
    print('Из какого файла Вы хотите изменить данные?')
    data_first, data_second = print_data()
    number_file = int(input('Введите номер файла: '))

    while number_file != 1 and number_file != 2:
        print('Неверный выбор! Даю тебе последний шанс')
        number_file = int(input('Введите номер файла'))

    find_mark = str(input('Поиск записи по номеру? y/n: '))

    if find_mark == 'y': #замена при поиске по номеру записи

        if number_file == 1:
            print('Какую именно запись по счету Вы хотите изменить?')
            number_journal = int(input('Введите номер записи: '))

            while number_journal < 1 or number_journal > (len(data_first) + 1):
                print('Неверный ввод! Даю тебе последний шанс')
                number_journal = int(input('Введите номер записи: '))
            element = list(data_first[number_journal - 1].split('\n'))
            parametr_rec = list(str(input(f"Какой параметр записи Вы хотите поменять?\n\n"
              f"1 {element[0]}\n"
              f"2 {element[1]}\n"
              f"3 {element[2]}\n"
              f"4 {element[3]}\n"
              f"Ведите номер параметра и новое значение через / :\n\n")).split('/'))
            
            while parametr_rec[0] not in '1234':
                print('Неверный ввод! Даю тебе последний шанс')
                parametr_rec = list(str(input('Ведите номер параметра и новое значение через / : ')).split('/'))

            data_element = list(data_first[number_journal-1].split('\n'))
            data_element[(int(parametr_rec[0]))-1] = parametr_rec[1]
            data_first[number_journal-1] = str(data_element[0]+'\n' + data_element[1]+'\n' + data_element[2] +'\n'+ data_element[3] + '\n\n')

            with open('data_first_variant.csv', 'w', encoding='utf-8') as file:
                for element in data_first:
                    file.write(element)
            
        else:
            print('Какую именно запись по счету Вы хотите изменить?')
            number_journal = int(input('Введите номер записи: '))

            while number_journal < 1 and number_journal > (len(data_second) + 1):
                print('Неверный выбор! Даю тебе последний шанс')
                number_journal = int(input('Введите номер записи: '))

            element = list(data_second[number_journal - 1].split(';'))
            parametr_rec = list(str(input(f"Какой параметр записи Вы хотите поменять?\n\n"
              f"1 {element[0]}\n"
              f"2 {element[1]}\n"
              f"3 {element[2]}\n"
              f"4 {element[3]}\n"
              f"Ведите номер параметра и новое значение через / :\n\n")).split('/'))
            
            while parametr_rec[0] not in '1234':
                print('Неверный ввод! Даю тебе последний шанс')
                parametr_rec = list(str(input('Ведите номер параметра и новое значение через / : ')).split('/'))

            data_element = list(data_second[number_journal-1].split(';'))
            data_element[(int(parametr_rec[0]))-1] = parametr_rec[1]
            data_second[number_journal-1] = str(data_element[0]+';'+data_element[1]+';'+data_element[2]+';'+data_element[3]+'\n')

            with open('data_second_variant.csv', 'w', encoding='utf-8') as file:
                for element in data_second:
                    file.write(element)
            

    else:  #замена при поиске по фамилии и имени
        print('Данные для поиска записи: \n')
        find_name = name_data()
        find_surname = surname_data()

        if number_file == 1:
            for i in range(len(data_first)):
                if (find_name + '\n' + find_surname) in data_first[i]:
                    count = i
            
            element = list(data_first[count].split('\n'))
            parametr_rec = list(str(input(f"Какой параметр записи Вы хотите поменять?\n\n"
              f"1 {element[0]}\n"
              f"2 {element[1]}\n"
              f"3 {element[2]}\n"
              f"4 {element[3]}\n"
              f"Ведите номер параметра и новое значение через пробел:\n\n")).split('/'))
            
            while parametr_rec[0] not in '1234':
                print('Неверный ввод! Даю тебе последний шанс')
                parametr_rec = list(str(input('Ведите номер параметра и новое значение через /: ')).split('/'))

            element[(int(parametr_rec[0]))-1] = parametr_rec[1]
            data_first[count] = str(element[0] +'\n' + element[1]+ '\n' + element[2] + '\n' + element[3] + '\n\n')
                    
            with open('data_first_variant.csv', 'w', encoding='utf-8') as file:
                for el in data_first:
                    file.write(el)

        else:
            for i in range(len(data_second)):
                if (find_name + ';' + find_surname) in data_second[i]:
                    count = i
            
            element = list(data_second[count].split(';'))
            parametr_rec = list(str(input(f"Какой параметр записи Вы хотите поменять?\n\n"
              f"1 {element[0]}\n"
              f"2 {element[1]}\n"
              f"3 {element[2]}\n"
              f"4 {element[3]}\n"
              f"Ведите номер параметра и новое значение через пробел:\n\n")).split('/'))
            
            while parametr_rec[0] not in '1234':
                print('Неверный ввод! Даю тебе последний шанс')
                parametr_rec = list(str(input('Ведите номер параметра и новое значение через /: ')).split('/'))

            element[(int(parametr_rec[0]))-1] = parametr_rec[1]
            data_second[count] = str(element[0] + ';' + element[1] + ';' + element[2] + ';' + element[3])

            with open('data_second_variant.csv', 'w', encoding='utf-8') as file:
                for el in data_second:
                    file.write(el)
                                


def delete_data():
    print('Из какого файла Вы хотите удалить данные?')
    data_first, data_second = print_data()
    number_file = int(input('Введите номер файла: '))

    while number_file != 1 and number_file != 2:
        print('Неверный выбор! Даю тебе последний шанс')
        number_file = int(input('Введите номер файла'))

    find_mark = str(input('Поиск записи по номеру? y/n: '))

    if find_mark == 'y':

        if number_file == 1:
            print('Какую именно запись по счету Вы хотите удалить?')
            number_journal = int(input('Введите номер записи: '))

            while number_journal < 1 or number_journal > (len(data_first) + 1):
                print('Неверный ввод! Даю тебе последний шанс')
                number_journal = int(input('Введите номер записи: '))

            del data_first[number_journal - 1]
            with open('data_first_variant.csv', 'w', encoding='utf-8') as file:
                for element in data_first:
                    file.write(element)

        else:
            print('Какую именно запись по счету Вы хотите удалить?')
            number_journal = int(input('Введите номер записи: '))

            while number_journal < 1 and number_journal > (len(data_second) + 1):
                print('Неверный выбор! Даю тебе последний шанс')
                number_journal = int(input('Введите номер записи: '))

            del data_second[number_journal - 1]
            with open('data_second_variant.csv', 'w', encoding='utf-8') as file:
                for element in data_second:
                    file.write(element)

    else:
        find_name = name_data() 
        find_surname = surname_data()
        
        if number_file == 1:
            for i in range(len(data_first)):
                if (find_name + '\n' + find_surname) in data_first[i]:
                    count = i

            del data_first[count]
            with open('data_first_variant.csv', 'w', encoding='utf-8') as file:
                for element in data_first:
                    file.write(element)

        else:
            for i in range(len(data_second)):
                if (find_name + ';' + find_surname) in data_second[i]:
                    count = i

            del data_second[count]
            with open('data_second_variant.csv', 'w', encoding='utf-8') as file:
                for element in data_second:
                    file.write(element)
