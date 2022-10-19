from datetime import datetime as dt
from time import time

# нужно продумать и прописать лог в файл
# названия ф-ций не менять, они применются во view на стороне пользователя и в др.системах
# описать грамотно формат записи данных
# определиться с типом файла, по умолчанию сейчас txt

# вообще, надо подумать вместе, по сути все ф-ции типовые, отличается только текст записи -
# так может стоит передавать этот текст на стороне view в момент фиксации лога,
# прописать его в параменты ф-ции и записывать в строку файла
# например:
# def logger(data, title):
#     time = dt.now().strftime('%H:%M')
#     with open('log.txt', 'a') as file: #или log.csv файл?
#         file.write('{};{title};{}\n'
#                     .format(time, data))
# только настроить нужный формат вывода и параметры


# записываем в лог выбранный вариант меню с указанием даты/времени
def menu_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('log.txt', 'a',encoding="utf8") as file: #или log.csv файл?
        file.write('{};Выбран пунк меню;{}\n'
                    .format(time, data))

# записываем в лог введенную строку для расчета с указанием даты/времени
def input_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('log.txt', 'a',encoding="utf8") as file: #или log.csv файл?
        file.write('{};Введена строка;{}\n'
                    .format(time, data))

# записываем в лог ошибку с указанием даты/времени - аргумент data будет передаваться на стороне view
# на этапе обработки - здесь  просто фиксация
def error_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('log.txt', 'a',encoding="utf8") as file: #или log.csv файл?
        file.write('{};Зафиксирована ошибка;{}\n' #по хорошему как-то обозначить, какая
                    .format(time, data))

# записываем в лог выдачу результата - аргумент data будет передаваться на стороне view
def res_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('log.txt', 'a',encoding="utf8") as file: #или log.csv файл?
        file.write('{};Получен результат вычисления;{}\n' 
                    .format(time, data))

# записываем в лог показ файла лог - сама выдана будет описана на стороне view
# здесь фиксируем это событие
def view_log_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('log.txt', 'a',encoding="utf8") as file: #или log.csv файл?
        file.write('{};Выдан файл лога по запросу;{}\n' 
                    .format(time, data))

