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