# Задача 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# *Пример:*
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def check_input(text_input):
    check_input = False
    while not check_input:
        try:
            number_input = int(input(text_input))
            check_input = True
        except:
            print('Некорректный ввод')
    return number_input

def reverse_str(str_r):
    new_str = ""
    for i in range(len(str_r)-1,-1, -1):
        new_str+=str_r[i] 
    return new_str        

def get_binary(number):
    res_str = ""
    while number > 0:
        res_str = res_str + str(int(number % 2))
        number //= 2
    print(res_str) #вывожу для себя для проверки   
    return int(reverse_str(res_str))

num = check_input('Введите целое число: ')    
print('Двоичное число:', get_binary(num))




