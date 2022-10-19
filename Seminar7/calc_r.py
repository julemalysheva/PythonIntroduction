import re
import logger as log

# здесь просто прописываем алгоритм расчета, все данные импортируются и передаются в эти ф-ции 
# внутри controller или main

# доработать вместо eval расчет выражения по строке для работы с рацион.числами, учитывая точку . и проверить работу знака - минус
# у меня ф-ция считает через список
# def calc_rational(data):
#     res = eval(data)
#     return res

def str_to_list(str_exp):
    # дальше пробую получить выражение из строки
    li_ch = re.split(r'\s*([()+*/-])\s*', str_exp)
    # убираем лишние '' - не смогла их обойти в регулярке, где есть число перед минусом или скобки()
    li_ch = list(filter((lambda el: el != ''), li_ch))
    print('Получили список из строки: ',li_ch)
    # преобразую числа во float
    li_zn = ['(',')','+','*','/','-']
    li_ch = list(map((lambda el: float(el) if el not in li_zn else el), li_ch))
    print('Преобразовали во float: ',li_ch)

    # обработка минусов
    # здесь минус перед первым числом в начале строки 
    if li_ch[0] == '-' and isinstance(li_ch[1], float):
        li_ch[1]=-li_ch[1]
        li_ch.pop(0)
        # print('убрали "-" в начале строки', li_ch)

    # список нужен для проверки, если эл-т перед минусом входит в этот список, значит "-" удаляем и добавляем к числу 
    li_zn = ['(','+','*','/','-'] #сюда не входит ")" - после нее возможен минус как знак выражения если перед числом
    size = len(li_ch)
    j = 2 #?3
    while j<size:
        # print('смотрим индекс:', j)
        if isinstance(li_ch[j], float) and li_ch[j-1] == '-':
            if li_ch[j-2] in li_zn:
            # not (isinstance(li_ch[j-2], float)) or (li_ch[j-2] != ')') :
                li_ch[j] = - li_ch[j]
                li_ch.pop(j-1)
                # print(f'Удален минус на позиции: {j-1}')
                # print(li_ch)
                size-=1 #размер при удалении уменьшается
                # print("Размер уменьшен до ", size)
                j-=1 #индексы смещяются - пробую быть в ранге, если удалили
                # print('индекс уменьшен', j)
        j+=1 #здесь переключаем счетчик     
        
    print('Избавляемся от минусов: ',li_ch)   
    return li_ch 


# идет расчет по списку

def operation(math_operation,x,y):
        if math_operation == "+":
            return x+y
        elif math_operation == "-":
            return x-y
        elif math_operation == "/":
            return x/y
        elif math_operation == "*":
            return x*y

# удалить, если сработает нормально внутри ф-ции, в т.ч. со скобками
# def calc(znak,li_ch): 
#     res_i = li_ch.index(znak) 
#     print("индекс знака операции = ", res_i)
#     # помещаем рез-т на предыдущее от знака место
#     li_ch[res_i-1] = operation(znak, li_ch[res_i-1], li_ch[res_i+1])
#     # удаляем след.два эл-та
#     del li_ch[res_i:res_i+2]
#     print('Список после операции', li_ch)
#     return li_ch

def calc(li_ch):
    while len(li_ch) > 1:
        while "(" in li_ch: 
            # здесь находим крайнее вхождение откр.скобки "(""
            r_index = (len(li_ch) -1) - list(reversed(li_ch)).index("(")
            print("индекс ( = ", r_index)
            # пробуем найти первый индекс закрытой скобки ")"
            # по идее можно проверить, если индекс ) больше последнего вхождения ( - значит скобки не вложенные, 
            # а по порядку. и применить др. логику - но не все сразу)) 
            try:
                ind = li_ch.index(")")
                print("индекс ) = ", ind)
            except:
                log.error_logger('Выражение со скобками задано неверно')
                print('Выражение задано неверно')  
            #сначала удаляем скобки и со смещением индексов передаем в ф-цию срез,иначе они снова будут найдены 
            li_ch.pop(r_index)  
            li_ch.pop(ind-1)  #-1 т.к. при удалении ( скобки прошло смещение
            print("удалили скобки", li_ch)
            print('диапазон в скобках',li_ch[r_index:ind-1])
            # передали срез внутри скобок в эту же ф-цию и вернули значение на место бывшей скобки (
            li_ch[r_index] = calc(li_ch[r_index:ind-1]) 
            #после отработки скобок результат помещаем на место откр.скобки(,остальное удаляем
            del li_ch[r_index+1:ind-1] 
            # 18.10 убрала пока удаление, т.к. по идее должно все удаляться внутри циклов расчета
            # не, при удалении др. рез-т,т.к. вызываем рекурсивно
            print('список после расчета в скобках', li_ch)

        # выполняем действия по порядку
        print('Выполняем действия по порядку')

        while "/" in li_ch or "*" in li_ch:
            for el in li_ch:
                if el == '*' or el == '/':
                    res_i = li_ch.index(el) 
                    print("индекс знака операции */ = ", res_i)
                    # помещаем рез-т на предыдущее от знака место
                    li_ch[res_i-1] = operation(el, li_ch[res_i-1], li_ch[res_i+1])
                    # удаляем след.два эл-та
                    del li_ch[res_i:res_i+2]
                    print('Список после операции', li_ch)

                    # li_ch = calc(el,li_ch)  
        while "+" in li_ch or "-" in li_ch:
            # таким образом пытаюсь выполнять +-по порядку в списке, а не как задано в цикле
            for el in li_ch:
                if el == '+' or el == '-':
                    res_i = li_ch.index(el) 
                    print("индекс знака операции +- = ", res_i)
                    # помещаем рез-т на предыдущее от знака место
                    li_ch[res_i-1] = operation(el, li_ch[res_i-1], li_ch[res_i+1])
                    # удаляем след.два эл-та
                    del li_ch[res_i:res_i+2]
                    print('Список после операции', li_ch)
                    # li_ch = calc(el,li_ch)  
    
    return li_ch[0]
             
def calc_rational(data):
    # пока ввод для проверки - а так значение берем из блока вью
    # str_exp = input('Введите выражение: ')
    li_ch = str_to_list(data)
    print(f'{data} = {calc(li_ch)}')
    print(f'Расчет eval для проверки: {eval(data)}')
    return calc(li_ch)

