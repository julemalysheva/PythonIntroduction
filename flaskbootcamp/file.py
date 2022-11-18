# этот файл просто какой-то промежуточный, получали здесь данные из файла
file = open('flaskbootcamp/file.txt', 'r',encoding='utf-8')
list1 = list()

result_data = []
for line in file.readlines():
    # print(line.split('\n')[0].split(';'))
    result_data.append(tuple(line.split('\n')[0].split(';')))
    
print(result_data)

file.close()

# то, что ниже, это код со 2 семинара, удалила из main на 3м, здесь сохраняю на всякий случай
# from flask import Flask, render_template


# app = Flask(__name__)

# @app.route('/')
# def main():
#     with open('flaskbootcamp/file.txt', 'r', encoding='utf-8') as file:
#         resultData = list()
#         for line in file.readlines():
#             resultData.append(tuple(line.split('\n')[0].split(';')))

#     return render_template('base.html', data=resultData)

# # render_templat
# # возвращает html код из указанного файла из папки templat
# @app.route('/about')
# def about():
#     return render_template('about.html')


# if __name__ == '__main__':
#     app.run()

# а это было в base.html
# <!-- указываем условие -->
# {% if data %}
# <!-- заполняем таблицу -->
#     <table>
#         <tr><th>Имя</th><th>Фамилия</th><th>Дата рождения</th></tr>
#         {% for row in data %}
#             <tr><td>{{ row[0] }}</td><td>{{ row[1] }}</td><td>{{ row[2] }}</td></tr>
#         {% endfor %} 
#         <!-- конец цикла -->
#     </table>
# {% endif %}
# <!-- конец условия -->