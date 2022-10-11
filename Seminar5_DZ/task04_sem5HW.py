# задача 4 необязательная Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.


def find_step(pol):
    step = ''
    for i in range(len(pol)):
        if pol[i] == "^":
            step = step + pol[i + 1]
            while pol[i + 2].isdigit():
                step = step + pol[i + 2]
                i += 1
            break
    return int(step)

def return_koef(pol, max_step):
    list_kf = [(i, 0) for i in range(max_step+1)]
    kf = 0
    for i in range(max_step,1,-1):
        for el in pol:
            if f'^{i}' in el:
                if len(el) == len(str(i))+2: kf = 1 
                else: kf = int(el[:el.find('x')-1]) 
                list_kf[i] = (i, kf) #?стоит ли делать кортежем, 
        #если итак все значения на своих индексах по условию

# идем заполнять 1 и 0 степень отдельно
    for el in pol:
        # проверка условия для свободного члена, т.е. 0 степени
        if "x" not in el: 
            # if el.isdigit():
            kf = int(el)
            list_kf[0] = (0, kf)
        # проверка условия для x, т.е. 1 степени
        if el.find('x') == len(el)-1:
            kf = int(el[:-2])
            list_kf[1] = (1, kf)

    return  list_kf      


try:
    with open('Polynomial.txt', 'r') as fp:
        pol_a = fp.read()
    with open('Polynomial2.txt', 'r') as fp:
        pol_b = fp.read()
except:
    pol_a = "23*x^11 + 63*x^10 + 24*x^9 + 28*x^8 + 19*x^6 + 56*x^5 + 68*x^4 + 68*x^3 + 92*x^2 + x + 73 = 0"
    pol_b = "93*x^6 + 100*x^5 + 39*x^3 + 58*x^2 + 64 = 0"

# нашли макс. степень
big = find_step(pol_a) if find_step(pol_a) > find_step(pol_b) else find_step(pol_b)
# убираем =0 и делим на одночлены
pol_a = ''.join(pol_a.split('=')[:-1]).split('+')
pol_b = ''.join(pol_b.split('=')[:-1]).split('+')
#убираем пробелы 
pol_a = list(map((lambda el : el.strip() ),pol_a))
pol_b = list(map((lambda el : el.strip() ),pol_b))
# получаем список кортежей степень,коэфф-т
pol_akf = return_koef(pol_a, big)
pol_bkf = return_koef(pol_b, big)
# print(pol_akf)
# print(pol_bkf)

# складываем коэфф.при степенях- получаем список кортежей
# пока оставлю список кортежей, хотя было бы достаточно и списка, можно переделать
li_sum_kf = list(map(lambda x,y: (x[0], x[1]+y[1]) ,pol_akf, pol_bkf)) 
print(li_sum_kf)
li_sum_kf.reverse()
# убираем нулевые коэф.после сложения
li_sum_kf = list(filter(lambda e: e[1]!=0, li_sum_kf))
# собираем строку, производим замены
str_p = list(map(lambda x: (str(x[1]) + "*x^"+str(x[0])), li_sum_kf))
str_p = list(map(lambda x: x.replace("*x^0", ""), str_p))
str_pol = " + ".join(str_p)
str_pol = str_pol.replace(" 1*x", " x").replace("x^1 ", "x ")
str_pol = str_pol + ' = 0'

# print(str_p)
print(str_pol)

with open('Polynomial_Sum.txt', 'w') as data: 
    data.write(str_pol)
