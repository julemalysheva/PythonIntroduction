# Задача 5 НЕОБЯЗАТЕЛЬНАЯ. Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат. Количество предикатов генерируется
# случайным образом от 5 до 11, проверяем это утверждение 10 раз, с помощью модуля time выводим на экран ,
# сколько времени отработала программа.

# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z

from random import randint
from datetime import datetime
import time
# пробую выводить по разному
start = time.time()
start_time = datetime.now()

def truth_check():
    result = 0
    for n in range(0, 10): #проверяем это утверждение 10 раз
        #Количество предикатов генерируется случайным образом от 5 до 11
        count_var = randint(5, 11) 
        first_bool = bool(randint(0,1))
        left_part, right_part = first_bool, first_bool
        print(f'{n+1}я Итерация для {count_var} переменных:')
        print(f'Первое присвоение {n+1}й итерации - лево-право: {left_part}, {right_part}')

        for i in range(count_var-1): #-1,т.к. две переменные уже в выражении, значение 1й рандомно присвоено выше
            next_var = bool(randint(0,1))
            left_part = not (left_part or next_var)
            right_part = (not right_part) and (not next_var)
            print(f'Итерация с {i+2}й переменной: левая часть {left_part}, правая часть {right_part}')
        if left_part == right_part:
            result += 1
        print(f'По итогу {n+1}й итерации - левая: {left_part}, правая {right_part}, утверждение: {left_part == right_part}, результат: {result}')  
        print()
    if result == 10:
        return True
    else:
        return False  

print(f'Утверждение {truth_check()}')   

print(f'Начали {start_time}')
end_time = datetime.now()
print(f'Окончили {end_time}')   
print('Длительность: {}'.format(end_time - start_time))

print()
finish = time.time()
result = finish - start
print("Program time: " + str(result) + " seconds.")

        
