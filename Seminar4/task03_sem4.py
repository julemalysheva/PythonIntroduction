# 29. Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

# a = int(input("Введите число a "))
# b = int(input("Введите число b "))
# i = max(a, b)
# while True:
#     if i%a==0 and i%b==0:
#         break
#     i += 1
# print(i)

# можно сначала найти наибольший общий делитель, и потом по формуле НОК


def check_input(text_input):
    check_input = False
    while not check_input:
        try:
            number_input = int(input(text_input))
            check_input = True
        except:
            print('Некорректный ввод')
    return number_input


def nod_evklid(a, b):
    while a*b !=0: 
        if a > b:
            a = a % b
        else:
            b = b % a 
    return (a + b)

def nok_ab(a1,b1):
    return int(a1*b1/nod_evklid(a1,b1))    

num_a =  check_input('a= ')   
num_b =  check_input('b= ')   
print('НОД:', nod_evklid(num_a, num_b))
print('НОК:', nok_ab(num_a, num_b))
