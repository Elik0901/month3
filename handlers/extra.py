import random
from aiogram import types, Dispatcher
from config import bot


async def echo(message: types.Message):
    if message.text == "python":
        await bot.send_dice(message.chat.id, emoji=random.choice(['🎲', '⚽', '🏀', '🎰', '🎯', '🎳']))
    else:
        await bot.send_message(message.from_user.id, message.text)


def reg_hand_extra(dp: Dispatcher):
    dp.register_message_handler(echo)
