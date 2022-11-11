import telebot
from telebot import types
import config
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
    /select - получить выборки из базы в Excel
    /del - удалить запись по полету
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

    # изменение типа данных - указать формат даты, иначе предупреждает
    # пока это не стала реализовывать, отбора по датам нет еще
    # flight_read['date'] = flight_read['date'].astype("datetime64[ns]") 
    # - это можно использовать для дат - чтоб формировать запрос в периоде

    # меняем тип временные дельты
    # для этого преобразования - нужно собрать в строке формат hh:mm:ss format
    flight_read['fl_hours'] = flight_read['fl_hours'].astype("timedelta64[ns]") 
    print('смена типа\n',flight_read.info())


@bot.message_handler(commands=['load'])
def load_message(message):
    try:
        flight_load()
        bot.send_message(message.chat.id, text='''Данные загружены.
        Выбери интересующий пункт меню:
        /add - добавить информацию о полете
        /data - посмотреть сводные данные
        /select - получить выборки из базы в Excel
        /del - удалить запись по полету
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

# собирает строку для подтверждения ввода новой записи
def str_list(li):
    str_li = ''
    str_li += f'''\nДата: {li[0]}
    Вид боевого применения: {li[1]}
    № упр: {li[2]}
    Время суток: {li[3]}
    Налёт: {li[4]}
    Кол-во полётов: {li[5]}
    Оценка: {li[6]}
    № летной книжки: {li[7]}'''
    return str_li

def num_str(message):
    global flight
    try:
        flight_num = message.text
        flight.append(flight_num)
        print(flight)
        markup = types.ReplyKeyboardMarkup(
            one_time_keyboard=True, resize_keyboard=True)
        markup.add('Ок', 'Нет')
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
            /select - получить выборки из базы в Excel
            /del - удалить запись по полету''')
            # добавляется запись в текущий или вновь созданный файл по команде /add - завершающий шаг
            with open('flight.csv', 'a', encoding="utf8") as file:
                file.write(f"{','.join(flight)}\n")

        elif confirm == 'Нет':
            bot.reply_to(message, '''Данные очищены.
            Выбери интересующий пункт меню:
            /add - добавить информацию о полете
            /data - посмотреть сводные данные
            /select - получить выборки из базы в Excel
            /del - удалить запись по полету''')
            flight.clear()
            print(f'Список очищен {flight}')
        else:
            raise Exception()
    except Exception as e:
        bot.reply_to(message, 'oooops')


@bot.message_handler(commands=['data'])
def data_message(message):
    # обновляем DataFrame
    try:
        flight_load()    
        bot.send_message(message.chat.id, text=flight_read.to_markdown(tablefmt="grid"))
        print(flight_read.to_markdown())
        print(flight_read.index)
        print(flight_read.info())
        # сформировать здесь свод в разрезе нужных группировок - только общие данные
    #  .to_markdown() - отправить красиво, может файлом?

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
        print('для свода\n',flight_read.info())
        svod_data = flight_read.groupby(['t_of_d','type_flight']).sum(numeric_only=False)[['fl_hours','count_fl']]
        print(svod_data.to_markdown())
        # print(df.to_markdown(tablefmt="grid"))
        bot.send_message(message.chat.id, text=f'Свод по времени суток:\n {svod_data.to_markdown(tablefmt="grid")}')
    
    except:
        bot.send_message(message.chat.id, text='''Данные не обнаружены.
        Жми, чтобы добавить:
        /add - добавить информацию о полете''')

# по хорошему здесь и в ф-цмм выше д.б.только варианты выборки на кнопках, которые будут обрабатываться
# соотв.декоратором по типу текста и по условию в ф-ции
# здесь во фрейм выборки можно добавить итоговую строку с суммой?
@bot.message_handler(commands=['select'])
def selections_message(message):
    # а можно все выборки не напрямую высылать сообщением, а помещать либо в текстовый файл, либо в Эксель
    # Vожно использовать функцию to_excel() для записи содержимого в файл. Единственный аргумент — это путь к файлу:
    # df.to_excel('./teams.xlsx')
    # frame.to_excel('data2.xlsx')
    # обновляем DataFrame
    try:
        flight_load()    
        # выборки по полям/значениям - пробую варианты - потом их разместить под кнопки и обработчиком текста выводить
        # по своим ф-циям
        fn = flight_read["type_flight"].map(lambda x: x == "Десантирование")
        # аналогично по др. полям - но здесь нет итогов
        print(flight_read[fn])
        bot.send_message(message.chat.id, text=flight_read[fn].to_markdown(tablefmt="grid"))
        # ночные/дневные
        fn = flight_read["t_of_d"].map(lambda x: x == "Д")
        print('дневные', flight_read[fn])
        bot.send_message(message.chat.id, text=f'Дневные полеты \n{flight_read[fn].to_markdown(tablefmt="grid")}')
        # ночные
        fn = flight_read["t_of_d"].map(lambda x: x == "Н")
        print('ночные', flight_read[fn])
        bot.send_message(message.chat.id, text=f'Ночные полеты \n{flight_read[fn].to_markdown(tablefmt="grid")}')
    except:
        bot.send_message(message.chat.id, text='''Данные не обнаружены.
        Жми, чтобы добавить:
        /add - добавить информацию о полете''')

# вопрос по удалению - стоит ли добавлять?
# если да - то удалять из фрейма, а потом его перезаписывать в файл? - проверить!
# сейчас у меня в каждой команде загружается он из файла, новое также сразу добавляется в файл
# перед удалением можно выслать юзеру эксель файл с полным перечнем, он выбирет индекс(ы) для удаления
# при добавление добавляем сразу в файл, перед выборкой обновляем фрейм, а вот при удалении файл перезаписываем
# из текущего фрейма - посмотреть, как будет
@bot.message_handler(commands=['del'])
def delete_message(message):
        # обновляем DataFrame
    try:
        flight_load() 
        print('загрузили фрейм перед удалением строки')
        try:
            flight_read.to_excel('A:\GB\PY\data_flights.xlsx')  
            # по аналогии можно будет сделать диапазон через - или запятую
            bot.send_message(message.chat.id, '✍️ Укажи индекс для удаления строки\nСмотри левый столбец в файле 👇')
             # добавить кнопку Отмена и регистрацию след.обработчика при вводе ответа
            markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1=types.KeyboardButton("Отмена")
            markup.add(item1)
            doc = open('A:\GB\PY\data_flights.xlsx', 'rb')
            msg = bot.send_document(message.chat.id, doc,reply_markup=markup)
            doc.close()
            bot.register_next_step_handler(msg, del_row)
        except:         
            bot.send_message(message.chat.id, text='Не удалось сформировать файл с данными .xlsx')
            # здесь можно предложить кнопки: Все данные в Телеграм/Отмена
            # Все данные в Телеграм - показать таблицу фрейма-ее можно использ.еще где-то
            # Отмена - выдаем команды для выбора - также можно использовать еще где-то
    except:
        bot.send_message(message.chat.id, text='''Данные не обнаружены.
        Жми, чтобы добавить:
        /add - добавить информацию о полете''')

@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text=="Отмена":
        markup = telebot.types.ReplyKeyboardRemove()    
        bot.reply_to(message, '''Хорошо.
        Выбери интересующий пункт меню:
        /add - добавить информацию о полете
        /data - посмотреть сводные данные
        /select - выборки из базы
        /del - удалить запись по полету
        ''',reply_markup=markup)
    # elif message.text=="Кнопка 2":
    #     bot.send_message(message.chat.id,'Спасибо за прочтение статьи!')
    #     # markup.remove(item1) так она пересчает работать, но сама кнопка есть


def del_row(message):
    global flight_read
    if message.text != 'Отмена':
        try:
            index_row = message.text
            if not index_row.isdigit():
                msg = bot.reply_to(
                    message, 'Нужно указать цифру. Введи индекс записи:')
                bot.register_next_step_handler(msg, del_row)
                return
            try:    
                # удаляем запись из фрейма
                print('index del', index_row)
                #удаляет по числовому типу, поэтому пока сделала для 1 элемента 
                flight_read.drop(labels = [int(index_row)],axis = 0, inplace = True)
                print('del row\n', flight_read)
                # перезаписываем файл csv
                flight_read.to_csv('flight.csv',index=False, header=False)
                msg = bot.reply_to(
                    message, f'Принял! Запись под {index_row} индексом удалена.\nСмотри файл:')
                #отправить обновленный эксель
                    # обновляем DataFrame
                try:
                    flight_load() 
                    print('загрузили фрейм после удаления')
                    try:
                        flight_read.to_excel('A:\GB\PY\data_flights.xlsx')  
                        doc = open('A:\GB\PY\data_flights.xlsx', 'rb')
                        msg = bot.send_document(message.chat.id, doc)
                        doc.close()
                    except:         
                        bot.send_message(message.chat.id, text='Не удалось сформировать файл с данными .xlsx')
                        # здесь можно отправить данные в телеграм сразу
                except:
                    bot.send_message(message.chat.id, text='Данные не обнаружены.')

            except:
                bot.reply_to(message, f'Запись под {index_row} индексом не найдена')   
        except Exception as e:
            bot.reply_to(message, 'oooops')
    else:
        message_reply(message)        


bot.polling()
