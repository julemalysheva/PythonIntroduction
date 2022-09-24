# 3. Напишите программу, которая принимает на вход число и проверяет,
# кратно ли оно 5 и 10 или 15, но не 30.

def check_num(number):
    divisible = False
    if ((number % 5 == 0 and number % 10 == 0) or number % 15 == 0) and number % 30 != 0:
        divisible = True
    return divisible


try:
    num = int(input("Введите число для проверки кратности: "))
    if check_num(num):
        print('Да')
    else:
        print('Нет')
except:
    print("некорректный ввод ") 


print('Решение с семинара: ')
try:
    a = int(input("Введите число: "))

    if( a % 5 == 0 and a % 10 == 0 or a % 15 == 0) and a % 30 != 0:
        print("Кратно")
    else:
        print("не кратно")
except:
    print("некорректный ввод ")