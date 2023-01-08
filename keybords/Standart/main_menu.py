from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

kb_menu = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True) #one_time_keyboard - клавиатура исчезает после нажатия

btn_start = KeyboardButton(text='/start')
btn_end = KeyboardButton(text='/end')
btn_contact = KeyboardButton(text='/contact', request_contact=True)
btn_menu = KeyboardButton(text='/menu')
btn_location = KeyboardButton(text='/location', request_location=True)
btn_ID = KeyboardButton(text='/ID')
btn_print = KeyboardButton(text='/print')

kb_menu.add(btn_start)
kb_menu.row(btn_contact, btn_menu, btn_location, btn_ID)
kb_menu.add(btn_print)
kb_menu.add(btn_end)
