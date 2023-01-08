from creat_bot import dp
from aiogram.types import Message
from keybords import kb_print



@dp.message_handler(commands=['Анапа'])
async def count_bot(message: Message):
    await message.answer(text='Славный город Анапа...', reply_markup=kb_print)
