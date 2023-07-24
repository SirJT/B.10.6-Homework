

import telebot
from config import keys, TOKEN
from extensions import CriptoConverter, APIExeptions



bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['hi'])
def echo_test(message: telebot.types. Message):
    bot.send_message(message.chat.id, 'Hello')








@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)

@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
     text = 'Чтобы начать работу введите команду боту в следующем формате: \n<имя валюты цену которой он хочет узнать>\<имя валюты в которой надо узнать цену первой валютыы>\<количество первой валюты>\nУвидеть список достуных валют: /values'
     bot.reply_to(message, text)

@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')
        if len(values) != 3:
            raise APIExeptions('Слишком много параметров')

        quote, base, amount = values
        total_base = CriptoConverter.get_price(quote, base, amount)
    except APIExeptions as e:
        bot.reply_to(message, f'Ошибка пользователя\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')


    else:
        text = f' Цена {amount} {quote} в {base} - {total_base}'
        bot.send_message(message.chat.id, text)





bot.polling(none_stop=True)