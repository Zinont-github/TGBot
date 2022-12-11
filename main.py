import telebot as tb
from telebot import types
import wikipedia
import wikipedia as wiki
import re
import random

bot = tb.TeleBot('5920126622:AAH7XrZnUQhH6mst1KeGR5W_IQSmv-afUlU')
wikipedia.set_lang('ru')

def getwiki(s):
    try:
        wikipage = wiki.page(s)
        wikitext = wikipage.content[:1000]
        wikimas = wikitext.split('.')
        wikimas = wikimas[:-1]
        wikitext2 = ''
        for x in wikimas:
            if not ('==' in x):
                if (len((x.strip())) > 3):
                    wikitext2 = wikitext2 + x + '.'
            else:
                break
        wikitext2 = re.sub('\([^()]*\)', '', wikitext2)
        wikitext2 = re.sub('\([^()]*\)', '', wikitext2)
        wikitext2 = re.sub('\{[^\{\}]*\}', '', wikitext2)
        return wikitext2
    except Exception as e:
        return 'На Википедии нет информации об этом'

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('Coin')
    markup.add(button1)
    bot.send_message(message.chat.id, "Привет, в этом боте ты можешь сыграть в монетку(Орел или решка)-НАЖМИ COIN\nИли узнать о интересующем тебя слове из Википедии-ВВЕДИ СЛОВО".format(message.from_user),reply_markup=markup)

@bot.message_handler(content_types=['text'])
def coin(message):
    if message.text == 'Coin':
        number = random.randint(0, 2)
        if number == 0:
            bot.send_message(message.chat.id, "Выпал Орел")
        else:
            bot.send_message(message.chat.id, "Выпала Решка")
    else:
        bot.send_message(message.chat.id, getwiki(message.text))

bot.polling()