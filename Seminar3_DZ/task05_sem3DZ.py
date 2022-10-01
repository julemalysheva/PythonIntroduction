# задача5 HARD необязательная.
# Сгенерировать массив случайных целых чисел размерностью m*n (размерность вводим с клавиатуры) ,
#  причем чтоб количество элементов было четное. Вывести на экран красивенько таблицей. 
#  Перемешать случайным образом элементы массива, причем чтобы каждый гарантированно переместился
#   на другое место и выполнить это за m*n / 2 итераций. То есть если массив три на четыре, 
#   то надо выполнить не более 6 итераций. И далее в конце опять вывести на экран как таблицу.

from random import choice, randint
# использую choice, чтоб случайным образом получить индексы для смешивания,
# как по условию задачи

def input_num(str_input):
    ch_num = False
    while not ch_num:
        try:
            num_input = int(input(str_input))
            ch_num = True
        except:
            print('Некорректный ввод, введите число')
    return num_input

def get_array_random(m, n, start, end):
    arr = []
    for row in range(m):
        arr_col = list()
        for el in range(n):
            arr_col.append(randint(start, end))
        arr.append(arr_col)
    return arr

def print_arr(arr):
    for row in arr:
        for elem in row:
            print(elem, end=' ')
        print()    

# задаем массив индексов, который используем для рандомного перемешивания,
# равный: число строк*число столбцов
def list_index(m,n):
    return list(range(m*n))

# здесь по индексу возвращаем соответствующие индексы строки и столбца в двумерном
# массиве через кортеж, в зависимости от числа столбцов 
def return_indexes(index, col):
    return (index//col, index%col)

# производим замену значений по случайно выбранным индексам
def mixing_pairs(list_arr, list_index):
    global col
    for _ in range(len(list_index)//2):
        ind1 = choice(list_index) 
        list_index.pop(list_index.index(ind1))
        ind1 = return_indexes(ind1, col) 
        ind2 = choice(list_index)
        list_index.pop(list_index.index(ind2))
        ind2 = return_indexes(ind2, col) 
        list_arr[ind1[0]][ind1[1]], list_arr[ind2[0]][ind2[1]] = list_arr[ind2[0]][ind2[1]], list_arr[ind1[0]][ind1[1]] 


check_even = False
while not check_even:
    row = input_num('Введите кол-во строк: ')
    col = input_num('Введите кол-во столбцов: ')
    if row*col%2==0:
        check_even = True
        my_array = get_array_random(row, col, 10, 99)
        print_arr(my_array)
        mixing_pairs(my_array, list_index(row, col))
        print('Перемешали случайным образом элементы массива:')
        print_arr(my_array)
    else: 
        print('Введите размерность, при которой число элементов будет четным')            






