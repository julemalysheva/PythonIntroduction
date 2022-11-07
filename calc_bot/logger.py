from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from datetime import datetime as dt

# context посмотреть позже, если он нигде не нужен будет - удалить из аргументов и параметров везде
# title описание события - передается при вызове
def log(update: Update, context: CallbackContext, title):
        # проверить, как и что записывать в лог еще - дату и время как минимум
    time = dt.now().strftime('%H:%M')
    with open('calc_bot/calc_bot.txt', 'a',encoding="utf8") as file: 
        file.write(f'{time},{title}, {update.effective_user.first_name},{update.effective_user.id}, \n')
        # {update.message.text} убрала пока - ругается что не везде он есть, надо разделить ф-ции лога 
        # на то, где есть сообщение или команда, и там, где просто выбор кнопки
        # и как-то фиксировать ответ бота

# query