#  17. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

import random

def check_input(text_input):
    check_input = False
    while not check_input:
        try:
            number_input = int(input(text_input))
            check_input = True
        except:
            print('Некорректный ввод')
    return number_input


def fill_list(n):
    list_n = []
    for _ in range(n):
        list_n.append(random.randint(-n, n))
    return list_n

# если нам не нужно по условию выводить значения позиций в файле, то нет смысла дважды проходить цикл и 
# сначала добавлять их в список, а потом перебирая цикл - искать произведение. Можно сразу умножать значения 
# по нужным позициям.
def multiply_for_position_file(file, list_item):
    multiply_item = 1
    for line in file:
        if 0 <= int(line) < len(list_item):
            multiply_item *= list_item[int(line)]
    return multiply_item            


count_num = check_input('N = ')
print(fill_list(count_num))
with open('file.txt', 'r') as data:
    multiply_list = multiply_for_position_file(data, fill_list(count_num))
print(multiply_list)

exit()

# 17. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
#  Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
# код из зала - работает после моих корректировок

import random
import os

path = "file.txt"

def fill_list(n):
    list = []
    for i in range(0, n):
        list.append(random.randint(-n, n))
    return list

# по хорошему здесь нужно добавить на вход длину списку и чекать его при добавлении индекса из файла в новый список
def read_file(len_list):
    file = open(path, "r")
    list = []
    for line in file:
        # добавляю условие проверки индекса с длиной списка элементов 
        if 0 <= int(line) < len_list:
            list.append(int(line))
    file.close()
    return list

def multi_on_pos(list, pos):
    result = 1
    for i in range(0, len(pos)):#здесь проходили по списку элементов - было len(list), надо по списку позиций
        # значение не по i, а по pos[i]
        result *= list[pos[i]] #берем значение из list по позиции из pos, список которых получили из файла
        # если просто так делать без проверок длины списка элементов, получаем IndexError: list index out of range
        # поэтому можно проверку длины добавить в момент заполнения в ф-цию read_file
        #или вообще по другому записать цикл, типа:
    # for pos_item in pos:
    #     result*=list[pos_item] 
    return result

def main():
    n = int(input("Ведите N: "))
    list = fill_list(n)
    print(list)
    positions = read_file(len(list))
    print(positions)
    print("Произведение элементов на указанных позициях: ", multi_on_pos(list, positions))

if __name__ == "__main__":
    main()
