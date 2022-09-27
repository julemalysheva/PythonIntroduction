# 11. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.

# *Пример:*

# - Для N = 5: 1, -3, 9, -27, 81

def check_input(text_input):
    check_input = False
    while not check_input:
        try:
            number_input = int(input(text_input))
            check_input = True
        except:
            print('Некорректный ввод')
    return number_input     

def n_count(n):
    num_i = 1
    for i in range(n-1):
        print(num_i, end=', ')  
        num_i *= -3 
    print(num_i)    

num_n =  check_input('N = ')   
n_count(num_n)     

# код с семинара
# n = int(input('Введите N '))
# z = 1
# for i in range(n):
# print(z, end = " " )
# z = z * -3
# print()