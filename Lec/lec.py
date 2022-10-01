a = float(input('a = '))
c = 0
sum = 0
while a!=int(a):
    a *= 10
b = a
while b != 0:
    sum += b%10
    b = b//10
print(int(sum))

exit()

#print('Введите a')
#a = int(input('Введите a: '))
#print('Введите b')
#b = int(input('Введите b: '))
#print(a, b)
#c = a+b
#print(a, '+', b, '=', c)
#print('{} + {} = {}'.format(a, b, c))

# exp1 = 2**3 - 10 % 5 + 2*3
# exp2 = 2**3 - 10 / 5 + 2*3
# print(exp1)  # 14.0 или 14
# print(exp2)  # 12.0 или 12

# a, b, c = 1, 2, 3  # вариант записи переменных
# # a: 1 b: 2 c: 3
# print('a: {} b: {} c: {}'.format(a, b, c))
# range(*(1, 5, 2))

# username = input('Введите имя: ')
# if(username == 'Маша'):
#  print('Ура, это же МАША!');
# else:
#  print('Привет, ', username);

# username = input('Введите имя: ')
# if username == 'Маша':
#  print('Ура, это же МАША!')
# elif username == 'Марина':
#  print('Я так ждала Вас, Марина!')
# elif username == 'Ильнар':
#  print('Ильнар - топ)')
# else:
#  print('Привет, ', username)

# original = 458
# inverted = 0
# while original != 0:
#  inverted = inverted * 10 + (original % 10)
#  original //= 10
# print(inverted)

# original = 23
# inverted = 0
# while original != 0:
#  inverted = inverted * 10 + (original % 10)
#  original //= 10
# else:
#  print('Пожалуй')
#  print('хватит )')
# print(inverted)
# Пожалуй
# хватит )
# 32

# for i in 1, -2, 3, 14, 5:
#  print(i)

# r = range(100, 0, -20) # range(100, 0, -20)
# for i in r:
#  print(i)
# # 100 80 60 40 20
# for i in range(5):
#  print(i) #как выводить в одну строку, а не в отдельную с каждой итерацией?
# # 0 1 2 3 4

# line = ""
# for i in range(5):
#     line = ""
#     for j in range(5):
#      line += "*"
# print(line)

# Немного о строках
# text = 'съешь ещё этих мягких французских булок'
# print(len(text))  # 39
# print('ещё' in text)  # True
# print(text.isdigit())  # False
# print(text.islower())  # True
# print(text.replace('ещё', 'ЕЩЁ'))
# for c in text:
#     print(c)

# text = 'съешь ещё этих мягких французских булок'
# print(text[0]) # c
# print(text[1]) # ъ
# print(text[len(text)-1]) # к
# print(text[-5]) # б
# print(text[:]) # print(text)
# print(text[:2]) # съ
# print(text[len(text)-2:]) # ок
# print(text[2:9]) # ешь ещё
# print(text[6:-18]) # ещё этих мягких
# print(text[0:len(text):6]) # сеикакл
# print(text[::6]) # сеикакл
# text = text[2:9] + text[-5] + text[:2] # ...    
# print(text)

# numbers = [1, 2, 3, 4, 5]
# print(numbers) # [1, 2, 3, 4, 5]
# numbers = list(range(1, 6))
# print(numbers) # [1, 2, 3, 4, 5]
# numbers[0] = 10
# print(numbers) # [10, 2, 3, 4, 5]
# for i in numbers:
#  i *= 2
#  print(i) # [20, 4, 6, 8, 10]
# print(numbers) # [10, 2, 3, 4, 5]

# colors = ['red', 'green', 'blue']
# for e in colors:
#  print(e) # red green blue
# for e in colors:
#  print(e*2) # redred greengreen blueblue
# colors.append('gray') # добавить в конец
# print(colors == ['red', 'green', 'blue', 'gray']) # True
# colors.remove('red') #del colors[0] # удалить элемент
# print(colors)

# Функции
# def f(x):
#  return x**2
def f(x):
 if x == 1:
  return 'Целое'
 elif x == 2.3:
  return 23
 else:
  return
print(f(1)) # Целое
print(f(2.3)) # 23
print(f(28)) # None
print(type(f(1))) # str
print(type(f(2.3))) # int
print(type(f(28))) # NoneType