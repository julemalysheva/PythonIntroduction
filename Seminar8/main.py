# Сделать также загрузку и выгрузку вспомог.справочников
# проверить и по логике везде добавить лог
staff = {}
from menu import *
from bd_json import *
import logger as log
from request import *
from add import add_worker, add_field
from change import *
from del_staff import *


# запускаем вход в программу - проверяем пользовательские права
user = registration()

# вспомогательные справочники и переменные
try:
    all_fields = load('all_fields.json')
except:   
    log.error_logger('Ошибка загрузки all_fields.json') 
    all_fields = ["ТН", "Дата рождения", "Адрес", "Пол", "Возраст", "Телефон",
                "Должность", "Оклад", "Отдел", "Стаж", "email", "Дата приема"]

    # справочник, где каждому ключу соответствует длина строки. словарь длины строки
    # сделать его также глобальным,т.к. при добавлении поля нужно сюда также добавить значение
try:
    len_field = load('len_field.json')    
except:
    log.error_logger('Ошибка загрузки len_field.json') 
    len_field = {
        "ТН": 3,"Дата рождения": 10,"Адрес": 20,"Пол": 3,"Возраст": 7,"Телефон": 12,
        "Должность": 20,"Оклад": 6,"Отдел": 15,"Стаж": 4,"email": 20,"Дата приема": 10
    }

# подумать, если нужно еще справочники даты и чисел, то можно их загружать из одного файла, просто списком
try:
    staff = load('staff.json')
    msgbox("База сотрудников загружена")
except:
    log.error_logger('Ошибка загрузки базы')
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
# пока печатаем для проверки загрузки 
# print(staff)

# непрерывный цикл меню до выхода юзера
while True:
    option = option_start()
    if option == 0: #'Работа с базой'
        #от выбранного пункта и подпункта строить вызов view_data() через переменную текст?
        point = choice_menu(user) 
        #идет проверка и вызов нужных ф-ций из нужных модулей 
        # полученный рез-т показваем через view_data()
        if point == 'добавить сотрудника':
            sotr = enter_item('Введите Фамилию и инициалы нового сотрудника\n')
            fields_sotr = input_fields_to_list(all_fields)
            staff = add_worker(staff, sotr, fields_sotr,all_fields)
            # выводим новую карточку сотрудника
            text = print_all_for_worker(staff,sotr)
            view_data(text,f'Выполнено: *{point}*')

        elif point == 'новое поле для карточек':
            field = enter_item('Введите название нового поля\n')
            staff = add_field(staff, field)
            # добавляю элемент во вспомог.справочники для корректного отображения на печати и пр.
            len_field[field] = integer_item("Введите длину созданного поля для печати: ",1,25)
            all_fields.append(field)
            # вывожу подтверждение выполнения задачи
            text = print_select_fields(staff, [field],len_field)  
            view_data(text,f'Выполнено: *{point}*')

        elif point == 'удалить сотрудника': 
            sotr = choice_field('Выберите сотрудника для удаления из базы', point, tuple(staff.keys()))
            if sotr != None:
                if check_yes():
                    staff = del_sotr(staff,sotr)
                    show_event_validation(point,print_list_worker(staff)) 
            else: show_event_validation(point,'Сотрудник не выбран')   

        elif point == 'удалить поле в карточках':
            key_field = choice_field('Выберите поле для удаления:',point,(all_fields))
            if key_field != None:
                if check_yes():
                    staff = del_key(staff,key_field)
                    all_fields.remove(key_field)
                    del len_field[key_field]
                    show_event_validation(point,f'Выполнено\n{all_fields}') 
            else: show_event_validation(point,'Значение не выбрано')   

        elif point == "менять поля у всех":
            field_for_change = choice_field('Выберите поле для изменения:',point,(all_fields))
            if field_for_change!=None:
                staff = change_item_field(staff, field_for_change)
                show_event_validation(point,f'Выполнено\n{print_select_fields(staff, [field_for_change], len_field)}') 
            else: show_event_validation(point,'Значение не выбрано')   

        elif point == "изменить поле у сотрудника":
            sotr = choice_field('Выберите сотрудника для редактирования поля', point, tuple(staff.keys()))
            if sotr != None:
                field_for_change = choice_field('Выберите поле для изменения:',point,(all_fields))
                if field_for_change!=None:
                    staff = change_item_field(staff, field_for_change,sotr)
                    show_event_validation(point,f'Выполнено\n{print_select_fields(staff, [field_for_change], len_field,sotr)}') 
                else: show_event_validation(point,'Значение не выбрано')   
            else: show_event_validation(point,'Сотрудник не выбран')   

        elif point == "пакетная индексация окладов":
            percent =  integer_item(f'Текущие оклады: \n{print_select_fields(staff, ["Оклад"],len_field)}\nПроцент повышения оклада:',1,100)   
            if percent !=None:
                staff = indexation(staff,percent)
                show_event_validation(point,f'Выполнено\n{print_select_fields(staff, ["Оклад"], len_field)}') 
            else: show_event_validation(point,'Значение не выбрано')   

        elif point == 'просто список сотрудников':
            list_worker = print_list_worker(staff)
            view_data(list_worker, point)

        elif point == 'выбрать поля для печати по всей базе':
            # выбираем поля для отображения из всего списка полей
            li_fields = mult_items(all_fields)
            if li_fields != None:
                text = print_select_fields(staff, li_fields, len_field) 
                view_data(text, point)
            else: show_event_validation(point,'Поля не выбраны')  

        elif point == 'выбрать поля и сотрудника для печати':  
            sotr = choice_field('Выберите сотрудника: ', point, tuple(staff.keys()))
            if sotr != None:
                li_fields = mult_items(all_fields)
                if li_fields != None:
                    text = print_select_fields(staff, li_fields, len_field,sotr) 
                    view_data(text, point)
                else: show_event_validation(point,'Поля не выбраны')  
            else: show_event_validation(point,'Сотрудник не выбран')   
 
        elif point == 'полные карточки всех сотрудников':
            text = print_all_data(staff)
            view_data(text, point)

        elif point == 'карточка выбранного сотрудника':
            sotr = choice_field('Выберите сотрудника: ', point, tuple(staff.keys()))
            if sotr != None:
                text = print_all_for_worker(staff,sotr)
                view_data(text, point)
            else: show_event_validation(point,'Сотрудник не выбран')   

        # в этом случае поля наезжаеют др.на друга - в консоли лучше печатал
        elif point == 'все данные таблицей':
            text = print_select_fields(staff, all_fields, len_field)
            view_data(text, point)

        elif point == 'по значениям полей':
            # выбираем поле
            field = choice_field(f'Выберите одно поле:', point, all_fields)
            if field!=None:
                # if field in all_fields:
                item = enter_value_for_key(field) 
                # else: show_event_validation(point,'Поле не найдено')   
            else: show_event_validation(point,'Значение не выбрано')   
            text = print_for_key_value(staff, field, item)
            view_data(text, point)

    elif option == 1: #'Смотреть лог'
        view_log('log_staff.txt')
    elif option == 2: #'Сохранить'
        try:
            save(staff, 'staff.json') 
            save(all_fields,'all_fields.json')
            save(len_field,'len_field.json')
            show_event_validation('Сохранение','Сохранение в файлы прошло успешно')
        except:
            show_event_validation('Сохранение','Ошибка сохранения базы')    
    else: #'Выход'
        if check_yes():
            try:
                save(staff, 'staff.json') 
                save(all_fields,'all_fields.json')
                save(len_field,'len_field.json')
                show_event_validation('Сохранение','Сохранение в файлы прошло успешно')
            except:
                show_event_validation('Сохранение','Ошибка сохранения базы')    
            break
        



