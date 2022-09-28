# Задача 3. Реализуйте алгоритм перемешивания списка. 
# Список размерностью 10 задается случайными целыми числами, выводится на экран, 
# затем перемешивается, опять выводится на экран.

from random import randint

def set_random_list(first_num, end_num, size):
    random_list = []
    for _ in range(size):
        random_list.append(randint(first_num, end_num))
    return random_list

def reverse_list(my_list):
    size = len(my_list)//2
    for i in range(size):
        my_list[i], my_list[len(my_list)-1-i] = my_list[len(my_list)-1-i], my_list[i]  
    # print(f'Реверс списка: {my_list}')
        

def shuffle_list(my_list):
    reverse_list(my_list) 
    if len(my_list)>2:

        for i in range(0, (len(my_list)-1), 2):
            my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
        # print(f'Промежуточно: {my_list}')
    # for i in range(0, (len(my_list)-2), 3):
    #     my_list[i], my_list[i+2] = my_list[i+2], my_list[i]
    # print(f'Промежуточно: {my_list}')
    # for i in range(0, (len(my_list)-3), 4):
    #     my_list[i], my_list[i+3] = my_list[i+3], my_list[i]        
    # print(f'Промежуточно: {my_list}')
    # for i in range(0, (len(my_list)-4), 5):
    #     my_list[i], my_list[i+4] = my_list[i+4], my_list[i]        
    # print(f'Промежуточно: {my_list}')


# дальше пробовала прописать какой-то универсальный алгоритм в зависимости от длины списка,
# но пока чего-то не хватает - при разной длине не все значения меняются - но в целом работает)
def shuffle_list_n(my_list):
    # reverse_list(my_list) #посмотреть, может его убрать вообще, оставить только на длину 2
    n = len(my_list)//2
    if len(my_list)>2:
        for с in range(n): 
            for i in range(0, (len(my_list)-1-с), 2+с): 
                my_list[i], my_list[i+1+с] = my_list[i+1+с], my_list[i]
            # print(f'Промежуточно {с}: {my_list}')

    # else: reverse_list(my_list)
        # for с in range(1, n+1): #пробую др.вариант, это работало, только при размере 4 не все смешались
        #     for i in range(0, (len(my_list)-с), с+1):
        #         my_list[i], my_list[i+с] = my_list[i+с], my_list[i]
        #     print(f'Промежуточно {с}: {my_list}')
    reverse_list(my_list)            


        

my_list = set_random_list(10, 99, 9)
new_list = my_list
print(f'Задан список:  {my_list}') 
shuffle_list(my_list)
print(f'Смешали спис: {my_list}') 
print("Второй вариант: ") 
print(f'Задан ВТОРОЙ:  {new_list}') 
shuffle_list_n(new_list)
print(f'Смешиваем 2й: {new_list}')

