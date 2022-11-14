from flask import Flask, render_template
from random import randint as rd


app = Flask(__name__)

@app.route('/')
def main():
    name = rd(0, 1)
    return render_template('base.html', name=name)


if __name__ == '__main__':
    app.run()
