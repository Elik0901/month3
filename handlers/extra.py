from aiogram import types,Dispatcher
from config import bot,dp


async def echo(message: types.Message):
    await bot.send_message(message.from_user.id, message.text)
    await message.answer('что-то еще?')

def reg_hand_extra(db:Dispatcher):
    db.register_message_handler(echo)