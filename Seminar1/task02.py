# 2. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.

#     *Примеры:*

#     - 6,78 -> 7
#     - 5 -> нет
#     - 0,34 -> 3

a = float(input("Введите дробь: "))
if a % 1 != 0:
    b = a * 10
    print(int(b % 10)) 
else:
    print("нет")


print("пишем код в функцию")

def des_fraction(x):
    if a % 1 != 0:
     b = a * 10
     return int(b % 10)
    else:
     return "нет"

n = float(input('Ввести дробь: '))
print(des_fraction(n))