# здесь я прописываю ф-ции входа
# выбора меню - от роли строю пункты меню - ?может для каждой роли создать свой словарь или список пунктов меню?
# вызываться будут на стороне main, а вывод строится через производств.модули
# также д.б. переменные, содержащие список пользователей/пароли для сверки значений

from easygui import *
import logger as log
from datetime import datetime, date


# запускаем вход в программу - проверяем пользовательские права
# список кортежей логин/пароль - и по ним проверять полученный список,преобразовав в кортеж на вхождение
users = [('main','main'),('admin','admin'),('user','user')]
def registration():
    list1 = ["Имя пользователя","Пароль"]
    while True: 
        # имя пользователя и пароль, как список ['admin', '545454'] - переводим в кортеж
        user = tuple(multpasswordbox("Пожалуйста, введите свой логин и пароль",title = "Авторизоваться",fields = (list1)))
        if user in users:
            log.register_logger(f'{user[0]} - успешный вход в систему')
            msgbox(f'Привет {user[0]}, добро пожаловать в интерфейс базы сотрудников')
            break    
        else: 
            log.error_logger(f'{user} - неверный логин/пароль')
            msgbox('Неверные логин/пароль, попробуйте снова')
    return user[0]   

def option_start():
    start_menu = {0: 'Работа с базой',1: 'Смотреть лог',2: 'Сохранить',3: 'Выход'}
    option = indexbox(msg = "Продолжите выбор",title = "Стартовое меню", choices =('Работа с базой','Смотреть лог','Сохранить','Выход'))
    log.menu_logger(f'{start_menu[option]} - стартовое меню')
    return option

# подтверждение выбора - можно использовать во многих запросах, не только при выходе
def check_yes():
    yn = ynbox(msg = "Вы уверены?",title = "Подтвердите выбор",choices =('Да','Нет'),image = None, default_choice = 'Да', cancel_choice = 'Нет')
    # if yn:
    #     msgbox('Подтверждение принято')
    log.menu_logger(f'Подтверждение выбора {bool(yn)}')
    return yn

def view_log(file):
    try:
        with open(file, 'r', encoding="utf8") as f:
            log.res_logger('Файл лога к просмотру')
            msg = f'Содержимое файла {file} выглядит следующим образом:' 
            text = f.read()
            textbox(msg, 'Файл лога', text)
    except:
        log.error_logger('Файл лога не найден')
        msgbox('Файл лога не найден')

# варианты меню предлагаются в зависимости от роли юзера
# по идее можно сразу создать вложенный словарь и перебирать в цикле внутрь пока вложенный эл-т это словарь
# но пока так оставила
def choice_menu(user): #добавить запись в лог здесь
    #от выбранного пункта и подпункта строить вызов view_data() через переменную текст?
    # возвращать текст конкретного меню
    menu ={
        'main':('добавить','удалить','изменить','выборка'),
        'admin':('добавить сотрудника','удалить сотрудника','изменить','выборка'),
        'user':('изменить','выборка')
    }
    msg = 'Выберите из списка интересующий вас пункт'
    title = 'Вы можете выбрать один'
    choices = menu[user]
    answer = choicebox(msg,title,choices)
    if answer != None:
        log.menu_logger(f'Выбран пункт -{answer}')
        # print('Вы выбрали: '+ str(answer)) #выдает конкретное выбранное значение
        if answer in ('добавить','удалить','изменить','выборка'):
            submenu = {
                'добавить': ('добавить сотрудника', 'новое поле для карточек'),
                'удалить':('удалить сотрудника','удалить поле в карточках'),
                'изменить':("менять поля у всех","изменить поле у сотрудника","пакетная индексация окладов"),
                'выборка':('по сотрудникам и полям','по значениям полей')
                }
            msg = 'Выберите интересующий вас пункт'
            title = f'Раздел *{answer}*'
            choices = submenu[answer]
            answer = choicebox(msg,title,choices)
            if answer != None:
                log.menu_logger(f'Выбран пункт -{answer}')
                # print('Вы выбрали: '+ str(answer)) #выдает конкретное выбранное значение
                if answer == 'по сотрудникам и полям':
                    msg = 'Выберите интересующий вас пункт'
                    title = f'Раздел *{answer}*'
                    choices = (
                    'выбрать поля для печати по всей базе',
                    'выбрать поля и сотрудника для печати',
                    'просто список сотрудников',
                    'полные карточки всех сотрудников',
                    'карточка выбранного сотрудника',
                    'все данные таблицей')
                    answer = choicebox(msg,title,choices)
                    if answer != None:
                        log.menu_logger(f'Выбран пункт -{answer}')
                        # print('Вы выбрали: '+ str(answer)) #выдает конкретное выбранное значение
                    else:
                        log.menu_logger('Выбор отменен')
                        msgbox('Вы отменили выбор')   

            else:
                log.menu_logger('Выбор отменен')
                msgbox('Вы отменили выбор')   
    else: 
        log.menu_logger('Выбор отменен')
        msgbox('Вы отменили выбор')   

    return answer   #(возвращать можно кортеж - пункт меню,список выбранных значений)  

#или проверять это уже в main и отдельной ф-цией запрашивать значения для выборки и изменений
# которое потом передавать в нужную ф-цию из др. модулей 
def enter_item(txt):
    st = enterbox(txt)
    return st

def input_fields_to_list(list_fields):
    fields_sotr = multenterbox("Заполните карточку нового сотрудника",title = 'Персональные данные',fields = (list_fields))
    return fields_sotr
# здесь запрашиваем несколько значений пользовательского ввода
# н-р при создании новой карточки

# число в диапазоне
def integer_item(msg,lowerbound=0,upperbound=100):
    # msg = 'Введите число, диапазон от 0 до 100'
    title = 'Только числовой тип'
    # lowerbound = 0
    # upperbound = 100
    default = 0
    result = integerbox(msg,title,default,lowerbound,upperbound)
    return result

# для выбора полей для печати, например. когда несколько можно выбрать - возвращает список
def mult_items(all_fields):
    msg = 'Выберите от одного до всех значений'
    title = 'Множественный выбор'
    choices = (all_fields)
    answer = multchoicebox(msg,title,choices)
    # for item in answer1: #здесь можно выбрать много значений?
    #     print (item)     #и в цикле записывать в список - по которому потом печатать если выбраны
    return answer


# здесь показываем результаты запросов выборки через текст или код бокс
def view_data(text, title):
    log.res_logger(title)
    msg = f'По вашему запросу сформировано:' 
    textbox(msg, title, text)
    # выдача рез-та на экран или 

# здесь показываем месседж бокс с подтверждением действия и вызываем view_data при необходимости
# показать новый вид карточки и т.д.-какие-то действия, кроме выборки
def show_event_validation(task, description):  
    log.res_logger(f'Задача: *{task}*  - {description}')  #см.может убрать потом
    msgbox(f'Задача: *{task}*  - {description}')

def choice_field(msg,title,choices):
    res = choicebox(msg,title,(choices))
    return res

def enter_value_for_key(section):
    # для целей выборки создаем список числовых полей
    fields_int = ["Возраст", "Оклад", "Стаж"]
    # для даты
    date_fields = ["Дата рождения", "Дата приема"]

    # если поле числовое - предлагаем свои варианты
    if section in fields_int:
        var = choicebox('Выберите вариант запроса:','Выборка по значению поля',('выбор конкретного значения','выбор диапазона'))
        if var == 'выбор конкретного значения':
            el = integer_item('Введите интересующее вас значение: ',0,1000000)
        elif var == 'выбор диапазона':
            el = []
            start = integer_item('Введите значение для поиска ОТ: ',0,1000000)
            end = integer_item('Введите значение для поиска ДО: ',0,1000000)
            el.append(start)
            el.append(end)
        else:  
            msgbox('Выбор отменен')
        #     # фикс лог

    # добавим работу с датой - другие варианты запроса
    elif section in date_fields:
        el = (None, None)
        var = choicebox('Выберите вариант отбора значений','Условия выборки',('выбор месяца','выбор года','выбор месяца и года'))
        if var == 'выбор месяца':
            el = integer_item('Введите номер месяца: ',1,12)
            if  el != None:
                el = (el, None)
            else:
                # фикс лог
                msgbox('Выбор отменен')
        elif var == 'выбор года':
            el = integer_item('Введите значение года: ',1900,int(date.today().year))
            if el != None:
                el = (None, el)
            else:
                # фикс лог
                msgbox('Выбор отменен')
        elif var == 'выбор месяца и года':
            el1 = integer_item('Введите значение месяца: ',1,12)
            if el1 != None:
                el = (el1, None)
            else:
                # фикс лог
                msgbox('Выбор отменен')   

            el2 = integer_item('Введите значение года: ',1900,int(date.today().year))     
            if el2 != None:
                el = (el1, el2)
            else:
                # фикс лог
                msgbox('Выбор отменен')

        else:
            # фикс лог
            msgbox('Выбор отменен')

    elif section == "Пол":
        el = choicebox('Выберите вариант отбора значений','Условия выборки',('М','Ж'))

    # в иных случаях при наличии такого поля в базе
    else: 
        el = enter_item('Введите интересующее вас значение: ')

    return el    
