import json
import telebot
from telebot import types
from parse import parse_news

token = '5392394956:AAFIsrBe478thzZ07J2IoC6ZBPb86aV4FLg'

bot = telebot.TeleBot(token)

keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton('Photo')
btn2 = types.KeyboardButton('Description')
keyboard.add(btn1, btn2)


def read_news():
    with open('data.json') as file:
        data = json.load(file)
    return data

@bot.message_handler(commands=['start'])
def start_parse(message):
    print('!!!')
    bot.send_message(message.chat.id, 'Hello, We started to parse some articles! Pls wait a few seconds...')
    print('started')
    parse_news
    print('parsed')
    data = read_news()
    for x in data:
        print(x)
        bot.send_message(message.chat.id, f'{x} --> *{data [x]["title"]}*',  parse_mode='Markdown')
    bot_message = bot.send_message(message.chat.id, 'Choose number of article for detail info(1-20)')
    bot.register_next_step_handler(bot_message, check_num)


def check_num(message):
    nums = [str(x) for x in range(1, 21)]
    if message.text not in nums:
        print(message.text)
        bot_message = bot.send_message(message.chat.id, 'Invalid number! You must choose number in range 1 to 20:')
        bot.register_next_step_handler(bot_message, check_num)
    else:
        data = read_news()
        bot_message = bot.send_message(message.chat.id, f'{data[message.text]["title"]}', reply_markup=keyboard)
        bot.register_next_step_handler(bot_message, show_info, message.text, data )


def show_info(message, num, data):
    if message.text.lower() == 'photo':
        bot.send_message(message.chat.id, data[num]['img'])
        bot_message = bot.send_message(message.chat.id, 'Choose number of article for detail info(1-20)')
        bot.register_next_step_handler(bot_message, check_num)
    else:
        bot.send_message(message.chat.id, data[num]['desc'])
        bot_message = bot.send_message(message.chat.id, 'Choose number of article for detail info(1-20)')
        bot.register_next_step_handler(bot_message, check_num)


bot.polling()