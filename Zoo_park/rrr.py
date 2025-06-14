import telebot
from insta import TOKEN, questions, nach

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(content_types=['text', ])
def admin_rep(message):
    bot.send_message(message.chat.id, f' До начала функции {message.text}')
    if message.text == 'y':
        bot.send_message(message.chat.id, 'Введите сообщение')
        bot.register_next_step_handler(message, step)
        bot.send_message(message.chat.id, f' Вывыели в функции {message.text}')
    else:
        bot.send_message(message.chat.id, f'сообщение не соотвествует y - {message.text}')


def step(message):
    text = message.text
    bot.send_message(message.chat.id, f'ввели - {text}')

bot.polling()