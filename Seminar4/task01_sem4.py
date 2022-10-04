# 26. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
    
#     *Пример:*
    
#     - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

# еще один вариант решения
# n = int(input('Введите число: '))

# def get_fibonacci(n):
#     fibo_nums = []
#     a, b = 1, 1
#     for i in range(n-1):
#         fibo_nums.append(a)
#         a, b = b, a + b
#     # print(fibo_nums)

#     a, b = 0, 1
#     for i in range (n):
#         fibo_nums.insert(0, a)
#         a, b = b, a - b
#     # print(fibo_nums)
#     return fibo_nums


# fibo_nums = get_fibonacci(n)
# print(get_fibonacci(n))
# print(fibo_nums.index(0))
# exit()

# n = int(input("Введите количество элементов: "))
# list = [None for _ in range(n*2 + 1)]

# def fib(k):
#     if k in [1, 2]:
#         return 1
#     else:
#         return fib (k-1) + fib (k-2)

# list[n] = 0

# for e in range(1, n+1):
#     list[n+e] = fib(e)
#     if e % 2 == 0:
#         list[n-e] = - fib(e)
#     else:
#         list[n-e] = fib(e)
# print(list)

# exit()

def check_input(text_input):
    check_input = False
    while not check_input:
        try:
            number_input = int(input(text_input))
            check_input = True
        except:
            print('Некорректный ввод')
    return number_input


def fib(n):
 if n in [1, 2]:
  return 1
 else:
  return fib(n-1) + fib(n-2)

num = check_input('Введите число k:')
list1 = []
list1.append(0)
for e in range(1, num+1):
 list1.append(fib(e)) #заполняем правую сторону
 if e % 2 == 0:
    list1.insert(0, -fib(e)) #заполняем левую сторону
 else: list1.insert(0, fib(e))    
print(list1) # [-21, 13, -8, 5, -3, 2, -1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

exit()
list2=[]
for el in range(0,num):
    if el%2!=0:
        list2.append(-list1[el+1])
    else: 
        list2.append(list1[el+1])
print(list2) #[1, -1, 2, -3, 5, -8, 13, -21]

list2= list2[::-1] #развернули список
print(list2) #[1, -1, 2, -3, 5, -8, 13, -21]
list3 = list()
list3=list2+list1
print(list3)

 



