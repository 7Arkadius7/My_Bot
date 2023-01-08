from creat_bot import dp
from aiogram.types import CallbackQuery
from keybords.Standart import main_menu
from handlers.call_back.callback import goods



@dp.callback_query_handler(goods.filter(items='Товары'))
async def add_cmd(callback: CallbackQuery):
    new_text = f'Товары добавлены в корзину! {callback.data.split(":")[-1]}'
    await dp.bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id, text=new_text)
    await callback.answer('Успешно добавлено в корзину', show_alert=True)