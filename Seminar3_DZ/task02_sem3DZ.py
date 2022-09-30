# Задача 2. Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from random import randint

def check_input(text_input):
    check_input = False
    while not check_input:
        try:
            number_input = int(input(text_input))
            check_input = True
        except:
            print('Некорректный ввод, нужно целое число')
    return number_input

def get_random_list(start, end, size):
    new_list = []
    for _ in range(size):
        new_list.append(randint(start, end))
    return new_list

def multiply_list_pairs(my_list):
    new_list = []
    len_limit = len(my_list)//2 
    if len(my_list)%2 != 0: len_limit+=1
    for i in range(len_limit):
        new_list.append(my_list[i] * my_list[len(my_list)-1-i])
    return new_list

len_list = check_input('Введите длину списка чисел: ')   
list_num = get_random_list(1, 10, len_list)   
print('Задан список:', list_num)  
print(f'Произведение пар чисел: {multiply_list_pairs(list_num)}') 

