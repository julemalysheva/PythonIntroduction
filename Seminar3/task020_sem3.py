# 20. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

# мое решение
def check_input(text_input):
    check_input = False
    while not check_input:
        try:
            number_input = int(input(text_input))
            check_input = True
        except:
            print('Некорректный ввод')
    return number_input

def input_list(len_list):
    list_str = []
    for _ in range(len_list):
        list_str.append(input('Введите строку: '))
    return list_str

def check_str_num(num, str_list):
    check_str = False
    str_num = str(num)
    for line in str_list:
        for char in line: #if n in list1[i]: здесь у ребят оптимальнее было условие
            if char == str_num:
                check_str = True
                break
    return check_str

len_list = check_input('Введите длину списка:')  
list_str = input_list(len_list) 
print(list_str)
num_find = check_input('Введите число для поиска: ') 
if check_str_num(num_find, list_str):
    print(f'Число {num_find} присутствует в списке')
else: print(f'Число {num_find} отсутствует в списке')   

exit()
# решения с семинара в зале:
def searchN(list1, n):
    global f
    for i in range(len(list1)):
        if n in list1[i]:
            f = 1
            break

try:
    n = int(input("Введите n: "))
except:
    print('Вводите числа!')
    exit()

f = 0
list1 = ['asd','qwwe','ddfgg','eeee','werwer3wewe34343w','4','233','wew']
searchN(list1,str(n))
if f == 1:
    print("есть")
else:
    print("нет")
