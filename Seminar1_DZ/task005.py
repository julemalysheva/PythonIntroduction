# Задача 5 VERY HARD SORT необязательная
# Задайте двумерный массив из целых чисел. Количество строк и столбцов задается с клавиатуры.
# Отсортировать элементы по возрастанию слева направо и сверху вниз.
# Например, задан массив:
# 1 4 7 2
# 5 9 10 3
# После сортировки
# 1 2 3 4
# 5 7 9 10

def input_num(str_input):
    ch_num = False
    while not ch_num:
        try:
            num_input = int(input(str_input))
            ch_num = True
        except:
            print('Некорректный ввод, введите число')
    return num_input


def get_array(m, n):
    arr = []
    for row in range(m):
        arr_col = list()
        for el in range(n):
            num = input_num('Введите число: ')
            arr_col.append(num)
        arr.append(arr_col)
    return arr


def print_arr(arr):
    for row in arr:
        for elem in row:
            print(elem, end=' ')
        print()


# def selection_sort_col(arr): #в данном случае сортируются элементы по столбцам внутри строк по возрастанию       
#     for i in range(len(arr)):
#         for j in range(len(arr[i])):
#             minimum = j
        
#             for k in range(j + 1, len(arr[i])):
#                 if arr[i][k] < arr[i][minimum]:
#                     minimum = k

#             arr[i][minimum], arr[i][j] = arr[i][j], arr[i][minimum]
            
#     return arr

def selection_sort(arr): #сортировка списка - одномерного массива       
    for i in range(len(arr)):
        minimum = i
        
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minimum]:
                minimum = j

        arr[minimum], arr[i] = arr[i], arr[minimum]
            
    return arr

#не придумала др.варианта, кроме как перенести элементы двумерного в обычнй список,
#и уже отсортированный (функцией выше) вернуть обратно
def sort_array(arr):
        list_arr = []
        for row in arr:
            for elem in row:
                list_arr.append(elem) 
        list_arr = selection_sort(list_arr)
        print(f'Промежуточный сортированный список {list_arr}')#вывод на экран для проверки

        position = 0
        new_arr = []
        for i in range(len(arr)):
            arr_col = list()
            for j in range(len(arr[i])): 
                arr_col.append(list_arr[position])
                position+=1
            new_arr.append(arr_col)     

        return new_arr                


row = input_num('Введите кол-во строк: ')
col = input_num('Введите кол-во столбцов: ')
my_array = get_array(row, col)
print(my_array) #вывожу сначала в строку
print('Задан массив:')
print_arr(my_array) #вывожу матрицей
# print('Сортируем массив - так получается только слева направо, по столбцам внутри строк:')
# print_arr(selection_sort_col(my_array))
new_array = sort_array(my_array)
print('Отсортированы элементы по возрастанию слева направо и сверху вниз:')
print_arr(new_array)


