# with open('file.txt', 'w') as data: # в data передаем файл с параметром, в этой конструкции закрывается он автоматически
#     data.write('line 333\n')

# colors = ['red', 'green333', 'blue123']
# data = open('file.txt', 'a') #a -режим дописывать в файл, если нет - будет создан. w - режим перезаписи
# # data.writelines(colors) # разделителей не будет
# data.write('line 12\n') #дописывать, \n это переход на нов. строку
# data.write('line 23\n')

# data.close() #нужно закрывать, чтоб не был занят приложением и не грузил память

# exit() #для того, чтоб не выполнялся последующий код
# чтение из файла
path = 'file.txt' #пусть
data = open(path, 'r') #если файла не будет - ошибка
for line in data:
 print(line)
data.close()

import lec as lc #импорт файла как псевдоним lc
# далее можно использовать функции того файла, например
print(lc.f(1))

def new_string(symbol, count):
 return symbol * count
print(new_string('!', 5)) # !!!!!
# print(new_string('!')) # TypeError missing 1 required ...тк нет аргумента
# мы можем назначить значение по умолчанию, как
def new_string(symbol, count = 3):
 return symbol * count
print(new_string('!', 5)) # !!!!!
print(new_string('!')) # !!!
print(new_string(4)) # 12 пайтон определяет тип во время вызова, число будет умножено, строка увеличена

def concatenatio(*params): # * дает набор аргументов - любое количество можно передавать
 res: int = 0             # переменная: тип данных - можно указать явно, указание типа не обязательно
 for item in params:
  res += item
 return res
# print(concatenatio('a', 's', 'd', 'w')) # asdw
# print(concatenatio('a', '1', 'd', '2')) # a1d2
print(concatenatio(1, 2, 3, 4)) # TypeError: ...если в функции явно указан тип Стринг

def fib(n):
 if n in [1, 2]:
  return 1
 else:
  return fib(n-1) + fib(n-2)
list = []
for e in range(1, 10):
 list.append(fib(e))
print(list) # 1 1 2 3 5 8 13 21 34


t = ()
print(type(t)) # tuple
t = (1,)
print(type(t)) # tuple
t = (1)
print(type(t)) # int
t = (28, 9, 1990)
print(type(t)) # tuple
colors = ['red', 'green', 'blue']
print(colors) # ['red', 'green', 'blue']
t = tuple(colors) #превратили список в кортеж
print(t) # ('red', 'green', 'blue')

t = tuple(['red', 'green', 'blue'])
print(t[0]) # red - можно обращаться по индексам
print(t[2]) # blue
# print(t[10]) # IndexError: tuple index out of range
print(t[-2]) # green или сзади наперед
# print(t[-200]) # IndexError: tuple index out of range
for e in t:
 print(e) # red green blue  - перебирать через цикл
# t[0] = 'black' # TypeError: 'tuple' object does not support item assignment
# т.е. нельзя назначать значения

t = tuple(['red', 'green', 'blue']) #список конвертировали в кортеж
red, green, blue = t #далее из кортежа передаем данные в три независимые переменные
print('r:{} g:{} b:{}'.format(red, green, blue))
# r:red g:green b:blue

# Словари - Неупорядоченные коллекции произвольных объектов с доступом по ключу
dictionary = {}
dictionary = \
 {
 'up': '↑',
 'left': '←',
 'down': '↓',
 'right': '→'
 }
print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
print(dictionary['left']) # ←
# типы ключей могут отличаться
# можем присваивать значения также через ключ
# печатаем ключи
for k in dictionary.keys():
    print(k)
    # печатаем только значения
for k in dictionary.values():
    print(k)
    # по всем элементам
#print(dictionary['type']) # KeyError: 'type'
del dictionary['left'] # удаление элемента
for item in dictionary: # for (k,v) in dictionary.items():
 print('{}: {}'.format(item, dictionary[item]))
# up: ↑
# down: ↓
# right: →
for (k,v) in dictionary.items():
    print(k, v)
# up: ↑
# down: ↓
# right: →    

# Множества
a = {1, 2, 3, 5, 8}
b = set([2, 5, 8, 13, 21])
c = set((2, 5, 8, 13, 21))
print(type(a)) # set
print(type(b)) # set
print(type(c)) # set
a = {1, 1, 1, 1, 1}
print(a) # {1}
colors = {'red', 'green', 'blue'}
print(colors) # {'red', 'green', 'blue'}
colors.add('red')
print(colors) # {'red', 'green', 'blue'}
colors.add('gray')
print(colors) # {'red', 'green', 'blue','gray'}
colors.remove('red')
print(colors) # {'green', 'blue','gray'}
# colors.remove('red') # KeyError: 'red'
colors.discard('red') # ok
print(colors) # {'green', 'blue','gray'}
colors.clear() # { }
print(colors) # set()
a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy() # c = {1, 2, 3, 5, 8}
# работа с множествами
u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21}
i = a.intersection(b) # i = {8, 2, 5}
dl = a.difference(b) # dl = {1, 3}
dr = b.difference(a) # dr = {13, 21}
q = a \
 .union(b) \
 .difference(a.intersection(b))
# {1, 21, 3, 13}
# Неизменяемое множество
a = {1, 2, 3, 5, 8}
b = frozenset(a)
print(b) # frozenset({1, 2, 3, 5, 8})

