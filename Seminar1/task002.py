# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

#     Примеры:

#     - 1, 4, 8, 7, 5 -> 8
#     - 78, 55, 36, 90, 2 -> 90

def getArr(arr_len):
    listNumber = []
    for _ in range(arr_len):
        number = int(input("введите число: "))
        listNumber.append(number)
    return listNumber


def maxArray(arr):
    maxNumber = arr[0]
    for num in arr:
        if num > maxNumber:
            maxNumber = num
    return maxNumber

list_number = getArr(5)
print('Задан массив чисел: ', list_number)
print('Максимальное число = ', maxArray(list_number))

