# задача 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# Входные и выходные данные хранятся в отдельных текстовых файлах.

def rle_code(txt):
    str_rle=''
    count_ch = 1
    i = 0
    while i < len(txt)-1:
        if txt[i] == txt[i+1]: count_ch+=1
        else: 
            str_rle+=str(count_ch)+txt[i]
            count_ch = 1
        i+=1
    str_rle+=str(count_ch)+txt[len(txt)-1]   
    return str_rle      

def rle_decode(txt):
    cnt = ''
    str_txt = ''
    for ch in txt:
        if ch.isdigit():
            cnt+=ch
        else:
            str_txt+=ch*int(cnt)  
            cnt = ''
    print(str_txt)
    return str_txt

try:
    with open('input.txt', 'r') as fp:
        line = fp.read()
except:
    line = "dddddddddddddddddllkkdfgggggggggggggpoffff"

print(rle_code(line))   

try:
    with open('rle.txt', 'w') as fp:
        fp.write(rle_code(line))
except:
    print("Что-то пошло не так)")

# восстановление данных
try:
    with open('rle.txt', 'r') as fp:
        line_rle = fp.read()
except:
    line_rle = '17d2l2k1d1f13g1p1o4f1'

print(line_rle)
rle_decode(line_rle)

