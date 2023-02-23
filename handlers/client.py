from aiogram import types, Dispatcher
from config import bot, db


async def hello_handler(massage: types.Message):
    await bot.send_message(massage.from_user.id, f'привет {massage.from_user.first_name}\n'
                                                 f'пока что не все')


def reg_client(db: Dispatcher):
    db.register_message_handler(hello_handler, commands=['hello'])

