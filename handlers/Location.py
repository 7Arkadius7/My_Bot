from creat_bot import dp
from aiogram.types import Message


@dp.message_handler(commands=['Location'])
async def way_bot(message: Message):
    await message.reply(text='Это твой путь!)')
