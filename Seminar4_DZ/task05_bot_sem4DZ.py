# задача 5 необязательная Сделать локальный чат-бот с JSON хранилищем на основе приложенного буткемпа. 
# Тема чат-бота любая, но нельзя использовать одноуровневый список или словарь.

import json
print_find_key = False
del_find_key = False

url_base = {}
def load():
    global url_base
    with open("url.json", "r", encoding="utf-8") as fl:
        url_base = json.load(fl)
    print("База полезных ссылок загружена")

try:
    load()
except:
    url_base = {
            "FRONT": {
            "Html": {"Html1": "Изучение HTML: https://developer.mozilla.org/ru/docs/Learn/HTML",
                     "Html2": "Справочник по элементам HTML: https://developer.mozilla.org/en-US/docs/Web/HTML/Element",
                     "Html3": "Структура веб-сайта: https://developer.mozilla.org/ru/docs/Learn/HTML/Introduction_to_HTML/Document_and_website_structure"},
            "Css": {"Css1": "Справочник CSS: https://webref.ru/css",
                    "Css2": "Шпаргалка по флексам: https://tpverstak.ru/flex-cheatsheet/",
                    "Css3": "Игра для понимания работы Флексов: https://flexboxfroggy.com/#ru",
                    "Css4": "Гриды шпаргалка: https://tpverstak.ru/grid/"},
            "Js": {"Js1": "Современный учебник JavaScript: https://learn.javascript.ru",
                   "Js2": "Свойство innerHTML: https://innerhtml.ru/"},
            "Figma": {"Figma1": "Курсы по фигме: https://www.youtube.com/channel/UCClA4EqjQMGyYR2-TIuHwQw",
                      "Figma2": "Канал про Дизайн: https://www.youtube.com/channel/UCswtUaxvXXZe3KkwMtgrj9g"}

        },
        "PROGRAM": {
            "C_sharp": {"C#1": "C# Metanit: https://metanit.com/sharp/",
            "C#2": "Практическое руководство. Эндрю Троелсен, Филипп Джепикс: https://www.htbook.ru/kompjutery_i_seti/programmirovanie/yazyk-programmirovaniya-si-sharp-7-i-platformy-net-i-net-core"},
            "Py": {"Py1": "Metanit.com для изучения теории: https://metanit.com/python/",
            "Py2": "Обучение на Степик: https://stepik.org/course/67/promo",
            "Py3": "Изучаем Python 3 на примерах: https://python-scripts.com/"},
            "Database": {"Db1": "БАЗЫ ДАННЫХ. УЧЕБНИК С ПРАКТИКУМОМ: https://www.iprbookshop.ru/120171.html"},
            "Git":{"Git1":"Руководство по Git на русском: https://git-scm.com/book/ru/v2",
            "Git2": "Cкринкаст от Ильи Кантора: https://vimeo.com/showcase/5616060"}
        }
    }


# здесь печать вложенного словаря с отступами
# продумать печать по уровням вложенности, когда н-р нужно только разделы/подразделы для их выбора,
# чтоб не писать отдельно функцию
def print_dict(d, indent=0):
   for key, value in d.items():
      print('\t' * indent + str(key))
      if isinstance(value, dict):
         print_dict(value, indent+1)
      else:
         print('\t' * (indent+1) + str(value))

# выводит словарь по выбранному разделу/подразделу, и т.д.,т.е. по ключу
def print_item_for_keys(d, key, indent=0):
    #использую глобальную переменную, т.к. предполагается рекурсивный вызов функции, сообщения дублируются
    global print_find_key
    print_find_key = False
    if key in d:
        print_find_key = True
        print('\t' * indent + str(key))
        if isinstance(d[key], dict):
            print_dict(d[key], indent + 1)
    else:
        for k, v in d.items():
            if isinstance(v, dict):
                if key in v:
                    print_find_key = True
                    print('\t' * indent + str(key))
                    if isinstance(v[key], dict):
                        print_dict(v[key], indent + 1)
                    else:print('\t' * (indent + 1) + str(v[key]))
                    break
                else:
                    print_item_for_keys(v,key,0)


#будем печатать только разделы и подразделы
def print_section(d, indent=0):
   for key, value in d.items():
      print('\t' * indent + f'Раздел {key}')
      if isinstance(value, dict):
        for m in value.keys():
            print('\t' * (indent+1)+f'Подраздел {m}')

def del_url(d, el):
    global del_find_key
    del_find_key = False
    if el in d:
        del_find_key = True
        del d[el]
    else:
        for k, v in d.items():
            if isinstance(v, dict):
                if el in v:
                    del_find_key = True
                    del v[el]
                    break
                else:
                    del_url(v,el)

def save():
    with open("url.json", "w", encoding="utf-8") as fl:
        fl.write(json.dumps(url_base, ensure_ascii=False))
    print('Наша база url была успешно сохранена в файле url.json')

print()

while True:
    comd = input("Введите команду: ")
    if comd =="/start":
        print('К полету готовы! Жду дальнейших указаний...')
    elif comd =="/stop":
        print('О! - нет, я буду скучать)..До новых встреч!')
        save()
        break
    elif comd =="/help":
        print('Здесь будет описание всех команд')
    elif comd =="/url":
        print('/all - введите эту команду, чтоб получить весь список')   
        print('/select - введите эту команду, чтоб указать Раздел/Подраздел')  
    elif comd =="/all":
        print('Вот что мы уже собрали: ')
        print()
        print_dict(url_base)
    elif comd =="/select":
        print('Что будем искать? Вот что у меня есть: ')
        print()
        print_section(url_base)
        section = input('Введите раздел или подраздел: ')
        print_item_for_keys(url_base, section)
        if not print_find_key:
            print('Упс..что-то пошло не так..Такой раздел не найден - повторите команду)')
    elif comd == "/add":
        #Сейчас нов.эл.можно добавить только в существующий раздел/подраздел - добавить функционал создания Структуры
        print('Напоминаю, какая структура есть сейчас: ')
        print_section(url_base)
        section = input('Укажите, в какой раздел нужно добавить ссылку: ')
        subsection = input('Введите название нужного подраздела, где мы добавим элемент: ')
        inp_ok = input(f'Вы уверены, создаем запись в разделе: {section} в подразделе {subsection}? Напишите Да - если так: ')
        if inp_ok == "Да":
            id_url = input('Введите уникальный идентификатор записи, например: css2, py4 и т.д. и т.п.: ')
            url_base[section][subsection][id_url] = input('Введите короткое описание и саму ссылку: ')
            print(f'Новая запись добавлена в раздел {section}:')
            print_item_for_keys(url_base, subsection)
        else: print('ОК')
    elif comd == "/del":
        print('Должен предупредить, если вы введете значение Раздела или Подраздела - они будут удалены вместе со всеми записями')
        del_el = input('Будьте внимательны!.. Что будем удалить? Введите название Раздела/Подраздела или ID записи: ')
        del_url(url_base, del_el)
        if del_find_key:
            print('Элемент был удален из базы ссылок:')
            print_dict(url_base)
        else:print('Такой элемент не найден')
    elif comd == "/save":
        save()
    elif comd == "/load":
        load()
    else:
        print('Простите, я вас не понял. Я еще только учусь. Посмотрите, что я уже умею через /help')    
