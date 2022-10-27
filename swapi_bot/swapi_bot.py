import telebot
from random import * #можно сделать такую команду, которая например из названий ищет подробнее рандомно про кого-то
from telebot import types
import requests


API_TOKEN='5751101961:AAGVOYtjx2-HaTZ8Z5wsx8YXehWVPryNDu4'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    # может сделать кнопки здесь, а не команды

