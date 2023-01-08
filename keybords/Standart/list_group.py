from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

kb_print = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True) #one_time_keyboard - клавиатура исчезает после нажатия


btn_start = KeyboardButton(text='/start')
btn_print = []
city = ['/Анапа', '/Геленжик', '/Сочи', '/Тверь']

for town in city:
    btn_print.append(KeyboardButton(text=town))

kb_print.row(*btn_print)
kb_print.add(btn_start)
