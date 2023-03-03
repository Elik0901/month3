from aiogram import types, Dispatcher
from config import bot, dp


async def quiz_3(call: types.CallbackQuery):
    question = 'откуда мем?'
    answer = [
        'с фильма',
        'от школьника',
        'от верблюда'
    ]

    photo = open('media/mm.jpg', 'rb')
    await bot.send_photo(call.message.chat.id, photo= photo)

    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answer,
        type='quiz',
        is_anonymous=True,
        correct_option_id=1,
        explanation='больше 3 лет'
    )
def register_client(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_3, lambda call: call.data =='button_1' )