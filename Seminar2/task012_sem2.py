# 12. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.

# *Пример:*

# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

def check_input(text_input):
    check_input = False
    while not check_input:
        try:
            number_input = int(input(text_input))
            check_input = True
        except:
            print('Некорректный ввод')
    return number_input     

def dictionary_for_n(num_n):
    dictionary_n = {}
    for i in range(1, num_n+1):
       dictionary_n[i] = 3*i+1
    return dictionary_n
                  

n = check_input('Введите n: ')   
n_slov =  dictionary_for_n(n)   
print(n_slov)