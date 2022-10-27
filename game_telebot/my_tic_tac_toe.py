import telebot
from random import *
from telebot import types
from game_work import *
from time import sleep as s
import config
from telebot import *


API_TOKEN=config.Token
bot = telebot.TeleBot(API_TOKEN)

step = 0
field = []
players = {}
hod = True
finish = False

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,f"Привет, {message.from_user.first_name}!\nПоиграем в крестики-нолики?!\nЖми /game")

@bot.message_handler(commands=['game'])
def game_message(message):
    global field, players, hod,finish, step
    step = 0
    finish = False
    field = new_field()
    text = print_field(field)
    bot.send_message(message.chat.id,f"Игровое поле:\n{text}")
    players, first_step, hod = set_players(message.from_user.first_name)
    bot.send_message(message.chat.id,f"\nЖребий выпал. Первым ходит:\n{first_step}")
    s(1)
    print('первый ход: ', hod)
    if first_step == 'bot':
        bot_step(message)
        # bot.register_next_step_handler(message, bot_step) #пробую не передавать аргумент
    else: 
        chat_user(message)
        # bot.register_next_step_handler(message,chat_user)    
        
    #     bot.send_message(message.chat.id,f'''Играйте! Вы ходите -{players[False][0]}-\nЧтобы сделать ход - 
    # выберите соответствующую кнопку''',reply_markup=make_board(field))

        # bot.register_message_handler(user_step,hod=False)
        # AttributeError: 'TeleBot' object has no attribute 'register_message_handler' не находит метод
        # bot.register_next_step_handler(msg,user_step)
        # bot.register_message_handler(start_executor, commands=['start']) # Start command executor
    # chat(message)

# @bot.message_handler(content_types=['text'])
# def chat(message):
#     global finish
#     # описать ходы?
#     if step < 10: 
#         if not finish:
#             print('ход: ', hod)
#             s(1)
#             if hod: #т.е. если True - это бот
#                 # bot.register_next_step_handler(message,bot_step)
#                 bot_step(message)
#                 # bot.send_message(message.chat.id,'Здесь будет ход бота') 
#                 # bot.register_next_step_handler(message,chat)
#             else: #т.е. если False - это человек,отправляем инлайн клавиатуру и обрабатываем call
#                 bot.send_message(message.chat.id,f'''Играйте! Вы ходите -{players[False][0]}-\nЧтобы сделать ход - 
#             выберите соответствующую кнопку''',reply_markup=make_board(field))
#             # это добавить либо в обработку call, либо здесь это делать - посмотрим, но все равно нужен отдельный @
#             # для обработки нажатия кнопки -поэтому лучше туда при положительном присвоении
#                 # plus_step()
#                 # reverse_hod()
#                 # это где оставить, здесь или в call?
#                 bot.register_next_step_handler(message,chat)

#         else: bot.send_message(message.chat.id,'Игра завершена') 
#     else: 
#         finish = True
#         bot.send_message(message.chat.id,'Игра завершена') 
            
def chat_user(message):
    if step < 10: 
        if not finish:
            print('ход юзера до нажатия кнопки: ', hod)
            s(1)
            bot.send_message(message.chat.id,f'''Играйте! Вы ходите -{players[False][0]}-\nЧтобы сделать ход - 
            выберите соответствующую кнопку''',reply_markup=make_board(field))
        else: bot.send_message(message.chat.id, 'Игра завершена\nНачните новую /game')
    else: bot.send_message(message.chat.id, 'Игра завершена\nНачните новую /game')
    

def make_board(field):
    keyboard = types.InlineKeyboardMarkup(row_width=3)
    # по хорошему можно сделать в цикле обхода списка - добавляя строку
    b1 = types.InlineKeyboardButton(text=field[0][0], callback_data='0 0')
    b2 = types.InlineKeyboardButton(text=field[0][1], callback_data='0 1')
    b3 = types.InlineKeyboardButton(text=field[0][2], callback_data='0 2')
    b4 = types.InlineKeyboardButton(text=field[1][0], callback_data='1 0')
    b5 = types.InlineKeyboardButton(text=field[1][1], callback_data='1 1')
    b6 = types.InlineKeyboardButton(text=field[1][2], callback_data='1 2')
    b7 = types.InlineKeyboardButton(text=field[2][0], callback_data='2 0')
    b8 = types.InlineKeyboardButton(text=field[2][1], callback_data='2 1')
    b9 = types.InlineKeyboardButton(text=field[2][2], callback_data='2 2')
    keyboard.add(b1, b2, b3, b4, b5, b6, b7, b8, b9)
    return keyboard


# увеличиваем шаг игры
def plus_step():
    global step
    step += 1
# меняем ход на противоположный
def reverse_hod():
    global hod
    hod = not hod
    return hod    

def bot_step(message):
    global finish, field
    if not none_hod(field) and not finish: 
        pl = ch_field(field)
        print('ход бота: ', hod)
        print(pl)
        s(1)
        bot.send_message(message.chat.id,f"\nbot ходит:\n{players[True][0]} на {pl[0]+1}, {pl[1]+1}")
        field[pl[0]][pl[1]] = players[True][0]
        plus_step()
        reverse_hod()
        text = print_field(field)
        bot.send_message(message.chat.id,f"Игровое поле:\n{text}")
        if check_win(field, players[True][0]):
            bot.send_message(message.chat.id,f"Bot выиграл!\n-{players[True][0]}-ки победили\nНачните новую /game")
            print('Bot выиграл!')
            finish = True
        else: 
            if step < 10:
                chat_user(message)
            elif not finish:
                finish = True
                bot.send_message(message.chat.id,f"Игра завершена в ничью\nИгровое поле:\n{text}\nНачните новую /game")    
            # bot.register_next_step_handler(message,chat_user)    
    else: bot.send_message(message.chat.id,f"Игра завершена\nИгровое поле:\n{text}\nНачните новую /game")
    # в конце можно регистрировать след.ход,на chat
    # bot.register_next_step_handler(message,chat_user)


# обрабатываем нажатие кнопки 
# здесь обрабатывается полученная позиция - устанавливается новое значение
# индексы поля, куда вносим значения, если свободны, call - чтоб добраться до message.chat.id и call.id
@bot.callback_query_handler(func=lambda call: True)
def user_step(call):
    global field, finish
    print('ход юзера: ', hod)
    # пробую обработать несвоевренное нажатие, иначе выкидывает из бота
    try:
        if not hod:
            if not finish: #not none_hod(field) and not finish:
                text = call.data.split()
                pl = list(map(int, text))
                print(pl)
                if field[pl[0]][pl[1]] == '_':
                    field[pl[0]][pl[1]] = players[False][0]
                    plus_step()
                    reverse_hod()
                    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=make_board(field))
                    # bot.edit_message_reply_markup(message.chat.id, message.message_id, 'Выбери:', reply_markup=keyboard2)
                    # text = print_field(field)
                    # bot.send_message(message.chat.id,f"Игровое поле:\n{text}")
                    if check_win(field, players[False][0]):
                        # bot.send_message(message.chat.id,f"Поздравляю с выигрышем!\n-{players[False][0]}-ки победили")
                        print('Поздравляю с выигрышем!')
                        finish = True
                        bot.send_message(call.message.chat.id, f"Поздравляю с выигрышем!\n-{players[False][0]}-ки победили\nНачните новую /game")
                    else:
                        if step < 10:
                            bot_step(call.message)
                        elif not finish:
                            finish = True
                            bot.send_message(call.message.chat.id,f"Игра завершена в ничью\nИгровое поле:\n{text}\nНачните новую /game")    
                    # bot.register_next_step_handler(call.message,bot_step)
                else:
                    bot.answer_callback_query(callback_query_id=call.id, text='Эта клетка уже занята!')

            else:
                bot.answer_callback_query(call.message.chat.id, 'Игра завершена!')
        else:
            bot.answer_callback_query(callback_query_id=call.id, text='Не твой ход! Ожидай бота!')
        
        # в конце можно регистрировать след.ход,на chat
    except:
        bot.send_message(call.message.chat.id,f"Oooops! Что-то пошло не так...\nНачните сначала /start")    


@bot.message_handler(commands=['stop'])
def stop_message(message):
    global finish
    bot.send_message(message.chat.id,f"Ок - прекращаю игру..")
    # bot.stop_bot() #так совсем останавливает бот с ошибкой
    finish = True
    bot.send_message(message.chat.id,f"Для начала новой игры выберите\n/game")


bot.polling()
