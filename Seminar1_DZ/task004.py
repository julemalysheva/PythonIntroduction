# задача 4 HARD необязательная Напишите простой калькулятор, который считывает с пользовательского
# ввода три строки: первое число, второе число и операцию, после чего применяет операцию
# к введённым числам ("первое число" "операция" "второе число") и выводит результат на экран.

# Поддерживаемые операции: +, -, /, *, mod, pow, div, где
# mod — это взятие остатка от деления,
# pow — возведение в степень,
# div — целочисленное деление.

# Если выполняется деление и второе число равно 0, необходимо выводить строку "Деление на 0!".

# Обратите внимание, что на вход программе приходят вещественные числа.

def sum(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Деление на 0!"


def multiply(a, b):
    return a * b


def mod(a, b):
    return a % b


def pow(a, b):
    return a ** b


def div(a, b):
    return a // b #нужно ли переводить в int?


def input_num(str_input):
    ch_num = False
    while not ch_num:
        try:
            num_input = float(input(str_input))
            ch_num = True
        except:
            print('Некорректный ввод, введите число')
    return num_input


def input_operation(text_input):
    check_oper = False
    while not check_oper:
        math_operation = input(text_input)
        if math_operation == "+":
            return sum
        elif math_operation == "-":
            return subtraction
        elif math_operation == "/":
            return division
        elif math_operation == "*":
            return multiply
        elif math_operation == "mod":
            return mod
        elif math_operation == "pow":
            return pow
        elif math_operation == "div":
            return div
        else:
            check_oper = False

first_num = input_num('Введите первое число: ')
second_num = input_num('Введите второе число: ')
operation = input_operation('Введите операцию из предложенных: +, -, /, *, mod, pow, div: ')
print(f'Ответ: {operation(first_num, second_num)}') #при необходимости добавить округление
