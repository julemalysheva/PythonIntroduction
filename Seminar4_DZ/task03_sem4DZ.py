# задача 3. Задана натуральная степень k. Сформировать случайным образом список 
# коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# *Пример:* 
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint

def input_num(str_input):
    ch_num = False
    while not ch_num:
        try:
            num_input = int(input(str_input))
            ch_num = True
            if num_input <= 0:
                print('Значение должно быть > 0')
                ch_num = False
        except:
            print('Некорректный ввод, введите число')
    return num_input

def ls_koef(k):
    koef = []
    for i in range(k):
        koef.append(randint(0,100)) 
     #старший коэф-т не мож.быть = 0
    koef.append(randint(1,100))
    return koef              

def create_polynomial(k):
    str_pol = ''
    kf = ls_koef(k)
    print(f'Список коэф: {kf}')
    pol = []
    #будем идти с конца, от k вниз, т.к. нам обязательно нужен старший коэф и последовательность от большего
    for i in range(k,1,-1):
        if kf[i] != 0:
            pol.append(str(f'{kf[i]}*x^{i}'))
    if kf[1] != 0:
            pol.append(str(f'{kf[1]}*x'))        
    if kf[0] != 0:
            pol.append(str(kf[0]))        
    # print(pol)
    str_pol = " + ".join(pol)
    str_pol = str_pol.replace(" 1*x", " x")
    str_pol = str_pol + ' = 0'
    # print(str_pol)
    return str_pol
    

k = input_num('Натуральная степень k = ')
str_polynomial = create_polynomial(k)
print(str_polynomial)
with open('Polynomial.txt', 'w') as data: 
    data.write(str_polynomial)

#формирую второй файл для след. задачи:
k = input_num('Натуральная степень k = ')
str_polynomial = create_polynomial(k)
print(str_polynomial)
with open('Polynomial2.txt', 'w') as data: 
    data.write(str_polynomial)
