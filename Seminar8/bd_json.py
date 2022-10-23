import json
# from main import * #staff #сама переменная инициализируется и формируется в модуле main 
import logger as log
from easygui import *

def load():
    # global staff
    with open("staff.json", "r", encoding="utf-8") as fl:
        staff = json.load(fl)
        log.register_logger("База сотрудников загружена")
    msgbox("База сотрудников загружена")
    # print("База сотрудников загружена")
    return staff

# может добавить try?
def save(data): 
    # global staff
    try:
        with open("staff.json", "w", encoding="utf-8") as fl:
            fl.write(json.dumps(data, ensure_ascii=False))
            log.register_logger("База успешно сохранена в файле staff.json")
        msgbox('База сотрудников была успешно сохранена в файле staff.json')    
        # print('База сотрудников была успешно сохранена в файле staff.json')
    except: 
        log.error_logger('Ошибка сохранения базы')
        msgbox('Ошибка сохранения базы')    


