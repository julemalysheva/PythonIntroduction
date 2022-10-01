# Задача 1. Напишите программу, которая принимает на вход вещественное или целое число и
# показывает сумму его цифр. Через строку нельзя решать.

# *Пример:*

# - 6782 -> 23
# - 0,56 -> 11


def check_input(text_input):
    check_input = False
    while not check_input:
        try:
            number_input = float(input(text_input))
            check_input = True
        except:
            print('Некорректный ввод')
    return number_input

# здесь если число дробное, сначала переводим его в целое до последнего знака после запятой
# но возникает проблема - в случае с 0,56 или 4,56 например, появляются "лишние" цифры в типе float и результат неверный.
# поэтому для округления пришлось воспользоваться длиной строки.
# Дальше несколько вариантов моих попыток - пробовала по разному, пока не додумалась до округления))

# Первый вариант - окончательный, к которому пришла
def sum_digits(number):
    # число знаков после точки
    znakov = (len(str(number))-len(str(int(number)))-1) 
    number = round(number, znakov)
    print(f'1 вариант - Первое округление до цикла приведения к целому: {number}')

    while number % 1 != 0: 
        znakov-=1 #с каждым циклом число знаков после запятой сокращается на 1
        number= round(number*10, znakov)

    number = int(number)    
    print(f'1 вариант - Целое число для расчетов: {number}')

    sum_digits = 0
    while number != 0: 
        sum_digits += number % 10 
        number//=10
    
    return sum_digits      

# Второй вариант - разделяю число на две части: левое целое и правое дробная оставшаяся часть,
# прохожусь по ним разными циклами, результат складываю. Также без округления с разными числами порой
# выдавал "лишние" цифры после запятой, пришлось округлять на каждом шаге
def sum_digits2(number):
    sum_digits = 0
    int_number = int(number) #получаю левую часть - целое число для первого цикла

    znakov = (len(str(number))-len(str(int(number)))-1) # число знаков после точки для округления
    right_num = round(number - int(number),znakov) # получаю правую дробную часть без целого
    print(f'2 вариант - Правая часть числа без целого: {right_num}')
    
    # первый цикл по левой части
    while int_number>0:
        sum_digits += int_number%10
        int_number//=10

    # второй цикл по правой дробной, если она есть
    while right_num % 1 != 0:
        znakov-=1
        right_num = round(right_num*10,znakov) #добавила округление до нужного числа знаков
        sum_digits += int(right_num%10) 
                
    return sum_digits 

# это вариант по типу первого, но цикл организован по длине строки
# сколько знаков после запятой - столько раз умножаем на 10 до целого
def sum_digits3(number):
    if number % 1 != 0:
        #считаем число знаков после запятой, если они есть, для округления
        znakov = (len(str(number))-len(str(int(number)))-1) 
        number = round(number, znakov)
        r = range(znakov)
        for _ in r:
            znakov-=1
            number= round(number*10, znakov)
    number = int(number)    
    print(f'3 вариант - считаем цифры числа: {number}')
    
    # теперь изымаем цифру каждого разряда и суммируем
    sum_digits = 0
    while number != 0: 
        sum_digits += number%10 
        number//=10
    
    return sum_digits    

# вариант со строкой - пусть тоже будет)
def sum_digitsofstr(number):
    sum_digits = 0
    for el in str(number):
        if el != '.':
            sum_digits += int(el)
    return sum_digits            


number_input = check_input('Введите число: ')
print(f'Остаток от деления на 1 = {number_input%1}')

print(f'1 вариант: {sum_digits(number_input)}')
print(f'2 вариант: {sum_digits2(number_input)}')
print(f'3 вариант: {sum_digits3(number_input)}')
print(f'Вариант по строке: {sum_digitsofstr(number_input)}')

# еще один вариант решения, где проверка идет на равенство целому числу, а не по остатку деления
# a = float(input('a = '))
# c = 0
# sum = 0
# while a!=int(a):
#     a *= 10
# b = a
# while b != 0:
#     sum += b%10
#     b = b//10
# print(int(sum))

# exit()