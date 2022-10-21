# *Добавить сотрудника - может только админ и главный админ - при добавлении последовательно предлагаем заполнить
# все имеющиеся на тот момент поля из списка всех полей
# *Добавить поле - имеет право только Главный админ - при добавлении поля прописываем новое значение в списке всех полей,
# затем каждому сотруднику добавляем этот ключ с пустым значением и идем в цикле предлагаем для каждого его заполнить данными

# и соответственно, после работы при выходе из системы или если пользователь выберет пункт Меню - Сохранить,
# все изменения из нашего словаря staff должны попадать в json файл

# делаю импорт своего рабочего файла, в проекте изменить - все связи будут через main/menu
# from sem8_Inform_System import print_all_for_worker
# from sem8_Inform_System import staff
# from sem8_Inform_System import all_fields

# пришлось сюда все временно скопировать, так как при импорте почему то запускал ф-ции из того файла


staff = {
    "Иванов П.С.": {
        "ТН": "001",
        "Дата рождения": "17.10.1980",
        "Адрес": "ул. Ленина, 43",
        "Пол": "М",
        "Возраст": 42,
        "Телефон": "+876390444",
        "Должность": "Директор",
        "Оклад": 150000,
        "Отдел": "Администрация",
        "Стаж": 22,
        "email": "ips1980@gmail.com",
        "Дата приема": '14.02.2005'
    },
    "Сергеева З.Л.": {
        "ТН": "002",
        "Дата рождения": "27.11.1983",
        "Адрес": "ул. Попова, 15",
        "Пол": "Ж",
        "Возраст": 39,
        "Телефон": "+79121451402",
        "Должность": "Главный бухгалтер",
        "Оклад": 100000,
        "Отдел": "Бухгалтерия",
        "Стаж": 18,
        "email": "sergeeva@gmail.com",
        "Дата приема": '14.12.2005'
    },
    "Григорьева Е.С.": {
        "ТН": "003",
        "Дата рождения": "27.07.1982",
        "Адрес": "ул. Просторная, 15-75",
        "Пол": "Ж",
        "Возраст": 40,
        "Телефон": "+79435558888",
        "Должность": "Коммерческий директор",
        "Оклад": 110000,
        "Отдел": "Администрация",
        "Стаж": 20,
        "email": "es_grig@gmail.com",
        "Дата приема": '25.02.2015'
    },
    "Тимофеев А.П.": {
        "ТН": "004",
        "Дата рождения": "21.10.1980",
        "Адрес": "ул. Пушкинская, 22-48",
        "Пол": "М",
        "Возраст": 42,
        "Телефон": "+79254445566",
        "Должность": "Зав.производством",
        "Оклад": 120000,
        "Отдел": "Администрация",
        "Стаж": 22,
        "email": "timofeev@gmail.com",
        "Дата приема": '14.04.2007'
    }
}

all_fields = ["ТН", "Дата рождения", "Адрес", "Пол", "Возраст", "Телефон",
              "Должность", "Оклад", "Отдел", "Стаж", "email", "Дата приема"]

    # создать структуру,где каждому ключу соответствует длина строки. например словарь длины строки
    # сделать его также глобальным,т.к. при добавлении поля нужно сюда также добавить значение
len_field = {
    "ТН": 3,
    "Дата рождения": 10,
    "Адрес": 20,
    "Пол": 3,
    "Возраст": 7,
    "Телефон": 12,
    "Должность": 20,
    "Оклад": 6,
    "Отдел": 15,
    "Стаж": 4,
    "email": 20,
    "Дата приема": 10
}


def print_all_for_worker(dict, key):
    if key in dict:
        print(f'\nФИО сотрудника: {key}')
        for m, n in dict[key].items():
            print(f'\t{m}: {n}')
    else:
        print('Такой сотрудник не найден')

def print_select_fields(staff, li_fields, sotr=''):
    # сформировать вывод  - собираем заголовок таблицы
    first_str = '\nФИО:'.ljust(15)
    for el in li_fields:
        first_str += str(el).ljust(len_field[el])+'\t'
    print(first_str)

    if sotr == '':
        for k, v in staff.items():
            str_item = str(k).ljust(15)
            for el in li_fields:
                str_item += str(v[el]).ljust(len_field[el])+'\t'
            print(str_item)
    else:  # если передано значение выборки по сотруднику
        str_item = sotr.ljust(15)
        for el in li_fields:
            str_item += str(staff[sotr][el]).ljust(len_field[el])+'\t'
        print(str_item)


# добавляем сотрудника
def add_worker(staff, sotr):
    staff[sotr] = {}
    for el in all_fields:
        staff[sotr][el] = input(f'Заполните поле {el}: ') 
    #выводим подтверждение создания новой карточки 
    print('Создана новая запись по сотруднику: ')
    print_all_for_worker(staff,sotr)    

# добавляем ключ - новое поле карточки
def add_field(staff, field):
    global all_fields, len_field
    len_field[field] = int(input("Введите длину созданного поля для печати: "))
    all_fields.append(field)
    print('\nВводите значения нового поля для каждого сотрудника\nили пропускайте ввод, нажимая Enter\n')
    for k, v in staff.items():
        v[field] = input(f'Сотрудник {k} - введите значение поля {field}: ')  
    # по завершению логично выдать список сотрудников со значением нового поля
    # важно аргументы передавать именно списком
    print_select_fields(staff, [field])  

# ввод будет прописан в меню, а связаны эти данные в мейн
# сейчас для работы ф-ции делаю
# также в мейн нужно будет проверить роль и права, при наличии права - запустить ф-цию,
# если нет - сообщить, что нет прав

# new_sotr = input('\nВведите Фамилию и инициалы нового сотрудника: ')
# add_worker(staff, new_sotr)
# print_select_fields(staff,all_fields)

# new_field = input('\nВведите название нового поля данных для карточки сотрудника: ')
# add_field(staff,new_field)

# удаление пока пропишу здесь, чтоб не делать импорт и не переносить переменные - потом все свести куда надо
def del_sotr(staff,key):
    if key in staff:
        del staff[key]
        print(f"Запись сотрудника {key} удалена")
    else:
        print("Элемент не найден")

# удалять поле пакетно по всему словарю можно только гл.админу
def del_key(staff, key_field):
    # при удалении поля удаляем его из вспомогательных справочников
    global all_fields, len_field
    all_fields.remove(key_field)
    del len_field[key_field]
    for k, v in staff.items():
        if key_field in v:
            del v[key_field]



# sotr_del = input('Выберите/введите сотрудника, чью запись нужно удалить: ')        
# del_sotr(staff,sotr_del)
# print_select_fields(staff,all_fields)

# del_field = input('Выберите/введите поле для удаления: ')
# del_key(staff, del_field)
# print_select_fields(staff,all_fields)


# прописываю изменения данных - перенести в отдельный модуль и настроить связи

# изменить какое-то поле пакетно или по сотруднику, по умолчанию пакетно, при выборе сотрудника передается аргумент сотр
def change_item_field(staff, field, sotr=''):
    if sotr == '':
        for k, v in staff.items():
            if field in v:
                v[field] = input(f'{k} новое значение поля {field}: ')
            else:
                # фикс лог
                print(f'Поле {field} не найдено')    
    else:
        if sotr in staff:
            if field in staff[sotr]:
                staff[sotr][field] = input(f'{sotr} новое значение поля {field}: ')   
            else:
                # фикс лог
                print(f'Поле {field} не найдено')          
        else:
             # фикс лог
            print(f'Сотрудник {sotr} не найден')   
                 


field_for_change = input('Поле для редактирования: ')  
if field_for_change in all_fields:
    flag = input('\nМеняем у всех или выбрать сотрудника?\n1-у всех\n2-у сотрудника\nВведите свой выбор:')
    if flag == '1':
        change_item_field(staff, field_for_change)  
        print_select_fields(staff,[field_for_change])
    elif flag == '2':
        sotr = input('Выберите/введите сотрудника, чью запись нужно изменить: ')  
        change_item_field(staff, field_for_change,sotr)   
        print_select_fields(staff,[field_for_change]) #или показывать карточку сотрудника с этим полем
else:  
        #    фикс лог
    print(f'Поле {field_for_change} не найдено')    

#пакетно повысить оклад на определенный процент
def indexation(staff, percent):
    for k, v in staff.items():
            if "Оклад" in v:
                v["Оклад"] = round(v["Оклад"]*percent/100+v["Оклад"])
                    
percent = float(input('\nПроцент повышения оклада: '))
indexation(staff, percent)
print_select_fields(staff, ["Оклад"])