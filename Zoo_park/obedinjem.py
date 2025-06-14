import telebot
from insta import TOKEN, questions, nach
from extclass import APIException, CriptoConvert

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])# Начало
def help_start(message: telebot.types.Message):
    text = f'Московский зоопарк привествует Вас!!!\n {nach}\nПредлагаем Вам пройти тест и определить своё тотемное животное.\
\n Для начала теста введите <да>, для отказа введите любой другой символ'
    bot.reply_to(message, text)

    bot.send_message(message.chat.id, f'Ответьте на вопрос {1}\n {questions[1]}')
    bot.send_message(message.chat.id, f'Введите номер ответа')


@bot.message_handler(content_types=['text', ])# Задаём вопрос о прохождении теста
def value(message: telebot.types.Message):
    values = message.text
    obrabotka(values, questions)
    except APIException as e:




        total_base = CriptoConvert.get_price(quote, base, amount)
    suma = 0
    bot.send_message(message.chat.id, f' начало теста - {message.text}')
    for i  in range(len(questions)):

        bot.register_next_step_handler(message, proba)

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

