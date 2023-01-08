from aiogram.utils import executor
from handlers import dp
from data_base.SQLite import check_connection


async def on_start_up(_):
    print('Бот запущен и готов к работе')
    try:
        check_connection()
        print('Подключение к БД успешное!')
    except:
        print('Ошибка БД')


async def on_shat_down(_):
    print('Бот устал и ушел отдыхать!')
    await dp.bot.send_message(chat_id=945887219, text='Бот устал и ушел отдыхать!')

if __name__ == '__main__':
    executor.start_polling(dispatcher=dp, skip_updates=True, on_startup=on_start_up, on_shutdown=on_shat_down)  # skip_updates=True - удаляет все что присылали пользователи, когда бот не работал
