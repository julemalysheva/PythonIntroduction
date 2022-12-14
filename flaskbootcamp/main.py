from flask import Flask, render_template
from LoginForm import Lf
from AuthForm import AuthF


app = Flask(__name__)
# csrf- атаки, имеется втсроенная возможность предотвращения этих атак во flask
# нужно прописать:
app.config['SECRET_KEY'] = 'hello hello hello hello hello world'



@app.route('/')
def main():
    return render_template('base.html')


@app.route('/register', methods=['GET', 'POST'])
def reg():
    form = Lf()
    if form.validate_on_submit():
        # таким образом можно достучаться и получить введенные данные
        # print(form.name.data, form.password.data)
        if form.password_again.data != form.password.data:
            return render_template('register.html', title='Регистрация', form=form,
            message = 'Пароли не совпадают!!!')
        # записываем данные в файл вместо базы данных
        with open('flaskbootcamp/file.txt', 'a', encoding='utf-8') as file:
            file.write(f'{form.name.data};{form.email.data};{form.password.data}\n')
        return render_template('register.html', message='Регистрация прошла успешно')

    return render_template('register.html', title='Регистрация', form=form)

@app.route('/log', methods=['GET', 'POST'])
def log():
    form = AuthF()
    if form.validate_on_submit():
        with open('flaskbootcamp/file.txt', 'r', encoding='utf-8') as file:
            data = ' '.join(file.readlines())
        
        if form.email.data not in data:
            return render_template('login.html', form=form, message='Вы не зарегистрированы')
        else:
            for i in data.split():
                if form.email.data in i:
                    if i.split(';')[-1] == form.password.data:
                        return render_template('login.html', message='Вы успешно авторизовались')
                    else:
                        return render_template('login.html', message='Неверный пароль')

    return render_template('login.html', form = form)    

if __name__ == '__main__':
    app.run()
