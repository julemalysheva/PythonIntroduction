from dataclasses import field
import telebot
from random import *
from telebot import types
from game_work import *

API_TOKEN='5704779560:AAHgxQnfLfMsASBZxqFmy3xIbIaH-_ynCjE'
bot = telebot.TeleBot(API_TOKEN)

field = []
players = {}
hod = True
step = 0
def step_plus():
    global step
    step+=1

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,f"Привет, {message.from_user.first_name}!\nПоиграем в крестики-нолики?!\nЖми /game")

# пробую сделать через печать поля, подумать над вывором через 9 кнопок
@bot.message_handler(commands=['game'])
def game_message(message):
    global field, players, hod
    field = new_field()
    text = print_field(field)
    bot.send_message(message.chat.id,f"Игровое поле:\n{text}")
    players, first_step, hod = set_players(message.from_user.first_name)
    bot.send_message(message.chat.id,f"\nЖребий выпал. Первым ходит:\n{first_step}")
    if first_step == 'bot':
        pl = ch_field(field)
        print(pl)
        bot.send_message(message.chat.id,f"\nbot ходит:\n{players[hod][0]} на {pl[0]+1}, {pl[1]+1}")
        field[pl[0]][pl[1]] = players[hod][0]
        step_plus()
        text = print_field(field)
        bot.send_message(message.chat.id,f"Игровое поле:\n{text}")
        bot.send_message(message.chat.id,f'''Играйте!\nЧтобы сделать ход - введите команду: 
        '/mygo' №строки №столбца через пробел
        Например: "/mygo 2 2" - чтобы сходить в центр''')
    else:
        bot.send_message(message.chat.id,f'''Играйте!\nЧтобы сделать ход - введите команду: 
        '/mygo' №строки №столбца через пробел
        Например: "/mygo 2 2" - чтобы сходить в центр''')

# здесь везде делать проверку выигрыша и увеличивать шаг 
# [True - играет бот, False-играет человек]
@bot.message_handler(commands=['mygo'])
def game_message(message):
    global field
    if step < 10:
        pl = ch_input(message.text)
        print(pl)
        if not isinstance(pl, list): #если ошибка ввода - вернулась строка ошибки
            bot.send_message(message.chat.id,pl)
        else:
            if field[pl[0]-1][pl[1]-1] == '_':
                field[pl[0]-1][pl[1]-1] = players[False][0]
                step_plus()
                text = print_field(field)
                bot.send_message(message.chat.id,f"Игровое поле:\n{text}")
                if check_win(field, players[False][0]):
                    bot.send_message(message.chat.id,f"Поздравляю с выигрышем!\n-{players[False][0]}-ки победили")
                    print('Поздравляю с выигрышем!')
                    exit()
                # после успешного хода человека всегда ходит бот и передает ход человеку, предлагая команду
                if step < 10 and ch_field(field) != None:
                    pl = ch_field(field)
                    print(pl)
                    bot.send_message(message.chat.id,f"\nbot ходит:\n{players[True][0]} на {pl[0]+1}, {pl[1]+1}")
                    field[pl[0]][pl[1]] = players[True][0]
                    step_plus()
                    text = print_field(field)
                    bot.send_message(message.chat.id,f"Игровое поле:\n{text}")
                    if check_win(field, players[True][0]):
                        bot.send_message(message.chat.id,f"Bot выиграл!\n-{players[True][0]}-ки победили")
                        print('Поздравляю с выигрышем!')
                        exit()

                    if step<9:
                        bot.send_message(message.chat.id,f'''Играйте!\nЧтобы сделать ход - введите команду: 
                        '/mygo' №строки №столбца через пробел
                        Например: "/mygo 2 2" - чтобы сходить в центр''')
                    else: 
                        bot.send_message(message.chat.id,f"Игра завершена\nИгровое поле:\n{text}\nНачните новую /game")
                else: bot.send_message(message.chat.id,f"Игра завершена\nИгровое поле:\n{text}\nНачните новую /game")
    
            else:
                bot.send_message(message.chat.id,f'Место {", ".join(pl)} занято, повторите команду')
                text = print_field(field)
                bot.send_message(message.chat.id,f"Игровое поле:\n{text}")
    else:
        bot.send_message(message.chat.id,f"Игра завершена\nИгровое поле:\n{text}\nНачните новую /game")
            


    # for i in range(9):
    #     # elem_go = 'x' if i % 2 != 0 else '0'
    #     while True:
    #         if hod: #игрок бот,т.к.мы приняли его за True
    #             print(message)
    #             pass #прописать логику умного выбора

    #         else: #игрок человек
    #             bot.send_message(message.chat.id,f'Куда ходит -{players[hod][0]}-?\n Укажите через запятую \nномер строки и столбца: ')
    #             # @bot.message_handler(content_types='text')
    #             # def message_reply(message):
    #             # print(message)
    #             print(message.text)    
    #             pl = ch_input(message.text)
    #             print(pl)
    #             if not isinstance(pl, list): #если ошибка ввода - вернулась строка ошибки
    #                 bot.send_message(message.chat.id,pl)
    #             else:
    #                 if field[pl[0]-1][pl[1]-1] == '_':
    #                     field[pl[0]-1][pl[1]-1] = players[hod][0]
    #                     text = print_field(field)
    #                     bot.send_message(message.chat.id,f"Игровое поле:\n{text}")
    #                     break
    #                 else:
    #                     bot.send_message(message.chat.id,'Поле занято, повторите ход')
    #                     text = print_field(field)
    #                     bot.send_message(message.chat.id,f"Игровое поле:\n{text}")

        
    #     if i >= 2:
    #         if check_win(field, players[hod][0]):
    #             print('Поздравляю с выигрышем!')
    #             break
    #     # как-то прописать ничью тоже
    #     if i == 8 and not check_win(field, players[hod][0]):
    #         print('Игра завершена в ничью...')

    #     hod = not hod #смена хода    


bot.polling()