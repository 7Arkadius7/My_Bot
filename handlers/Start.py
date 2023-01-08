from creat_bot import dp
from aiogram.types import Message
from keybords import kb_menu

@dp.message_handler(commands=['start'])
async def start_bot(message: Message):
    name = message.from_user.full_name
    await message.answer(f'{name}, приветствую тебя! Пожалуйста, выбери один из пунктов меню.', reply_markup=kb_menu)
    await dp.bot.send_message(chat_id=message.from_user.id, text='Стартуем через 5, 4, 3, 2, 1 ......')

