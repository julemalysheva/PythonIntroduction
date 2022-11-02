import telebot
from telebot import types
import requests
import config
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

# передавать срез команды, исключая / - 0 элемент [1:]
@bot.message_handler(commands=['people','films','starships','vehicles','species','planets'])
def get_commands(message):
    print(message.text)
    if message.text == '/films':
        name = 'title'
    else: name = 'name'    
    # как бы здесь добавить индикатор выполнения или гиф с часами хотя бы
    bot.send_message(message.chat.id, 'Идет поиск...,\nожидайте, пожалуйста')
    photo = open("A:\GB\PY\swapi_bot\img\main.gif", 'rb')
    bot.send_animation(message.chat.id, photo)
    photo.close()
    #  "next": null, в конце, по 10 героев на странице
    # "https://swapi.dev/api/people/?page=1"
    # r = requests.get(url='https://swapi.dev/api/people/').json()
    name_list = get_requests(message.text[1:],name, message)
    if len(name_list)>0:
        bot.send_message(message.chat.id, "Жми, чтоб получить подробнее", reply_markup=make_keyboard(name_list,message.text[1:]))

def get_requests(resource, name, message):
    name_list = []
    i = 1
    try:
        while i != 0:
            r = requests.get(url=f'https://swapi.dev/api/{resource}/?page={i}').json()
            if 'results' in r:
                print('Нашел results')
                for el in r['results']:
                    name_list.append(el[name])
            
            bot.send_message(message.chat.id, f'Ищу на след.странице...') 
            if r["next"] != None: 
                i+=1
            else: i = 0            
    except:
        print('что-то пошло не так')    
        bot.send_message(message.chat.id, 'что-то пошло не так\nпопробуй еще раз или позже..')
    print(name_list)  
    return name_list    

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
    if call.data != None:
        bot.answer_callback_query(call.id, "Сейчас поищу")
        r = requests.get(url=search_url).json()
        item = r["results"][0]
        # передали словарь для обработки красивого вывода - получили текст
        item = print_item(r["results"][0])
        bot.send_message(call.message.chat.id, f"По запросу найдено\n{item}")
        # вывод картинки или инфы, что ее не нашли
        search_unsplash_photo(call)

def print_item(dict):
    txt = ''
    not_li = ['created', 'edited','url']
    list_search_name = ['homeworld','species','vehicles','starships','residents','pilots','planets','characters',
    'people',]
    for k,v in dict.items():
        if k not in not_li and v != None:
            if k == 'homeworld':
                r = requests.get(v).json()  
                txt+= f'\n{str(k)}:\t\t{r["name"]}\n' 
            elif k == 'films':
                films = []
                for el in v:
                    r = requests.get(el).json()
                    films.append(r['title']) 
                txt+= f'\n{str(k)}:\t\t{" ,".join(films)}\n' 
            elif k in list_search_name:
                search_name = []
                for el in v:
                    r = requests.get(el).json()
                    search_name.append(r['name']) 
                txt+= f'\n{str(k)}:\t\t{" ,".join(search_name)}\n' 
            else:
                txt+= f'\n{str(k)}:\t\t{v}\n'
    return txt    

# идет поиск выдача фото в случае успеха
def search_unsplash_photo(call):
    # берем правую часть от строки, а именно имя героя и т.д.
    el_query = call.data.split('=')[1]
    query = f'https://api.unsplash.com/search/photos?page=1&query={el_query}'
    headers = {'Accept-Version': 'v1', 'Authorization': f'Client-ID {config.AccessKey}'}
    response = requests.get(query, headers=headers)
    if response.status_code == 200:
        try:
            print(response)
            response = response.json()
            item = response['results'][0]["urls"]['regular']
            autor = response['results'][0]["user"]['name']
            bot.send_message(call.message.chat.id, f"Вот что нашел на unsplash.com\nАвтор {autor}")
            bot.send_photo(call.message.chat.id,item)
        except: bot.send_message(call.message.chat.id, f"А вот картинку я не нашел...")    
    else: bot.send_message(call.message.chat.id, f"А вот картинку я не нашел...")

   
bot.polling()