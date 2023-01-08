from creat_bot import dp
from aiogram.types import Message
from keybords.Standart import main_menu


@dp.message_handler(commands=['end'])
async def end_bot(message: Message):
    await message.answer(text='Bye, my friend!)')
    main_menu.btn_location['text'] = 'Измена'

