file = open('flaskbootcamp/file.txt', 'r',encoding='utf-8')
list1 = list()

result_data = []
for line in file.readlines():
    # print(line.split('\n')[0].split(';'))
    result_data.append(tuple(line.split('\n')[0].split(';')))
    
print(result_data)

file.close()