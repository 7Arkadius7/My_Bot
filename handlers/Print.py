from creat_bot import dp
from aiogram.types import Message
from keybords import kb_inline


@dp.message_handler(commands='print')
async def end_bot(message: Message):
    await message.answer(text="Привет!\nI'm printer, my friend!\nГотов выполнять Ваши команды.)", reply_markup=kb_inline)
