import telebot
from telebot import types

token = "7823395074:AAEX4d0K-xfkjWfR5chpfuS9jDH9k52-qag"

bot = telebot.TeleBot("token")

web_app_url = "https://t.me/Hamstercopebot/webapp"

text = "Это приложение - копия игры Hamster Sofia!\n\nНажмите на кнопку снизу, что запустить его!"

button = types.InlineKeyboardButton('Запустить', url=web_app_url)
keyboard = types.InlineKeyboardMarkup()
keyboard.add(button)

@bot.message_handler(commands=['start'])
def send_message(message):
    bot.send_message(message.chat.id, text=text, reply_markup=keyboard)

bot.polling()