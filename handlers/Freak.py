from creat_bot import dp
from aiogram.types import Message


@dp.message_handler()
async def everything(message: Message):
    if message.text.isdigit():
        await message.reply(text=f'Я нашел циферку {message.text}')
    else:
        await message.reply(text='Мой твой не понимат (((')
        await dp.bot.send_message(chat_id=945887219, text=f'{message.from_user.full_name} писал какие-то гадости, а именно "{message.text}"')
