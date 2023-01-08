from creat_bot import dp
from aiogram.types import Message



@dp.message_handler(commands=['id'])
async def id_user(message: Message):
    await dp.bot.send_message(chat_id=message.from_user.id, text=f'Твой ID -> {message.from_user.id}')