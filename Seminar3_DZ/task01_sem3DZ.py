#  Задача 1 Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, 
#  стоящих на нечётной позиции.
#  *Пример:*
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint

def get_random_list(start, end, size):
    new_list = []
    for _ in range(size):
        new_list.append(randint(start, end))
    return new_list

def sum_odd_pos(my_list):
    sum_odd = 0 
    for i in range(1, len(my_list), 2):
        sum_odd+= my_list[i]     
    return sum_odd

my_list = get_random_list(1, 20 , 6)
print(f'Задан список: {my_list}')
print('Сумма элементов на нечетных позициях: ', sum_odd_pos(my_list))                  
