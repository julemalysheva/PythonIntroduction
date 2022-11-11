import telebot
from telebot import types
import config
from work import *
import numpy as np
import pandas as pd

API_TOKEN = config.Token
bot = telebot.TeleBot(API_TOKEN)
flight = []
flight_read = None
head_flight = ['date', 'type_flight', 'n_exe', 't_of_d', 'fl_hours', 'count_fl', 'score', 'num_rec']


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, f'''
    Приветствую, {message.from_user.first_name}!
    Я flight_accounting_bot.
    Помогу тебе вести учет полетов.
    Выбери интересующий пункт меню:
    /load - загрузить из файла
    /add - добавить информацию о полете
    /data - посмотреть сводные данные
    /select - выборки из базы
    ''')
    # /data - можно сделать меню с вариантами выборки по кнопкам
# добавить потом кнопочное меню
# при вводе значений можно добавить проверку формата через регулярку

def flight_load():
    global flight_read
    flight_read = pd.read_csv(
    'flight.csv', 
    delimiter=',', 
    # передаем заголовки в dataframe
    names = head_flight)
    print(flight_read)
    # print('тип данных', type(flight_read))


@bot.message_handler(commands=['load'])
def load_message(message):
    try:
        flight_load()
        bot.send_message(message.chat.id, text='''Данные загружены.
        Выбери интересующий пункт меню:
        /add - добавить информацию о полете
        /data - посмотреть сводные данные
        /select - выборки из базы
        ''')
    except:
        bot.send_message(message.chat.id, text='''Данные не обнаружены.
        Жми, чтобы добавить:
        /add - добавить информацию о полете''')
     

@bot.message_handler(commands=['add'])
def add_message(message):
    flight.clear()
    msg = bot.reply_to(
        message, 'Введи дату полета в поле для сообщений 👇 в формате xx.xx.xxxx')
    # регистрируем след.событие после ввода даты
    bot.register_next_step_handler(msg, date_input)

# здесь последовательно запрашивать поля и пока можно записывать в глобальный список - разораться с csv


def date_input(message):
    global flight
    try:
        flight_date = message.text
        flight.append(flight_date)
        print(flight)
        # добавить варианты через инлайн клавиатуру - 3 знач
        # может лучше сделать обычную? для считывания текста сразу в поле
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        b1 = types.InlineKeyboardButton(
            text='Десантирование войск боевой техники', callback_data='Десантирование')
        b2 = types.InlineKeyboardButton(
            text='Перевозка боевой техники и грузов', callback_data='Перевозка')
        b3 = types.InlineKeyboardButton(
            text='Полеты на СОЖ', callback_data='СОЖ')
        keyboard.add(b1, b2, b3)
        bot.reply_to(message, 'Выберите Вид боевого применения 👇',
                     reply_markup=keyboard)

    except Exception as e:
        bot.reply_to(message, 'oooops')


@bot.callback_query_handler(func=lambda call: True)
def user_choice(call):
    global flight
    text = call.data
    bot.answer_callback_query(call.id, "Принято")
    flight.append(text)
    print(flight)
    msg = bot.edit_message_text(chat_id=call.message.chat.id,
                                message_id=call.message.message_id, text='Введи номер упражнения')
    bot.register_next_step_handler(msg, exe_input)


def exe_input(message):
    global flight
    try:
        num_exe = message.text
        flight.append(num_exe)
        print(flight)
        # все упражнения, начинающиеся на 2 относятся к ночным, остальные к дневным
        if num_exe[0] == '2':
            flight.append('Н')
        else:
            flight.append('Д')
        msg = bot.reply_to(
            message, 'Отлично! Жду время полета 👇 в формате чч:мм\nНапример, 2:45; 3:00; 0:20 и т.д.')
        bot.register_next_step_handler(msg, time_input)
    except Exception as e:
        bot.reply_to(message, 'oooops')


def time_input(message):
    global flight
    try:
        # добавляю к значению секунды для типа timedelta64[ns] -  hh:mm:ss format
        flight_time = f'{message.text}:00'
        flight.append(flight_time)
        print(flight)
        msg = bot.reply_to(
            message, 'Ок! Сколько было полетов?')
        bot.register_next_step_handler(msg, count_input)
    except Exception as e:
        bot.reply_to(message, 'oooops')


def count_input(message):
    global flight
    try:
        flight_count = message.text
        if not flight_count.isdigit():
            msg = bot.reply_to(
                message, 'Нужно указать цифру. Введи число полетов:')
            bot.register_next_step_handler(msg, count_input)
            return
        flight.append(flight_count)
        print(flight)
        msg = bot.reply_to(
            message, 'Принял! Теперь введи оценку за боевое применение:')
        bot.register_next_step_handler(msg, eval_input)
    except Exception as e:
        bot.reply_to(message, 'oooops')


def eval_input(message):
    global flight
    try:
        flight_eval = message.text
        if not flight_eval.isdigit():
            msg = bot.reply_to(message, 'Нужно указать цифру. Введи оценку:')
            bot.register_next_step_handler(msg, eval_input)
            return
        flight.append(flight_eval)
        print(flight)
        msg = bot.reply_to(
            message, 'Супер! Укажи номер книжки/номер страницы\nнапример, 2/56')
        bot.register_next_step_handler(msg, num_str)
    except Exception as e:
        bot.reply_to(message, 'oooops')



def num_str(message):
    global flight
    try:
        flight_num = message.text
        flight.append(flight_num)
        print(flight)
        markup = types.ReplyKeyboardMarkup(
            one_time_keyboard=True, resize_keyboard=True)
        markup.add('Ок', 'Отмена')
        msg = bot.reply_to(
            message, f'Проверь и подтверди введенные данные по полету{str_list(flight)}', reply_markup=markup)
        bot.register_next_step_handler(msg, process_confirm)
    except Exception as e:
        bot.reply_to(message, 'oooops')


def process_confirm(message):
    global flight
    try:
        confirm = message.text
        if confirm == 'Ок':
            # вывести команды или кнопки меню в отдельную ф-цию и вызывать ее после события
            bot.reply_to(message, '''Данные сохранены.
            Выбери интересующий пункт меню:
            /add - добавить информацию о полете
            /data - посмотреть сводные данные
            /select - выборки из базы''')
            # добавить запись в файл
            with open('flight.csv', 'a', encoding="utf8") as file:
                file.write(f"{','.join(flight)}\n")

        elif confirm == 'Отмена':
            bot.reply_to(message, '''Данные очищены.
            Выбери интересующий пункт меню:
            /add - добавить информацию о полете
            /data - посмотреть сводные данные
            /select - выборки из базы
        ''')
            flight.clear()
            print(f'Список очищен {flight}')
        else:
            raise Exception()
    except Exception as e:
        bot.reply_to(message, 'oooops')


@bot.message_handler(commands=['data'])
def data_message(message):
    # обновляем DataFrame
    flight_load()    
    bot.send_message(message.chat.id, text=flight_read.to_string())
    bot.send_message(message.chat.id, text=flight_read.to_markdown(tablefmt="grid"))
    print(flight_read.to_markdown())
    print(flight_read.index)
    print(flight_read.info())
    # сформировать здесь свод в разрезе нужных группировок - только общие данные
#  .to_markdown() - отправить красиво, может файлом?
# изменение типа данных - это можно вынести в раб.модуль
    # flight_read['fl_hours'] = flight_read['fl_hours'].astype("datetime64[ns]") - это можно использовать для дат
    # чтоб формировать запрос в периоде

    # для этого преобразования - нужно собрать в строке формат hh:mm:ss format
    flight_read['fl_hours'] = flight_read['fl_hours'].astype("timedelta64[ns]") 
    print('смена типа\n',flight_read.info())
    tdi = flight_read.fl_hours.sum() #сумма налета часов - считает дельты по строкам
    print(tdi) #0 days 07:15:00
    # tdi = tdi /  np.timedelta64(1,  "h") #пытаюсь перевести в часы, получаю верно - тип Флоат
    # print(tdi) #7.25
    # пробую получить только часы и минуты без дней
    minutes = tdi.total_seconds()/60
    hours = minutes/60
    print(tdi.total_seconds(),minutes, hours) #26100.0 435.0 7.25

    bot.send_message(message.chat.id, text=f'Время вылетов:\n {flight_read.fl_hours}')
    bot.send_message(message.chat.id, text=f'Сумма налета: {flight_read.fl_hours.sum()}')
    # в итоге мне нужен именно этот показатель в часах - Сумма налета к часам: 7.25
    # в разных вариантах группировки
    bot.send_message(message.chat.id, text=f'Сумма налета к часам: {flight_read.fl_hours.sum()/ np.timedelta64(1,  "h")}')
    bot.send_message(message.chat.id, text=f'Сумма вылетов: {flight_read.count_fl.sum(numeric_only=True)}')

    # формирую свод: Время суток - Налет - кол.полетов
    # article_read.groupby('source').count()[['user_id']]
    print('для свода\n',flight_read.info())
    svod_data = flight_read.groupby(['t_of_d','type_flight']).sum(numeric_only=False)[['fl_hours','count_fl']]
    print(svod_data.to_markdown())
    # print(df.to_markdown(tablefmt="grid"))
    bot.send_message(message.chat.id, text=f'Свод по времени суток:\n {svod_data.to_markdown(tablefmt="grid")}')


@bot.message_handler(commands=['select'])
def selections_message(message):
    # а можно все выборки не напрямую высылать сообщением, а помещать либо в текстовый файл, либо в Эксель
    # Vожно использовать функцию to_excel() для записи содержимого в файл. Единственный аргумент — это путь к файлу:
    # df.to_excel('./teams.xlsx')
    # frame.to_excel('data2.xlsx')
    # обновляем DataFrame
    flight_load()    
    # выборки по полям/значениям - пробую варианты - потом их разместить под кнопки и обработчиком текста выводить
    # по своим ф-циям
    fn = flight_read["type_flight"].map(lambda x: x == "Десантирование")
    # аналогично по др. полям - но здесь нет итогов
    print(flight_read[fn])
    bot.send_message(message.chat.id, text=flight_read[fn].to_markdown())
    # ночные/дневные
    fn = flight_read["t_of_d"].map(lambda x: x == "Д")
    print('дневные', flight_read[fn])
    bot.send_message(message.chat.id, text=f'Дневные полеты \n{flight_read[fn].to_markdown()}')
    # ночные
    fn = flight_read["t_of_d"].map(lambda x: x == "Н")
    print('ночные', flight_read[fn])
    bot.send_message(message.chat.id, text=f'Ночные полеты \n{flight_read[fn].to_markdown()}')

# вопрос по удалению - стоит ли добавлять?
# если да - то удалять из фрейма, а потом его перезаписывать в файл? - проверить!
# сейчас у меня в каждой команде загружается он из файла, новое также сразу добавляется в файл
# перед удалением можно выслать юзеру эксель файл с полным перечнем, он выбирет индекс(ы) для удаления

bot.polling()
