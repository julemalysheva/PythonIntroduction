# Задача 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт 
# разницу между максимальным и минимальным значением дробной части элементов.
# *Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def check_input(text_input):
    check_input = False
    while not check_input:
        try:
            number_input = float(input(text_input))
            check_input = True
        except:
            print('Некорректный ввод')
    return number_input

# задаем список через ввод с клавиатуры
def get_list(len_l):
    arr = []
    for _ in range(len_l):
        arr.append(check_input('Введите число: '))
    return arr


# выделяем дробную часть, в данном случае не округляю, иначе получаются не совсем те значения
def select_fp(num_float):
    # count_digits = (len(str(num_float))-len(str(int(num_float)))-1)
    # return round(num_float % 1, count_digits) 
    return num_float % 1

# ищем мин.дробную часть числа
def min_part(list_float):
    min_fract = select_fp(list_float[0])
    for el in list_float:
        if select_fp(el) < min_fract:
            min_fract = select_fp(el)
    return min_fract            

# ищем макс.дробную часть числа
# можно было и в одной функции найти и мин. и макс.и сразу разницу,
# но решила сделать так, разделить на подзадачи
def max_part(list_float):
    max_fract = select_fp(list_float[0])
    for i in range(1, len(list_float)): #есть ли смысл в такой записи, насколько оправдано сокращение на 1 итерацию
        if select_fp(list_float[i]) > max_fract:
            max_fract = select_fp(list_float[i])
    return max_fract            


list_num = get_list(5)
print(list_num)
print('Разница между максимальным и минимальным значением дробной части элементов')
print(f'равна {max_part(list_num)-min_part(list_num)}')
