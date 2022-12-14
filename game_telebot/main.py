import telebot
from random import *
from telebot import types
from game_work import *
from time import sleep as s
import config


API_TOKEN=config.Token
bot = telebot.TeleBot(API_TOKEN)

field = []
players = {}
hod = True
finish = False

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,f"Привет, {message.from_user.first_name}!\nПоиграем в крестики-нолики?!\nЖми /game")

# пробую сделать через печать поля, подумать над выбором через 9 кнопок
@bot.message_handler(commands=['game'])
def game_message(message):
    global field, players, hod,finish
    finish = False
    field = new_field()
    text = print_field(field)
    bot.send_message(message.chat.id,f"Игровое поле:\n{text}")
    players, first_step, hod = set_players(message.from_user.first_name)
    bot.send_message(message.chat.id,f"\nЖребий выпал. Первым ходит:\n{first_step}")
    s(1)
    if first_step == 'bot':
        pl = ch_field(field,players[True][0],players[False][0])
        print(pl)
        bot.send_message(message.chat.id,f"\nbot ходит:\n{players[hod][0]} на {pl[0]+1}, {pl[1]+1}")
        field[pl[0]][pl[1]] = players[hod][0]
        text = print_field(field)
        bot.send_message(message.chat.id,f"Игровое поле:\n{text}")
        s(1)
        bot.send_message(message.chat.id,f'''Играйте! Вы ходите -{players[False][0]}-\nЧтобы сделать ход - введите команду: 
        '/go' №строки №столбца через пробел
        Например: "/go 2 2" - чтобы сходить в центр''')
    else:
        bot.send_message(message.chat.id,f'''Играйте! Вы ходите -{players[False][0]}-\nЧтобы сделать ход - введите команду: 
        '/go' №строки №столбца через пробел
        Например: "/go 2 2" - чтобы сходить в центр''')

# здесь везде делать проверку выигрыша и наличие свободного хода 
# [True - играет бот, False-играет человек]
# можно доработать - выдавать кнопки, повторяющие поле - для хода, и по нажатию добавлять в поле
@bot.message_handler(commands=['go'])
def game_message(message):
    global field, finish
    # если еще есть незанятые ячейки
    if not none_hod(field) and not finish:
        pl = ch_input(message.text)
        print(pl)
        if not isinstance(pl, list): #если ошибка ввода - вернулась строка ошибки
            bot.send_message(message.chat.id,pl)
        else:
            if field[pl[0]-1][pl[1]-1] == '_':
                field[pl[0]-1][pl[1]-1] = players[False][0]
                text = print_field(field)
                bot.send_message(message.chat.id,f"Игровое поле:\n{text}")
                if check_win(field, players[False][0]):
                    bot.send_message(message.chat.id,f"Поздравляю с выигрышем!\n-{players[False][0]}-ки победили")
                    print('Поздравляю с выигрышем!')
                    finish = True
                    # exit()
                    # bot.stop_bot()
                # после успешного хода человека всегда ходит бот и передает ход человеку, предлагая команду
                if not none_hod(field) and not finish: #ch_field(field) != None:
                    pl = ch_field(field,players[True][0],players[False][0])

                    print(pl)
                    s(1)
                    bot.send_message(message.chat.id,f"\nbot ходит:\n{players[True][0]} на {pl[0]+1}, {pl[1]+1}")
                    field[pl[0]][pl[1]] = players[True][0]
                    text = print_field(field)
                    bot.send_message(message.chat.id,f"Игровое поле:\n{text}")
                    if check_win(field, players[True][0]):
                        bot.send_message(message.chat.id,f"Bot выиграл!\n-{players[True][0]}-ки победили")
                        print('Bot выиграл!')
                        finish = True
                        # exit()
                        # bot.stop_bot()

                    if not none_hod(field) and not finish:
                        s(1)
                        bot.send_message(message.chat.id,f'''Играйте! Вы ходите -{players[False][0]}-\nЧтобы сделать ход - введите команду: 
                        '/go' №строки №столбца через пробел
                        Например: "/go 2 2" - чтобы сходить в центр''')
                    else: 
                        s(1)
                        bot.send_message(message.chat.id,f"Игра завершена\nИгровое поле:\n{text}\nНачните новую /game")
                else: bot.send_message(message.chat.id,f"Игра завершена\nИгровое поле:\n{text}\nНачните новую /game")
    
            else:
                bot.send_message(message.chat.id,f'Место {pl} занято, повторите команду')
                text = print_field(field)
                bot.send_message(message.chat.id,f"Игровое поле:\n{text}")
    else:
        s(1)
        text = print_field(field)
        bot.send_message(message.chat.id,f"Игра завершена\nИгровое поле:\n{text}\nНачните новую /game")

@bot.message_handler(commands=['stop'])
def stop_message(message):
    global finish
    bot.send_message(message.chat.id,f"Ок - прекращаю игру..")
    # bot.stop_bot() #так совсем останавливает бот с ошибкой
    finish = True
    bot.send_message(message.chat.id,f"Для начала новой игры выберите\n/game")


@bot.message_handler(content_types='text')
def message_reply(message):
    bot.send_message(message.chat.id,f'''{message.from_user.first_name}, пожалуйста, воспользуйтесь командами:
    /game - чтобы начать новую игру
    /go - чтобы совершить свой ход в текущей игре
    /stop - остановить игру
    ''')


bot.polling()