from aiogram import types, Dispatcher
from config import bot, ADMIN


def get_user_username(from_user):
    if from_user.username is None:
        return from_user.first_name
    return from_user.username


async def ban(message: types.Message):
    if message.chat.type != "private":
        if message.from_user.id not in ADMIN:
            await message.answer('я не буду этого делать ты всего лишь подданный!')
        elif not message.reply_to_message:
            await message.answer('а кого банить то?')
        else:
            await bot.kick_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)
            await message.answer(text=f"{get_user_username(message.reply_to_message.from_user)} вышел сам!")
    else:
        await message.answer('в группе делай!')


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(ban, commands=['ban'], commands_prefix='!/')
