# задача 3. Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка
# (или на какой оси она находится).

# *Пример:* - x=34; y=-30 -> 4 - x=2; y=4-> 1 - x=-34; y=-30 -> 3

def input_num(str_input):
    ch_num = False
    while not ch_num:
        try:
            num_input = float(input(str_input))
            ch_num = True
            if num_input == 0:
                print('Значение не должно быть равно 0')
                ch_num = False
        except:
            print('Некорректный ввод, введите число')
    return num_input


def quarter_number(x, y):
    if (x > 0 and y > 0):
        return 1
    elif (x < 0 and y > 0):
        return 2
    elif (x < 0 and y < 0):
        return 3
    else:
        return 4


num_x = input_num('Введите координату точки по оси X = ')
num_y = input_num('Введите координату точки по оси Y = ')
print(quarter_number(num_x, num_y))
