# # думаю, логично 4 ф-ции:
# 1. Вход/выход - загрузка/сохранение
# 2. Выбор меню - запрос пользователя
# 3. Результат запроса - выполнено
# 4. Информация об ошибке на любом шаге

# Все ф-ции работают по одному принципу, делают одно и то же - фиксируют событие в файл с указанием даты/времени
# Вызываются в др. модулях при каждом взаимодействии с пользователем.

from datetime import datetime as dt
from time import time
# записываем в лог вход и выход пользователя
def register_logger(data=''):
    with open('log.txt', 'a',encoding="utf8") as file:
        file.write('{} Зафиксировано событие {}\n'
                    .format(dt.now().strftime('%d.%m.%Y-%H:%M'), data))
# записываем в лог вариант меню с запросом пользователя
def menu_logger(data=''):
    with open('log.txt', 'a',encoding="utf8") as file:
        file.write('{} Выбран пункт меню {}\n'
                    .format(dt.now().strftime('%d.%m.%Y-%H:%M'), data))
# записываем в лог (фиксацию) ошибки с указанием даты/времени 
def error_logger(data=''):
    with open('log.txt', 'a',encoding="utf8") as file:
        file.write('{} Зафиксирована ошибка {}\n' #по хорошему как-то обозначить, какая
                    .format(dt.now().strftime('%d.%m.%Y-%H:%M'), data))
# записываем в лог выдачу результата запроса
def res_logger(data=''):
    with open('log.txt', 'a',encoding="utf8") as file:
        file.write('{} Получен результат запроса {}\n'
                    .format(dt.now().strftime('%d.%m.%Y-%H:%M'), data))