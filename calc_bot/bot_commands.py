from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackContext, ConversationHandler
from datetime import datetime
from logger import log
from calc import calc_data, check_data

# здесь будут описываться сами команды для диспетчера
# а все расчеты будут тянутся из модуля calc

# log(update, context,title)
# вызывать лог в каждой команде/обработчике

# Этапы/состояния разговора
FIRST, SECOND, CALC = range(3)
# Данные обратного вызова
ONE, TWO = range(2)


def start(update, _):
    """Вызывается по команде `/start`."""
    # Получаем пользователя, который запустил команду `/start`
    user = update.message.from_user
    log(update, _, f'Пользователь начал разговор {update.message.text}')
    # logger.info("Пользователь %s начал разговор", user.first_name)
    # Создаем `InlineKeyboard`, где каждая кнопка имеет
    # отображаемый текст и строку `callback_data`
    # Клавиатура - это список строк кнопок, где каждая строка,
    # в свою очередь, является списком `[[...]]`
    keyboard = [
        [
            InlineKeyboardButton("Рассчитать выражение",
                                 callback_data=str(ONE)),
            InlineKeyboardButton("Посмотреть лог файл",
                                 callback_data=str(TWO)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Отправляем сообщение с текстом и добавленной клавиатурой `reply_markup`
    update.message.reply_text(
        text=f'''Приветствую, {user.first_name}! Я калькулятор-бот,
        \nпосчитаю выражение с целыми, рациональными и комплексными числами.'
        \nВыберите из предложенных пунктов меню:''', reply_markup=reply_markup
    )
    # Сообщаем `ConversationHandler`, что сейчас состояние `FIRST`
    return FIRST


def start_over(update, context):
    """Тот же текст и клавиатура, что и при `/start`, но не как новое сообщение"""
    # Получаем `CallbackQuery` из обновления `update`
    query = update.callback_query
    log(update, context, 'Пользователь вернулся в меню')
    # На запросы обратного вызова необходимо ответить,
    # даже если уведомление для пользователя не требуется.
    # В противном случае у некоторых клиентов могут возникнуть проблемы.
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Рассчитать выражение",
                                 callback_data=str(ONE)),
            InlineKeyboardButton("Посмотреть лог файл",
                                 callback_data=str(TWO)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
   # Отредактируем сообщение, вызвавшее обратный вызов.
   # Это создает ощущение интерактивного меню.
    # query.edit_message_text(
    #     text="Выберите из предложенных пунктов меню:", reply_markup=reply_markup
    # )
    # делаю не изменение, а ответ, иначе затирается ранее выданный результат
    # update.message.reply_text(
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Выберите из предложенных пунктов меню:", reply_markup=reply_markup)
    # query.send_message(
    #     text="Выберите из предложенных пунктов меню:", reply_markup=reply_markup
    # )

    # Сообщаем `ConversationHandler`, что сейчас находимся в состоянии `FIRST`
    return FIRST


def input_data(update, _):
    """Запрос строки выражения"""
    log(update, _, 'Выбран пункт меню: "Рассчитать выражение"')
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text='''
    Обратите внимание:
    1. В рациональных числах 
    - не допускаются "," (запятые) - отделяйте дробную часть "." (точкой),
    например: 2.54-1.05*6.45 и т.п.
    2. Комплексные числа в выражении 
    - должны быть обрамлены скобками (), 
    например: (2+4j)*(1-3j)-(1+8j) и т.п.
    \n👇 Введите выражение в поле для сообщений: ''')
    # в этом состоянии фильтруется сообщение - если это текст и не команда, то вызывается след.ф-ция view_result
    return CALC


def view_result(update, _):
    log(update, _, f'Пользователь ввел выражение {update.message.text}')
    # log(update, _, 'Выдаем результат расчета')
    # в input_data просим ввести строку для расчета, после чего здесь выдаем результат через calc_data и
    # новые кнопки для возврата в меню или выхода из программы
    user_input = update.message.text
    if isinstance(check_data(user_input), tuple):
        try:
            # значения из кортежа передали переменным
            t, value = check_data(user_input)
            result = calc_data(t, value)
        except:
            result = 'Некорректное выражение'
    else:
        # В выражении недопустимые символы - возвращаем это пользователю
        result = check_data(user_input)

    log(update, _, f'Выдаем результат: {result}')

    keyboard = [
        [
            InlineKeyboardButton("Вернуться в Меню", callback_data=str(ONE)),
            InlineKeyboardButton("Нет, с меня хватит ...",
                                 callback_data=str(TWO)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Отправляем сообщение с текстом и добавленной клавиатурой `reply_markup`
    update.message.reply_text(
        text=f"{result}\nНачать сначала?", reply_markup=reply_markup
    )
    # Сообщаем `ConversationHandler`, что сейчас состояние `SECOND`
    return SECOND


def view_log(update, context):
    # показываем лог или отправляем файл
    # новые кнопки для возврата в меню или выхода из программы
    log(update, context, 'Выдаем лог-файл')

    """Показ выбора кнопок"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Вернуться в Меню", callback_data=str(ONE)),
            InlineKeyboardButton("Нет, с меня хватит ...",
                                 callback_data=str(TWO)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # ?клавиатуру добавить при отправке файла или изменять прошлое сообщение?
    # или здесь context?
    query.bot.send_document(chat_id=update.effective_chat.id, document=open('calc_bot/calc_bot.txt', 'rb'), caption='Файл лога',
                            )
    # update.message.reply_text(
    #     text="Начать сначала?", reply_markup=reply_markup
    # )
    context.bot.send_message(chat_id=update.effective_chat.id,
                        text="Начать сначала?", reply_markup=reply_markup)

    # query.edit_message_text(
    #     text="Начать сначала?", reply_markup=reply_markup
    # )
    # Переход в состояние разговора `SECOND`

    return SECOND


def end(update, context):
    """Возвращает `ConversationHandler.END`, который говорит
    `ConversationHandler` что разговор окончен"""
    log(update, context, 'Пользователь завершил разговор')
    query = update.callback_query
    query.answer()
    # update.message.reply_text(text="Увидимся в другой раз!")
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Увидимся в другой раз!")

    return ConversationHandler.END


def cancel(update, _):
    user = update.message.from_user
    log(update, _, 'Пользователь отменил разговор')
    update.message.reply_text('До новых встреч')
    # или edit_message_text?
    return ConversationHandler.END
