# Задача 3. Реализуйте алгоритм перемешивания списка. 
# Список размерностью 10 задается случайными целыми числами, выводится на экран, 
# затем перемешивается, опять выводится на экран.

from random import randint

def set_random_list(first_num, end_num, size):
    random_list = []
    for _ in range(size):
        random_list.append(randint(first_num, end_num))
    return random_list
       

def shuffle_list(my_list):
    if len(my_list) % 2 == 0:
        limit = len(my_list)//2 
        if len(my_list) == 2: 
            limit = 1
    else: limit = len(my_list)//2 + 1    

    for c in range(limit):
        for i in range(c, (len(my_list)-1), 2):
            my_list[i], my_list[i+1] = my_list[i+1], my_list[i]

def reverse_list(my_list):
    size = len(my_list)//2
    for i in range(size):
        my_list[i], my_list[len(my_list)-1-i] = my_list[len(my_list)-1-i], my_list[i]  
    # print(f'Реверс списка: {my_list}')

# дальше пробовала прописать иной алгоритм в зависимости от длины списка,
# но пока чего-то не хватает - при разной длине не все значения меняются - но в целом работает)
def shuffle_list_n(my_list):
    # reverse_list(my_list) #посмотреть, может его убрать вообще, оставить только при длине = 2?
    n = len(my_list)//2
    if len(my_list)>2:
        for с in range(n): 
            for i in range(0, (len(my_list)-1-с), 2+с): 
                my_list[i], my_list[i+1+с] = my_list[i+1+с], my_list[i]
            # print(f'Промежуточно {с}: {my_list}')
    reverse_list(my_list)            


my_list = set_random_list(10, 99, 10)
new_list = my_list
print(f'Задан список:  {my_list}') 
shuffle_list(my_list)
print(f'Смешали спис: {my_list}') 
print("Второй вариант: ") 
print(f'Задан ВТОРОЙ:  {new_list}') 
shuffle_list_n(new_list)
print(f'Смешиваем 2й: {new_list}')

