# задача 4. Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

def check_input(text_input):
    check_input = False
    while not check_input:
        try:
            number_input = int(input(text_input))
            check_input = True
        except:
            print('Некорректный ввод')
    return number_input

# сначала находим НОД по методу Евклида
def nod_evklid(a, b):
    while a*b !=0: 
        if a > b:
            a = a % b
        else:
            b = b % a 
    return (a + b)

# затем по формуле определяем НОК
def nok_ab(a1,b1):
    return int(a1*b1/nod_evklid(a1,b1))    

num_a =  check_input('a= ')   
num_b =  check_input('b= ')   
print('НОД:', nod_evklid(num_a, num_b))
print('НОК:', nok_ab(num_a, num_b))