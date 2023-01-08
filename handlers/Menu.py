from creat_bot import dp
from aiogram.types import Message
from keybords import kb_inline


@dp.message_handler(commands=['menu'])
async def menu_bot(message: Message):
    await message.answer(text='Вот тебе меню)', reply_markup=kb_inline)

