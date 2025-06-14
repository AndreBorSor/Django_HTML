import telebot
from insta import TOKEN, questions, nach

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])# Начало
def help_start(message: telebot.types.Message):
    text = f'Московский зоопарк привествует Вас!!!\n {nach}\nПредлагаем Вам пройти тест и определить своё тотемное животное.\
\n Для начала теста введите <да>, для отказа введите любой другой символ'
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text', ])# Задаём вопрос о прохождении теста
def value(message: telebot.types.Message):
    bot.send_message(message.chat.id, f'Введите да или нет {message.text}')
    values = message.text

    if values != 'да': #Если нет, то останавливает бот
        bot.send_message(message.chat.id, 'Очень жаль. Если передумайте, то набери <да>')
        #bot.stop_polling()
    else:
        bot.send_message(message.chat.id, f'Очень хорошо!!!\n {nach}\n Давайте теперь начнём')
        #bot.register_next_step_handler(message,test)



@bot.message_handler(content_types = ['text', ])
def test(message: telebot.types.Message):# Выводим вопросы и получаем сумму балов
    suma = 0
    bot.send_message(message.chat.id, f' начало теста - {message.text}')
    for i  in range(len(questions)):
        bot.send_message(message.chat.id, f'Ответьте на вопрос {i+1}\n {questions[i]}')
        bot.send_message(message.chat.id, f'Введите номер ответа')
        bot.register_next_step_handler(message, proba)
       #tes = proba (message)
        tes = message.text
        bot.send_message(message.chat.id, f'ввели? {tes} - {type(tes)}')
        vv = int(tes)
        if 1 < vv > 4:
            bot.reply_to(message, 'Ошибка ввода')  # Вывести в отдкльный класс
        else:
            suma += vv
        bot.send_message(message.chat.id, f'тип вводимого {type(tes)} - {tes}')

    bot.send_message(message.chat.id, f'Сумма ответов равна {suma}')

#@bot.message_handler(content_types=['text', ])
def proba(message: telebot.types.Message):
    otv = message.text
    bot.send_message(message.chat.id, f'Вы ввели _____ {otv}')
    #bot.register_next_step_handler(message.text, test)
    return otv




bot.polling()

