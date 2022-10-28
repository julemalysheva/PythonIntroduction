import telebot
from random import * #можно сделать такую команду, которая например из названий ищет подробнее рандомно про кого-то
from telebot import types
import requests
import json
import config
from json import *


API_TOKEN=config.Token
bot = telebot.TeleBot(API_TOKEN)

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
    bot.send_message(message.chat.id, 'Поиск займет немного времени,\nожидай, пожалуйста')
    #  "next": null, в конце, по 10 героев на странице
    num_people = 0
    # "https://swapi.dev/api/people/?page=1"
    r = requests.get(url='https://swapi.dev/api/people/').json()
    bot.send_message(message.chat.id, f'Нашел героев, всего - {r["count"]}')
    i = 1
    while i != 0:
        try:
            r = requests.get(url=f'https://swapi.dev/api/people/?page={i}').json()

            if 'results' in r:
                print('Нашел results')
                for el in r['results']:
                    bot.send_message(message.chat.id, el['name'])
            
            bot.send_message(message.chat.id, f'след.страница - {r["next"]}')
            if r["next"] != None: #isinstance(r["next"],str):
                i+=1
            else: i = 0            
        except:
            print('что-то пошло не так')    
            bot.send_message(message.chat.id, 'что-то пошло не так')
    

   
bot.polling()