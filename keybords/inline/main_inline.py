from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from handlers.call_back.callback import goods

kb_inline = InlineKeyboardMarkup(row_width=2)

btn_add = InlineKeyboardButton(text='Добавить', callback_data='ADD')
btn_remove = InlineKeyboardButton(text='Купить', callback_data=goods.new(items='Товары', count='100'))
btn_print = InlineKeyboardButton(text='Печать', callback_data='PRINT_P')
btn_exit = InlineKeyboardButton(text='Выход', callback_data='EXIT')

kb_inline.row(btn_add, btn_remove)
kb_inline.add(btn_print)
kb_inline.add(btn_exit)
