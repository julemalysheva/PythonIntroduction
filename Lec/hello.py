
'''
Lambda – для создания небольших маленьких функций
Map – применяет функцию к списку или словарю, возвращает измененный объект
Filter - применяет логическую функцию к списку или словарю, возвращает элементы, 
которые удовлетворяют условию
Zip – создает кортежи из элементов словарей или списков
List comprehension  - удобная генерация списков	
'''

add = lambda x, y : x + y   #тут что-то поменяли
  
print(add(2, 3) ) # Результат: 5

def multiply2(x):
  return x * 2
    
print(list(map(multiply2, [1, 2, 3, 4])) )  # Вернет [2, 4, 6, 8]

dict_a = [{'name': 'python', 'points': 10}, {'name': 'java', 'points': 8}]

res = list(filter(lambda x : x['name'] == 'python', dict_a)) # Вернет: [{'name': 'python', 'points': 10}]

print(res)

a = [10, 20, 30, 40]
b = ['a', 'b', 'c', 'd', 'e']
for i, j in zip(a, b):
    print(i, j)

spisok = [16, 46, 26, 36]
for i in enumerate(spisok):
    print(i)


squares = [x ** 2 for x in range(10)]

odds = [x for x in range(10) if x % 2 != 0]

print(squares)

print(odds)