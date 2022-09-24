# задача 2. Напишите программу для проверки истинности
# утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


def check_exp():
    check_true = True
    for x in range(2):
        x = bool(x)
        for y in range(2):
            y = bool(y)
            for z in range(2):
                z = bool(z)
                print(f'Для значений предикат: x = {x}, y = {y}, z = {z}')
                print(
                    f'Утверждение {not (x or y or z) == (not x and not y and not z)}')
                if not (x or y or z) != (not x and not y and not z):
                    check_true = False
                    break

check_exp() # вывожу информацию для себя для проверки значений
if check_exp:
    print('Утверждение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z истинно для всех значений предикат')
else:
    print('Утверждение не является истинным для всех значений предикат')

    
