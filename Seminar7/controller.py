from calc_r import calc_rational
from calc_c import calc_compl
import view
import logger as log

# в зависимости от типа строки запускаем разный функционал
# "r" - рациональ.,иначе - комплексные считаем
def calc_data(t, data):
    return calc_rational(data) if t == "r" else calc_compl(data)

def button_click():
    # запускаем цикл бесконечного вызова меню, пока не выберет 3 - Выход
    while True:
        var = view.get_variant()
        # если выбран пункт меню 1 - расчет
        if var == 1:
            # t-тип данных, value - сама строка
            t, value= view.get_value() #значения из кортежа передали переменным
            try:
                result = calc_data(t, value) #и уже вызываем нужную ф-цию
                view.view_data(result, "resul") #выдаем результат
            except:
                log.error_logger('Некорректное выражение')  
                print('Некорректный ввод выражения')  
        # если выбран пункт меню 2 - показать лог
        elif  var == 2:   
            view.view_logger('log.txt')
        # # предполагаем, что проверка ввода идет на стороне view, тогда Иначе будет соответствовать пункту 3 - Выход
        # # прерываем цикл
        else: 
            # здесь вопрос, прописываем это здесь или через отдельный модуль во view?
            print('Будем рады новой встрече))')
            break    