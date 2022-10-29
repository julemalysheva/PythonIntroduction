import telebot
from random import * #можно сделать такую команду, которая например из названий ищет подробнее рандомно про кого-то
from telebot import types
import requests
import json
import config
from processing_swapi import *
from json import *


API_TOKEN=config.Token
bot = telebot.TeleBot(API_TOKEN)
root_url = 'https://swapi.dev/api/'

@bot.message_handler(commands=['start'])
def start_message(message):
    # может сделать кнопки здесь, а не команды
    bot.send_photo(message.chat.id,'https://images.stopgame.ru/blogs/2017/06/04/d1-4QnO.jpg')   
    bot.send_message(message.chat.id, f'''
    Приветствую, {message.from_user.first_name}!
    Я бот по Star Wars.
    Помогу тебе найти информацию.
    Используй команды:
    /people - получить все ресурсы людей
    /films - получить все киноресурсы
    /starships - получить все ресурсы звездолета
    /vehicles - получить все ресурсы транспортного средства
    /species - получить все ресурсы по видам персонажей
    /planets - получить все ресурсы планеты
    ''') 

@bot.message_handler(commands=['people'])
def get_people(message):
    # как бы здесь добавить индикатор выполнения или гиф с часами хотя бы
    bot.send_message(message.chat.id, 'Идет поиск...,\nожидайте, пожалуйста')
    photo = open("A:\GB\PY\swapi_bot\img\main.gif", 'rb')
    bot.send_animation(message.chat.id, photo)
    photo.close()
    #  "next": null, в конце, по 10 героев на странице
    # "https://swapi.dev/api/people/?page=1"
    # r = requests.get(url='https://swapi.dev/api/people/').json()
    # bot.send_message(message.chat.id, f'Нашел героев, всего - {r["count"]}')

    # можно потом вынести в отдельную ф-цию, если по всем делать однотипные, просто передавать команду в url запроса
    # а тип запроса и корневой url везде одинаковые - они возвращают список, мы его передаем в ф-цию, которая собирает
    # инлайн клавиатуру - в data_call нужно помимо названия из списка добавить имя переданной команды для 
    # последующей организации поиска
    name_people = []
    i = 1
    while i != 0:
        try:
            r = requests.get(url=f'https://swapi.dev/api/people/?page={i}').json()
            if 'results' in r:
                print('Нашел results')
                for el in r['results']:
                    # bot.send_message(message.chat.id, el['name'])
                    name_people.append(el['name'])
            
            bot.send_message(message.chat.id, f'след.страница - {r["next"]}')
            if r["next"] != None: 
                i+=1
            else: i = 0            
        except:
            print('что-то пошло не так')    
            bot.send_message(message.chat.id, 'что-то пошло не так\nпопробуй еще раз или позже..')
    print(name_people)      
    # bot.send_message(message.chat.id, ','.join(name_people))
    bot.send_message(message.chat.id, "Жми, чтоб получить подробнее", reply_markup=make_keyboard(name_people,'people'))

# формируем клавиатуру по 3 кнопки в строке  
# можно в эту ф-цию передавать раздел, откуда пришел запрос, например people, и собирать это в callback_data,
# чтоб при обработке callback_data вести поиск в нужном разделе
# https://swapi.dev/api/people/?search=r2 - можно сразу формировать поисковый запрос в значение кнопки
# https://swapi.dev/api/ - это базовый url

def make_keyboard(li_item, resource):
    markup = types.InlineKeyboardMarkup(row_width = 3)
    i = 0
    while i < len(li_item)-2:
        b1 = types.InlineKeyboardButton(li_item[i], callback_data=f'{resource}/?search={li_item[i]}')
        b2 = types.InlineKeyboardButton(li_item[i+1], callback_data=f'{resource}/?search={li_item[i+1]}')
        b3 = types.InlineKeyboardButton(li_item[i+2], callback_data=f'{resource}/?search={li_item[i+2]}')
        markup.add(b1,b2,b3)
        i+=3
# остаток также помещаем в клавиатуру
    if len(li_item)/3!=0:
        row = [types.InlineKeyboardButton(el, callback_data=f'{resource}/?search={el}') for el in li_item[i:]]
        markup.add(*row)    
    return markup    

#обработка нажатия инлайн кнопок 
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    # ссылка для поиска всегда берется из ответа: базовый url+полученный из кнопки
    search_url = root_url+call.data
    # дальше смотри, может в зависимости от ресурса нужно собирать разные поля, тогда можно проверить:
    if 'people' in call.data:
        bot.answer_callback_query(call.id, "Сейчас поищу")
        r = requests.get(url=search_url).json()
        print(r["results"][0])
        item = r["results"][0]
        # передали словарь для обработки красивого вывода - получили текст
        item = print_people(r["results"][0])
        bot.send_message(call.message.chat.id, f"По запросу найдено\n{item}")
        # нужно поискать картинку) этот адрес нужно собрать через запрос
        bot.send_photo(call.message.chat.id,'https://avatars.mds.yandex.net/i?id=3085ef43b7c7d7b5faa6e13460ba624f-5607836-images-thumbs&n=13')


   
bot.polling()