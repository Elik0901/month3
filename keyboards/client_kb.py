from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

male_button = KeyboardButton("Мальчик")
female_button = KeyboardButton("Девочка")

direction_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).add(male_button, female_button)


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