
import easygui as g
import sys
# from easygui import *

import easygui
import os

# имя пользователя и пароль, как список ['admin', '545454']
list1 = ["имя пользователя","пароль"]
fin = easygui.multpasswordbox("Пожалуйста введите свой логин и пароль",title = "авторизоваться",fields = (list1))
print(fin)
exit()


try:
    int('Exception')
except:
    easygui.exceptionbox ('Ошибка преобразования данных типа int! Проверьте свой тип данных!')


# просто путь к папке
msg = 'Выберите файл, будет возвращен полный каталог файла'
title = 'Диалог выбора файла'
default = r'F:\flappy-bird'
full_file_path = easygui.diropenbox(msg, title, default)
print ('Полный путь к выбранному файлу:' + str (full_file_path))


msg = 'Поддержка большого текста'
title = 'Text Code'
text = 'abcdefghijklmnopqrstuvwxyzABCDEFGHJIKLMNOPQRSTUVWXYZ0123456789-/'
textContent = easygui.textbox(msg,title,text)
codeContent = easygui.codebox(msg,title,text) #можно использовать для моноширного текста/кода
print (textContent)
print (codeContent)


while 1:
    g.msgbox('Привет, добро пожаловать в интерфейс заказа')

    msg = "Какой кофе вы хотите выпить?"
    title = "заказ"
    choices = ['Карамель макиато', 'Ваниль Фуруи Уайт', "Ручной удар", "Капучино"]

    choice = g.choicebox(msg, title, choices)

    # Обратите внимание, что параметр msgbox - это строка
    # Если пользователь выбирает Отмена, функция возвращает None
    g.msgbox('«Ваш выбор:»' + str(choice), "результат")

    msg = "Вы хотите снова начать выбирать?"
    title = "пожалуйста, выбери"

    # Вызвать диалог продолжения / отмены
    if g.ccbox(msg, title):
        pass  # Если пользователь выбирает Продолжить
    else:
        sys.exit(0)  # Если пользователь выбирает Отмена

# след.пример
import easygui as g

msg = 'Пожалуйста, заполните следующую контактную информацию'
title = 'Учетный центр'
fieldNames = ["* имя пользователя", "* настоящее имя", 'Фиксированный телефон', " *номер мобильного телефона", "  QQ", " *E-mail"]
fieldValues = []
fieldValues = g.multenterbox(msg, title, fieldNames)

while 1:
    if fieldValues == None:
        break
    errmsg = ""
    for i in range(len(fieldNames)):
        option = fieldNames[i].strip()
        if fieldValues[i].strip() == "" and option[0] == "*":
            errmsg += (f'Требуется  % S \n\n   {fieldNames[i]}')
    if errmsg == "":
        break
    fieldValues = g.multenterbox(errmsg, title, fieldNames, fieldValues)

# print("Информация о пользователе следующая:% s" % str(fieldValues))

# пример с показом текста
import easygui as g
import os

file_path = g.fileopenbox(default="*.txt")

with open(file_path) as f:
    title = os.path.basename(file_path)
    msg = 'Содержимое файла [% s] выглядит следующим образом:' % title
    text = f.read()
    g.textbox(msg, title, text)

# примеры кнопок
import easygui
title = easygui.msgbox (msg = 'подсказка', title = 'часть заголовка', ok_button = "OOK")
 
msg = easygui.msgbox('Hello Easy GUI')
print('Возвращаемое значение: '+ msg)
 
ccbox = easygui.ccbox("here is Continue | Cancel Box!")
print('Возвращаемое значение: '+ str (ccbox))
 
ynbox = easygui.ynbox("Yes Or No Button Box!")
print('Возвращаемое значение: '+ str (ynbox))


image = 'me.jpg'
msg = 'Here is my photo,a python fan also'
choices = ['Yes','No',"Not Sure"]
title = 'Am I handsome?'
easygui.buttonbox(msg,title,image=image,choices=choices)

msg = 'Выберите из этого списка тот, который вам нравится'
title = 'Вы должны выбрать один'
choices = ['1','2','3','4','5','6','7']
answer = easygui.choicebox(msg,title,choices)
print('Вы выбрали: '+ str(answer)) #выдает конкретное выбранное значение

st = easygui.enterbox ("Пожалуйста, введите абзац текста: \ n")
print ("Вы ввели:" + str (st))

# для выбора полей для печати, например. когда несколько можно выбрать - возвращает список
msg = 'Выберите из этого списка тот, который вам нравится'
title = 'Вы должны выбрать один'
choices = (1,2,3,4,5,6,7,8,9)
answer1 = easygui.multchoicebox(msg,title,choices)
for item in answer1: #здесь можно выбрать много значений?
    print (item)     #и в цикле записывать в список - по которому потом печатать если выбраны

# число в диапазоне
msg = 'Введите число, диапазон от 0 до 100'
title = 'Только числовой тип'
lowerbound = 0
upperbound = 100
default = None
image = 'me.jpg'
result = easygui.integerbox(msg,title,default,lowerbound,upperbound,image)
print(result)

