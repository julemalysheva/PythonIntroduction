from random import *


def new_field():
    field = [['_' for j in range(3)] for i in range(3)]
    return field


def print_field(field):
    text = ''
    for i in range(len(field)):
        text += '\n'+' | '.join(field[i])
        # print(' | '.join(field[i]))
    return text

# определяем игрока и чем ходит


def set_players(human):
    hod = choice([True, False])  # определили рандомно 1го игрока
    # буду считать по ходу программы, что True - это бот, False - человек
    dic = {}
    dic[hod] = ['x']  # и добавили это значение в словарь
    dic[not hod] = ['0']
    if hod == True:
        dic[hod].append('bot')
        dic[not hod].append(human)
    else:
        dic[hod].append(human)
        dic[not hod].append('bot')

    print(dic)
    return (dic, dic[hod][1], hod)

# как-то нужно возвращать ошибку, может проверять если тип не список - то возвращать в pos строку уведомления
# наверное, придется эту проверку делать в мейн


def ch_input(text):
    # check_input = False
    # while not check_input:
    # убираем команду, остается 0й один элемент после разделителя пробела- это как раз строка с номером строки/столбца 
    # через запятую
    text = text.split()[1:]
    try:
        pos = list(map(int, text))
        # check_input = True
        if pos[0] > 3 or pos[1] > 3 or pos[0] < 1 or pos[1] < 1:
            pos = 'Значения могут быть только от 1 до 3\nПовторите команду'
            print('Значения могут быть только от 1 до 3')
            # check_input = False
    except:
        pos = 'Некорректный ввод, повторите команду'
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
def ch_field(field):
    _pos = [(index1,index2) for index1,value1 in enumerate(field) for index2,value2 in enumerate(value1) if value2=='_']
    print(_pos)
    pl = choice(_pos)
    return pl      
