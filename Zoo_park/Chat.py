import telebot
import sys
from extclass import CriptoConvert, APIException
from data import TOKEN, questions, nach

bot = telebot.TeleBot(TOKEN)
"""
@bot.message_handler()
def echo_test(message:telebot.types.Message):
    bot.send_message(message.chat.id, 'Hello')
"""



@bot.message_handler(commands = ['start', 'help'])
def help_start(message:telebot.types.Message):
    text = f'Московский зоопарк привествует Вас!!!\n {nach}\nПредлагаем Вам пройти тест и определить своё тотемное животное.\
\n Для начала теста введите <да>, для отказа введите любой другой символ'
    bot.reply_to(message, text)

#@bot.message_handler(content_types = ['text', ])
def test (message:telebot.types.Message):
    for key, val in questions.items():
        bot.send_message(message.chat.id, val)


@bot.message_handler(content_types = ['text', ])
def values (message:telebot.types.Message):
    values = message.text
    if values == 'да':
        bot.send_message(message.chat.id, 'Хорошо, тогда  начнём')
        bot.send_message(message.chat.id, nach)
        test(message)
    else:
        bot.send_message(message.chat.id, 'Очень жаль. Если передумайте, то набери <да>')
        #sys.exit() выключаем телеграмм бот



"""
@bot.message_handler(content_types = ['text', ])
def values (message:telebot.types.Message):
    values = message.text
    if values == 'да':
        bot.reply_to(message, 'Хорошо, тогда  начнём')
        test()



@bot.message_handler(content_types = ['text', ])
def test (message:telebot.types.Message):
    for key in questions.keys():
        bot.send_message(message.chat.id, questions(key))



обработка исключений
@bot.message_handler(content_types = ['text', ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')
        if len(values) != 3:
            raise APIException('Ошибка в параметрах')
        quote, base, amount = values
        total_base = CriptoConvert.get_price(quote, base, amount)
    except APIException as e:
        bot.reply_to(message, f'Ошибка пользователя\n {e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n {e}')

    else:
        tot = float(total_base)
        am = float(amount)
        itog = round(tot * am, 2)
        text = f'Цена {amount} {quote} в {base} - {itog}'
        bot.send_message(message.chat.id, f'{text}')
        
        """

bot.polling()

