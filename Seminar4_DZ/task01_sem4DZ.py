# задача 1. Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.

def check_input(text_input):
    check_input = False
    while not check_input:
        try:
            number_input = int(input(text_input))
            check_input = True
        except:
            print('Некорректный ввод')
    return number_input

# не беру в расчет 1
def prime_factors(n):
    list_factors = []
    mp = 2
    while mp<=n:
        while n%mp==0:
           list_factors.append(mp) 
           n = n/mp
        mp+=1
    return list_factors       

num = check_input('Введите число N: ')
if num>1: 
    if len(prime_factors(num))>1:
        print('Простые множители числа', num, ': ', prime_factors(num))
    else: print('Простое число', num, 'делится само на себя:', prime_factors(num))
else: print('Введите число > 1')
    