from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

direction_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
)


submit_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
)
submit_markup1 = KeyboardButton("ДА")
submit_markup2 = KeyboardButton("НЕТ")

cancel_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).add(KeyboardButton('CANCEL'))

submit_markup.add(submit_markup1, submit_markup2)