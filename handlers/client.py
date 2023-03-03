from aiogram import types, Dispatcher
from config import bot, dp
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def hello_handler(massage: types.Message):
    await bot.send_message(massage.from_user.id, f'привет {massage.from_user.first_name}\n'
                                                 f'пока что не все')

async def mem1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton('Next', callback_data='button_1')
    markup.add(button_1)
    question = 'откуда мем?'
    answer = [
        'с фильма',
        'от школьника',
        'от верблюда'
    ]
    photo = open('media/mm.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo= photo)

    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answer,
        type='quiz',
        is_anonymous=True,
        correct_option_id=1,
        reply_markup =markup
    )
def reg_client(db: Dispatcher):
    db.register_message_handler(hello_handler, commands=['hello'])
    dp.register_message_handler(mem1, commands=['memi'])

