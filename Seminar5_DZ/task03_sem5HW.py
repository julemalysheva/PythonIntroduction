# задача 3. Напишите программу, удаляющую из текста все слова, содержащие "абв".

li_txt = input('Введите текст:').split()
li_txt = list(filter((lambda el : "абв" not in el ),li_txt))
new_text = " ".join(li_txt)
print(new_text)