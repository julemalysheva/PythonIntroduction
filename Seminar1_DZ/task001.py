# задача 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.

# *Пример:* - 6 -> да - 7 -> да - 1 -> нет -

def input_num(str_input):
    ch_num = False
    while not ch_num:
        try:
            num_input = int(input(str_input))
            ch_num = True
        except:
            print('Некорректный ввод, введите число') 
    return num_input               


def check_day(day_number):
    if (1 <= day_number <= 5):
        return 'Нет'
    elif (day_number == 6 or day_number == 7):
        return 'Да'
    else:
        return 'Ввели значение вне диапазона 1-7'



num_day = input_num("Введите день недели от 1 до 7: ")
print(check_day(num_day))

