# 16. Задайте список из n чисел последовательности (1 + 1/n)*n и выведите на экран их сумму.

def check_input(text_input):
    check_input = False
    while not check_input:
        try:
            number_input = int(input(text_input))
            check_input = True
        except:
            print('Некорректный ввод')
    return number_input


def sequence(num):
    return (1 + 1 / num) ** num #по условию возведение в степень или умножение


def set_list_sequence(n):
    list_sequence = []
    for i in range(1, n+1): #начинаем с 1, т.к. по условию и чтоб избежать /0
        list_sequence.append(sequence(i))  #а элементы в список заносим не 1 индекса, а с 0го
        # а здесь можно было не выносить выражение в отд.функцию sequence, а сразу добавить его в скобки и записать
    return list_sequence


def sum_list(list_s):
    sum_l = 0
    for item in list_s:
        sum_l += item
    return sum_l


num_n = check_input('Введите целое число: n = ')
list_sequence_n = set_list_sequence(num_n)
print(f'Список из {num_n} чисел: {list_sequence_n}')
print(f'Сумма элементов: {sum_list(list_sequence_n)}')

exit()
#  16. Решение из зала -  у меня примерно также, но создала отдельно ф-цию суммы, и здесь есть проверка main?

def sequence(n):
    return (1 + 1/n)**n

def feel_list(n):
    list = []
    for i in range(1, n+1):
        list.append(sequence(i))
    return list
# можно было воспользоваться встроенной функцией sum
def main():
    n = int(input("Enter n: "))
    list_sequence = feel_list(n)
    print(list_sequence)
    print("Sum of sequence: ", sum(list_sequence))

if __name__ == "__main__":
    main()
