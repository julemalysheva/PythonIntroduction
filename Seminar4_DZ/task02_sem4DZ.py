# задача 2 . Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

from random import randint
# сделала два варианта: просто преобразовать в множество
# или проверить предварительно сортированный список

def random_list(start,end,size):
    rand_list = []
    for _ in range(size):
        rand_list.append(randint(start, end))
    return rand_list

def bubble_sort(lst):
    for i in range(1,len(lst)):
        for j in range(len(lst)-i):   
            if lst[j] < lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]  

def non_repeat(list_num):
    non_repeat = []
    for i in range(len(list_num)-1):
        if list_num[i] != list_num[i+1]:
            non_repeat.append(list_num[i])
    # вопрос, как быть с последним элементом - выводим отдельно
    non_repeat.append(list_num[len(list_num)-1])        
    return non_repeat            


list_num = random_list(1,15,25)
print()
print(f'Задана последовательность чисел: {list_num}')  
print(f'Множество неповторяющихся элементов: {set(list_num)}')   
print()
bubble_sort(list_num)
print('Второй вариант без множества через сортировку:')
print(f'Список неповторяющихся элементов: {non_repeat(list_num)}')   
