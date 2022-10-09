# задача 5 необязательная Дан список чисел. Создайте список, в который попадают числа, 
# описывающие максимальную возрастающую последовательность. Порядок элементов менять нельзя.
# *Пример:* 
# [1, 5, 2, 3, 4, 6, 1, 7] => [1,  7] 
#     [1, 5, 2, 3, 4,  1, 7, 8 , 15 , 1 ] => [1,  5]
from random import randint

# li_num = [1, 5, 2, 3, 4, 6, 1, 7]
li_num = [randint(1,10) for i in range(8)]
# вызывать эту ф-цию в цикле перебора массива, сравнивая его длину
def сheck_seq(el, list_num):
    new_li= []
    new_li.append(el)
    for _ in range(len(list_num)):
        if el+1 in list_num:
             new_li.append(el+1)
             el+=1
    return new_li

max_seq = 1
for el in li_num:
    if len(сheck_seq(el, li_num)) > max_seq:
        max_seq = len(сheck_seq(el, li_num))
        min_el = el
li_seq = сheck_seq(min_el, li_num)
max_li = []
max_li.append(li_seq[0])
max_li.append(li_seq[-1])

print('Список чисел', li_num)
print(f'Макс.последовательность: {li_seq}')
print(f'Границы.последовательности: {max_li}')


