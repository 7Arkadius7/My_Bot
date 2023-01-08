from creat_bot import dp
from aiogram.types import CallbackQuery
from keybords.Standart import main_menu


@dp.callback_query_handler(text='ADD')
async def add_cmd(callback: CallbackQuery):
    print(callback)
    await callback.answer('Успешно добавлено в корзину!', show_alert=False)