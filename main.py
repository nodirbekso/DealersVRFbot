import requests
import xlrd as xl
import telebot
from telebot import types
#from functions import *


bot = telebot.TeleBot("5730578811:AAEabzoxrROUy9A_NA5yImXMUiVqCichfeY")

@bot.message_handler(commands = ['url'])
def url(message):
    markup = types.InlineKeyboardMarkup()
    btn_my_site= types.InlineKeyboardButton(text='Бизнинг сайт', url='https://beeline.uz')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, "Сайтимизга утиш учун шу тугмани босинг.", reply_markup = markup)

@bot.message_handler(commands = ['click'])
def switch(message):
    markup = types.InlineKeyboardMarkup()
    switch_button = types.InlineKeyboardButton(text='17421',callback_data="17422")
    markup.add(switch_button)
    bot.send_message(message.chat.id, "17423", reply_markup = markup)



@bot.message_handler(commands=["start"])
def start(message):
    mess = f"<b>Ассалому алайкум {message.from_user.first_name} \n" \
           f"Ушбу бот Сизга Фаргона водийсида хизмат юритаётган дилерларимиз хакида маълумот беради. \n"  \
           f"Худудни танланг: </b> "
    bot.send_message(message.chat.id, mess, parse_mode="html")



bot.polling(none_stop=True)