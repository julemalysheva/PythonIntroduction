# сделать импорт и связи со всеми модулями
from easygui import *

# удаление пока пропишу здесь, чтоб не делать импорт и не переносить переменные - потом все свести куда надо
def del_sotr(staff,key):
    if key in staff:
        del staff[key]
        msgbox(f"Запись сотрудника {key} удалена")
    else:
        msgbox("Элемент не найден")
    return staff    

# удалять поле пакетно по всему словарю можно только гл.админу
def del_key(staff, key_field):
    # при удалении поля удаляем его из вспомогательных справочников
    # global all_fields, len_field
    for k, v in staff.items():
        if key_field in v:
            del v[key_field]
        else: msgbox("Элемент не найден")   
    return staff        



# sotr_del = input('Выберите/введите сотрудника, чью запись нужно удалить: ')        
# del_sotr(staff,sotr_del)
# print_select_fields(staff,all_fields)

# del_field = input('Выберите/введите поле для удаления: ')
# del_key(staff, del_field)
# print_select_fields(staff,all_fields)
