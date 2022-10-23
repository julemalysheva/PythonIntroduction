# тоже пока прописываю все в одном, потом наладить связи и импорт

# прописываю изменения данных - перенести в отдельный модуль и настроить связи

# изменить какое-то поле пакетно или по сотруднику, по умолчанию пакетно, при выборе сотрудника передается аргумент сотр
from easygui import *
from menu import enter_item

def change_item_field(staff, field, sotr=''):
    if sotr == '':
        for k, v in staff.items():
            if field in v:
                v[field] = enter_item(f'{k} - текущее значение {v[field]} \nВведите новое значение поля {field}: ')
            else:
                # фикс лог
                msgbox(f'Поле {field} не найдено')    
    else:
        if sotr in staff:
            if field in staff[sotr]:
                staff[sotr][field] = enter_item(f'{sotr} - текущее значение {staff[sotr][field]} \nВведите новое значение поля {field}: ')   
            else:
                # фикс лог
                msgbox(f'Поле {field} не найдено')          
        else:
             # фикс лог
            msgbox(f'Сотрудник {sotr} не найден')   
    return staff        
                 


# field_for_change = input('Поле для редактирования: ')  
# if field_for_change in all_fields:
#     flag = input('\nМеняем у всех или выбрать сотрудника?\n1-у всех\n2-у сотрудника\nВведите свой выбор:')
#     if flag == '1':
#         change_item_field(staff, field_for_change)  
#         print_select_fields(staff,[field_for_change])
#     elif flag == '2':
#         sotr = input('Выберите/введите сотрудника, чью запись нужно изменить: ')  
#         change_item_field(staff, field_for_change,sotr)   
#         print_select_fields(staff,[field_for_change]) #или показывать карточку сотрудника с этим полем
# else:  
#         #    фикс лог
#     print(f'Поле {field_for_change} не найдено')    

#пакетно повысить оклад на определенный процент
def indexation(staff, percent):
    for k, v in staff.items():
            if "Оклад" in v:
                v["Оклад"] = round(v["Оклад"]*percent/100+v["Оклад"])
    return staff            
                    
# percent = float(input('\nПроцент повышения оклада: '))
# indexation(staff, percent)
# print_select_fields(staff, ["Оклад"])

# можно для гл.админа доб.возм-ть изменения названия поля - автоматически поменять всем, старое значение присвоить новому
# и старое удалить