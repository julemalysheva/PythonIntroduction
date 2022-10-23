# from main import len_field,all_fields

# - карточки сотрудника по строкам
# печатает список сотров с полными данными - всю базу последовательно по каждому сотру
from easygui import msgbox


def print_all_data(staff):
    str_res = ''
    for k, v in staff.items():
        str_res += f'\nФИО сотрудника: {k}'
        #  print(f'\nФИО сотрудника: {k}')
        for m, n in v.items():
            str_res+=f'\n\t{m}: {n}'
            # print(f'\t{m}: {n}')
    return str_res

# печатает все данные по найденному сотруднику по строкам - не таблицей

def print_all_for_worker(dict, key):
    str_res = ''
    if key in dict:
        str_res+=f'\nФИО сотрудника: {key}'
        # print(f'\nФИО сотрудника: {key}')
        for m, n in dict[key].items():
            str_res+=f'\n\t{m}: {n}'
            # print(f'\t{m}: {n}')
    else:
        str_res+='Такой сотрудник не найден'
        # print('Такой сотрудник не найден')
    return str_res

# можно запрашивать через графич.интерфейс или хотя бы через запятую список полей для вывода
# и на основе этого списка формировать таблицу. Длину полей заголовков и значений задать словарем или иной структурой
# добавила выбор сотрудника, по умолчанию - пусто "", тогда отбор по всей базе
# иначе по переданному сотруднику

def print_select_fields(staff, li_fields,len_field, sotr=''):
    # использую структуру len_field,где каждому ключу соответствует длина строки. некий словарь длины строки
    # сформировать вывод  - собираем заголовок таблицы
    # str_res=''
    str_res = '\nФИО:'.ljust(15)
    for el in li_fields:
        str_res += str(el).ljust(len_field[el])+'\t'
    # print(first_str)

    if sotr == '':
        for k, v in staff.items():
            str_item = str(k).ljust(15)
            for el in li_fields:
                str_item += str(v[el]).ljust(len_field[el])+'\t'
            str_res+= '\n' + str_item   
            # str_item+='\n'    
            # print(str_item)
    else:  # если передано значение выборки по сотруднику
        if sotr in staff:
            str_item = sotr.ljust(15)
            for el in li_fields:
                str_item += str(staff[sotr][el]).ljust(len_field[el])+'\t'
            str_res+= '\n' + str_item 
            # str_item+='\n'            
            # print(str_item)
        else: msgbox(f'Сотрудник {sotr} не найден')    

    # str_res = first_str + '\n' + str_item   
    return str_res    

# печатает просто список сотрудников
def print_list_worker(staff):
    res = 'Сотрудники:\n '
    for k in staff:
        res+=f'\n{k}'
    return res

# печатает все данные по найденному сотруднику по строкам - не таблицей

def print_all_for_worker(dict, key):
    if key in dict:
        res = f'\nФИО сотрудника: {key}'
        for m, n in dict[key].items():
            res+=f'\n\t{m}: {n}'
    else:
        msgbox('Такой сотрудник не найден')

    return res

# по отделу, по должности, по полу и .тд.,т.е. по конкретному значению вложенного ключа
# сейчас печатает только ФИО и ТН - можно добавить флаг
# 1 - печатать только ФИО по выбранному параметру
# 2- печатать все данные по тем сотр-м, кот.соответствуют условию отбора
# без передачи параметров сделать флаг в ф-ции по умолчанию - только ФИО ТН, например
def print_for_key_value(dict, key, item):
    # для целей выборки создаем список числовых полей
    fields_int = ["Возраст", "Оклад", "Стаж"]
    # для даты
    date_fields = ["Дата рождения", "Дата приема"]

    res = f'\nДанные по запросу - {key} = {item} ":"'
    # print('\nДанные по запросу - ', key, "=", item, ":")
    count_find = 0
    for k in dict:
        
        # если поле для поиска числовое
        if key in fields_int and isinstance(item, list):
            # если значение этого ключа попадает в диапазон
            if item[0] <= int(dict[k][key]) <= item[1]:
                res+=f'\nФИО: {k} \tТН: {dict[k]["ТН"]} \t{str(key)}: {dict[k][key]}'
                # print(
                #     f'ФИО: {k} \tТН: {dict[k]["ТН"]} \t{str(key)}: {dict[k][key]}')
                count_find += 1
        
        # если работаем с датой
        elif key in date_fields:
            li_date = dict[k][key].split(".") #0-день,1-месяц,2-год
            li_date = list(map(int,li_date))
            if item[0] != None and item[1] != None: #ищем месяц и год
                if li_date[1] == item[0] and li_date[2] == item[1]:
                    res+=f'\nФИО: {k} \tТН: {dict[k]["ТН"]} \t{str(key)}: {dict[k][key]}'
                    # print(
                    #     f'ФИО: {k} \tТН: {dict[k]["ТН"]} \t{str(key)}: {dict[k][key]}')
                    count_find += 1
            elif item[0] != None and item[1] == None: #ищем месяц 
                if li_date[1] == item[0]:
                    res+=f'\nФИО: {k} \tТН: {dict[k]["ТН"]} \t{str(key)}: {dict[k][key]}'
                    # print(
                    #     f'ФИО: {k} \tТН: {dict[k]["ТН"]} \t{str(key)}: {dict[k][key]}')
                    count_find += 1
            elif item[0] == None and item[1] != None: #ищем год 
                if li_date[2] == item[1]:
                    res+=f'\nФИО: {k} \tТН: {dict[k]["ТН"]} \t{str(key)}: {dict[k][key]}'
                    # print(
                    #     f'ФИО: {k} \tТН: {dict[k]["ТН"]} \t{str(key)}: {dict[k][key]}')
                    count_find += 1

        # в остальных случаях
        elif key in dict[k]:  # если искомый ключ есть во вложенном словаре сотрудника
            if dict[k][key] == item:  # если значение этого ключа совпадает с искомым
                res+=f'\nФИО: {k} \tТН: {dict[k]["ТН"]} \t{str(key)}: {dict[k][key]}'
                # print(
                #     f'ФИО: {k} \tТН: {dict[k]["ТН"]} \t{str(key)}: {dict[k][key]}')
                count_find += 1
                
    if count_find == 0:
        # фиксируем лог и
        res = 'По заданным параметрам ничего не найдено'
        # print('По заданным параметрам ничего не найдено')

    return res    
