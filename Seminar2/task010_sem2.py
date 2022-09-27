# 10. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние
# между ними в 2D пространстве.

# *Пример:*

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21


# import math


def check_input(text_input):
    check_input = False
    while not check_input:
        try:
            number_input = float(input(text_input))
            check_input = True
        except:
            print('Некорректный ввод')
    return number_input            


def distance_between_points(x1, y1, x2, y2):
    # distance_points = math.sqrt((x2-x1)**2+(y2-y1)**2)
    distance_points = ((x2-x1)**2+(y2-y1)**2)**0.5
    return round(distance_points, 2)

print('Введите координаты точки A:')
x_a = check_input('x1 = ')   
y_a = check_input('y1 = ')  
print('Введите координаты точки B:')
x_b = check_input('x2 = ')   
y_b = check_input('y2 = ')  
print(f'Расстояние между точками = {distance_between_points(x_a, y_a, x_b, y_b )}')

