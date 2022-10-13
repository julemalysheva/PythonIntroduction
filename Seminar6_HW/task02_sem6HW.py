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

li_ch = []
i = 0 #отвечает за диапазон смещения, когда смотрю срез в ()

def operation(math_operation,x,y):
        if math_operation == "+":
            return x+y
        elif math_operation == "-":
            return x-y
        elif math_operation == "/":
            return x/y
        elif math_operation == "*":
            return x*y

# для среза скобок пробую добавить старт и финиш, по умолчанию (вне скобок) - 0 и конец массива,
# но похоже я не разобралась со значениями по умолчанию в функции и ловила ошибки вне списка.
# пришлось ниже везде вызывать ее с передачей аргументов
def calc(znak,start=0,end=len(li_ch),r_ind=0): 
    global li_ch, i
    # при поиске индекса в срезе начинает брать индексы не с нужного, а с 0.
    # поэтому передаю сюда этот отступ r_ind для правильного позиционирования, по умолчанию он равен 0
    res_i = li_ch[start:end].index(znak) + r_ind
    print("индекс знака операции = ", res_i)
    res = operation(znak, li_ch[res_i-1], li_ch[res_i+1]) 
    # удаляем элементы и знак
    li_ch.pop(res_i+1) #идет смещение, поэтому делаем это от большего к меньшему 
    li_ch.pop(res_i) 
    li_ch.pop(res_i-1)                        
    li_ch.insert(res_i-1,res) #на его место помещаем результат
    print('Список после операции', li_ch)
    i += 2 #3 удалили,1добавили - диапазон для среза уменьшаем на 2
    print('уменьшаем верхний диапазон от первоначального на ',i)
    # return i


str_i = input('Введите строку: ').strip()
print(str_i)
# собираем элементы в список
num = ''
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

# обработать знак "-" почти работает))
# убрала пока, в варианте -49-45*(2+4*-3)+8/2 берет -45 числом а не знаком и числом
# хотя вроде под условие не попадает https://skr.sh/sGNLjjL6ZZZ
# size = len(li_ch)
# j = 3
# while j<size:
#     if isinstance(li_ch[j], int) and li_ch[j-1] == '-':
#         if (not isinstance(li_ch[j-2], int)) or  (li_ch[j-2] != ')') :
#             li_ch[j] = - li_ch[j]
#             li_ch.pop(j-1)
#             size-=1 #размер при удалении уменьшается
#             j-=1 #индексы смещяются - пробую быть в ранге, если удалили
#     j+=1 #здесь переключаем счетчик        
# # здесь минус перед первым числом в начале строки после всех преобразований
# if li_ch[0] == "-" and isinstance(li_ch[1], int):
#     li_ch[1]=-li_ch[1]
#     li_ch.pop(0)

# print(li_ch)

while len(li_ch) > 1:
    i = 0 #здесь он нужен только в срезах в скобках, но на всякий очищаю каждый раз
    while "(" in li_ch: 
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
        li_ch.pop(ind-1)  #-1 т.к. при удалении ( скобки прошло смещение
        print("удалили скобки", li_ch)
        #сдвигаю диапазон вниз после удаления элементов на - i
        i = 0
        while "/" in li_ch[r_index:ind-1-i]: #диапазон смещается при удалении, поэтому - i
            calc("/",r_index, ind-1-i,r_index)
        while "*" in li_ch[r_index:ind-1-i]:
            calc("*",r_index, ind-1-i,r_index)    
        while "+" in li_ch[r_index:ind-1-i]:
            calc("+",r_index, ind-1-i,r_index)  
        while "-" in li_ch[r_index:ind-1-i]:
            calc("-",r_index, ind-1-i,r_index)    
        
            # step(li_ch[r_index:ind-1]) это заменила на код - ошибки области видимости, хотя считались вложенные скобки
    # while len(li_ch) > 1:

    # выполняем действия по порядку
    print('Выполняем действия по порядку вне скобок')
    # дальше выдавал ошибки без параметров, по умолчанию не сработало - так норм
    while "/" in li_ch:
        calc("/",0,len(li_ch),0)
    while "*" in li_ch:
        calc("*",0,len(li_ch),0)    
    while "+" in li_ch:
        calc("+",0,len(li_ch),0)  
    while "-" in li_ch:
        calc("-",0,len(li_ch),0)     

             

# print(li_ch[0])
print(f'{str_i} = {li_ch[0]}')


