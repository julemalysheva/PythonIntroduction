# 21. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.

# *Пример:*

# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1

# мое решение:
def seach_index(find_str, list_str):
    index_seach = -1
    count_find = 0
    for i in range(len(list_str)):
        if list_str[i] == find_str:
            count_find+=1
        if count_find == 2:
            index_seach = i
            break
    return index_seach

str_find = (input('Строка для поиска: '))            
list_str = ["123", "234", 123, "567"]    
print(seach_index(str_find, list_str))

# решение с семинара из зала:
list1 = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
search = input("Enter: ")

def find_second(list1, search):
    result = -1
    count = 0
    for i in range(len(list1)):
        if list1[i] == search:
            count += 1
            if count == 2:
                result = i
    return result

print(find_second(list1, search))
