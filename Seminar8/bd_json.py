import json
# from main import * #staff #сама переменная инициализируется и формируется в модуле main 
import logger as log
from easygui import *

def load(file):
    # global staff
    with open(file, "r", encoding="utf-8") as fl:
        data = json.load(fl)
        log.register_logger("База сотрудников загружена")
    # msgbox("База сотрудников загружена")
    # print("База сотрудников загружена")
    return data

# может добавить try?
def save(data, file): 
    # global staff
    try:
        with open(file, "w", encoding="utf-8") as fl:
            fl.write(json.dumps(data, ensure_ascii=False))
            log.register_logger(f'Сохранение прошло успешно в файле {file}')
        # print('База сотрудников была успешно сохранена в файле staff.json')
    except: 
        log.error_logger('Ошибка сохранения базы')


