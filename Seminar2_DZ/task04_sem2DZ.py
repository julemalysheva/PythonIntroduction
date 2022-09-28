# Задача 4 НЕОБЯЗАТЕЛЬНАЯ. Напишите программу, которая принимает на вход N, 
# и координаты двух точек и находит расстояние между ними в N-мерном пространстве.

def check_input(text_input):
    check_input = False
    while not check_input:
        try:
            number_input = float(input(text_input))
            check_input = True
        except:
            print('Некорректный ввод')
    return number_input            

    
def distance_between_points(x,y,n):
    sum_sqrt=0
    for i in range(n):
        sum_sqrt+= (y[i]-x[i])**2
    distance_points = sum_sqrt**0.5
    return round(distance_points, 2)

n = int(check_input('Введите N: '))
list_x = []
list_y = []
for i in range(n):
    print('Введите координаты точки:')
    x = check_input(f'Введите a{i+1}: ')
    list_x.append(x)
    y = check_input(f'Введите b{i+1}: ')
    list_y.append(y)

print(f'Расстояние между точками в {n}-мерном пространстве = {distance_between_points(list_x, list_y, n)}')
