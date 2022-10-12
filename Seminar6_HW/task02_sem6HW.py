# Задача 2. Напишите программу вычисления арифметического выражения заданного строкой. 
# Используйте операции +,-,/,*. приоритет операций стандартный.

# *Пример:* 
# 2+2 => 4; 
# 1+2*3 => 7; 
# 1-2*3 => -5;
# - Добавьте возможность использования скобок, меняющих приоритет операций.
#     *Пример:* 
#     1+2*3 => 7; 
#     (1+2)*3 => 9;

# работают в т.ч. вложенные скобки, но есть вопрос по синтаксису.
# внутри функции step передаю срез списка из скобок, поэтому ф-цию пришлось
# создать с параметрами. При этом нужно, чтоб список менялся глобально, поэтому
# в calc() прописала global li_ch - это решило проблему ошибок поиска,
# все считается отлично, но при след.старте выдает предупреждение синтаксиса
# https://skr.sh/sGNn8j2Y8Am

li_ch = []

def operation(math_operation,x,y):
        if math_operation == "+":
            return x+y
        elif math_operation == "-":
            return x-y
        elif math_operation == "/":
            return x/y
        elif math_operation == "*":
            return x*y

def calc(znak, li_ch): 
    global li_ch
    res_i = li_ch.index(znak)
    # print("индекс знака операции = ", res_i)
    res = operation(znak, li_ch[res_i-1], li_ch[res_i+1]) 
    # удаляем элементы и знак
    li_ch.pop(res_i+1) #идет смещение, поэтому делаем это от большего к меньшему 
    li_ch.pop(res_i) 
    li_ch.pop(res_i-1)                        
    li_ch.insert(res_i-1,res) #на его место помещаем результат


str_i = input('Введите строку: ').strip()
print(str_i)
# собираем элементы в список
# подумать как обработать знак "-" перед числом
num = ''
minus = False
for ch in str_i:

    if ch.isdigit():
        num+=ch
    else: 
        if len(num)>0 and num.isdigit(): li_ch.append(int(num))
        li_ch.append(ch)
        num = ''
        # добавляем крайний элемент - число, при условиях выше он его собирает, но не добавляет,т.к. закончилась строка
if len(num)>0 and num.isdigit(): li_ch.append(int(num))        
#убираем пробелы 
li_ch = list(filter((lambda el : el!=" " ),li_ch))
print(li_ch)

# пришлось передавать список в параметры,т.к. внутри передаю срез при наличии скобок
def step(li_ch):
    while len(li_ch) > 1:
        while "(" in li_ch: #или вообще просто тупо здесь все прописать, но тогда и вложенные придется здесь писать?
            # здесь находим крайнее вхождение откр.скобки "(""
            r_index = (len(li_ch) -1) - list(reversed(li_ch)).index("(")
            print("индекс ( = ", r_index)
            # пробуем найти первый индекс закрытой скобки ")"
            try:
                ind = li_ch.index(")")
                print("индекс ) = ", ind)
            except:
                print('Выражение задано неверно')  
            #сначала удаляем скобки и со смещением индексов передаем в ф-цию срез,иначе они снова будут найдены 
            li_ch.pop(r_index)  
            li_ch.pop(ind)  
            step(li_ch[r_index:ind-1])

# добавила список в аргументы,т.к. передаю срез и не получалось с ним
        while "/" in li_ch:
            calc("/", li_ch)
        while "*" in li_ch:
            calc("*", li_ch)    
        while "+" in li_ch:
            calc("+", li_ch)  
        while "-" in li_ch:
            calc("-", li_ch)     

    # print(f'{str_i} = {li_ch[0]}')
             

step(li_ch)
print(li_ch[0])


