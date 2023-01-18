from view import *
from model import *
import telebot
from telebot import types

bot = telebot.TeleBot('5978852618:AAG-BBMaJ0EFIzxYdUWWWoIHziqiVU6Hi-A')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    view = types.KeyboardButton('Отобразить весь телефонный справочник')
    search = types.KeyboardButton('Поиск по фамилии')
    add = types.KeyboardButton('Добавить запись')
    delete = types.KeyboardButton('Удалить запись')
    markup.add(view, search, add, delete)
    mess = f'Привет, {message.from_user.first_name}. Выбери необходимое действие'
    bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_user_text(message):
    message.text = message.text.lower()
    if message.text =='отобразить весь телефонный справочник':
        all = get_all()
        bot.send_message(message.chat.id, show_all(all), parse_mode='Markdown')
    elif message.text == 'поиск по фамилии':
        bot.send_message(message.chat.id, 'Введите фамилию', parse_mode='html')
    elif message.text == 'добавить запись':
        bot.send_message(message.chat.id, "Введите фамилию, имя и номер телефона через пробел", parse_mode='html')
    elif message.text == 'удалить запись':
        bot.send_message(message.chat.id, 'Введите число', parse_mode='html')
    elif message.text == 'photo':
        photo = open('main_bot.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    else:
        try:
            number = int(message.text)
            delete(number-1)
            bot.send_message(message.chat.id, 'Запись успешно удалена', parse_mode='html')
        except:
            if len(message.text.split(' '))==1:
                all = get_all()
                bot.send_message(message.chat.id, searching(all, message.text.strip()), parse_mode='html')
            elif len(message.text.split(' '))==3:
                add(message.text.title().split(' '))
                bot.send_message(message.chat.id, 'Запись добавлена', parse_mode='html')
            else:

                bot.send_message(message.chat.id, 'Я тебя не понимаю', parse_mode='html')


bot.polling(none_stop=True)