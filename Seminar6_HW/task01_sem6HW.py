# Задача 1. Создайте программу для игры в "Крестики-нолики".

def print_field(field):
    for i in range(len(field)):
        print(' | '.join(field[i]))


def ch_input(text):
    check_input = False
    while not check_input:
        try:
            pos = list(map(int, input(text).split(',')))
            check_input = True
            if pos[0] > 3 or pos[1] > 3 or pos[0] < 1 or pos[1] < 1:
                print('Значения могут быть только от 1 до 3')
                check_input = False
        except:
            print('Некорректный ввод')
    return pos


def check_win(field, elem_go):
    # проверяем по строкам через число вхождений
    for el in field:
        if el.count(elem_go) == 3:
            return True
# здесь я тренируюсь транспонировать вложенный список ускоренными методами)
    # col_in_row = list(map(list, zip(*field)))
    col_in_row = [[field[j][i]
                   for j in range(len(field))] for i in range(len(field[0]))]
# проверяем по столбцаи   
    for el in col_in_row:
        if el.count(elem_go) == 3:
            return True
# проверяем главную диагональ
    find_el = 0
    for i in range(3): 
        if field[i][i] == elem_go: find_el+=1
    if find_el == 3: return True
# проверяем диагональ
    if field[2][0] == elem_go and field[1][1] == elem_go and field[0][2] == elem_go:
        return True

# вернуться позже,нужно не просто рандом, а умный ход, где уже есть макс.число эл-та бота, иначе если нет
# лучше закрывать ход соперника, а потом можно рандом из пустой строки, столбца
# 
# пробую функцию проверки свободных ячеек для рандомного хода бота - через кортежи - работает, но этого мало
# def ch_field(field):
#     _pos = [(index1,index2) for index1,value1 in enumerate(field) for index2,value2 in enumerate(value1) if value2=='_']
#     return _pos      


field = [['_' for j in range(3)] for i in range(3)]
print_field(field)


for i in range(9):
    elem_go = 'x' if i % 2 != 0 else '0'
    while True:
        pl = ch_input(
            f'Куда ходит {elem_go}?\n Укажите через запятую номер строки и столбца: ')
        if field[pl[0]-1][pl[1]-1] == '_':
            field[pl[0]-1][pl[1]-1] = elem_go
            print_field(field)
            break
        else:
            print('Поле занято, повторите ход')
            print_field(field)
    if i >= 2:
        if check_win(field, elem_go):
            print('Поздравляю с выигрышем!')
            break
        
