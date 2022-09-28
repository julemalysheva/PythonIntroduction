# Задача 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# *Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def check_input(text_input):
    check_input = False
    while not check_input:
        try:
            number_input = int(input(text_input))
            check_input = True
        except:
            print('Некорректный ввод')
    return number_input

def fac(n):
    factorial = 1
 
    for i in range(2, n+1):
     factorial *= i
 
    return factorial

def multiplication_list(num_n):
    list_multiply = []
    for item in range(1, num_n + 1):
        fac_item = fac(item)
        list_multiply.append(fac_item)

    return list_multiply   

number_input = check_input('Введите N: ')
print(f'Набор произведений чисел от 1 до {number_input}:')
print(multiplication_list(number_input))

