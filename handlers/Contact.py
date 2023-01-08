from creat_bot import dp
from aiogram.types import Message



@dp.message_handler(commands=['contact'])
async def count_bot(message: Message):
    await message.answer(text='Раз, два, три, четыре, пять...')
