from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import bot, ADMIN
from keyboards.client_kb import direction_markup, submit_markup, cancel_markup


class FSMAnketa(StatesGroup):
    id = State()
    name = State()
    age = State()
    region = State()
    gender = State()


async def fsm_start(message: types.Message):
    if message.chat.type == 'private' and message.from_user.id in ADMIN:
        await FSMAnketa.id.set()
        await message.answer(f"Здраствуй {message.from_user.full_name}")
    elif message.from_user.id not in ADMIN:
        await message.answer("ТЫ НЕ КУРАТОР!!!")
    else:
        await message.answer('Пиши в личку!')


async def load_id(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            data['id'] = int(message.text)

            await FSMAnketa.next()
            await message.answer("Как зовут?", reply_markup=cancel_markup)
    except:
        await bot.send_message(message.from_user.id, "id состоит только из цифр")


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAnketa.next()
    await bot.send_message(message.from_user.id, "сколько лет?", reply_markup=direction_markup)



async def load_age(message: types.Message, state: FSMContext):
    try:
        if 99 > int(message.text) > 18:
            async with state.proxy() as data:
                data['age'] = int(message.text)
            await FSMAnketa.next()
            await message.answer("откуда?", reply_markup=cancel_markup)
        else:
            await message.answer("возраст не подходит")
    except:
        await message.answer("Вводи только числа!")


async def load_region(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['region'] = message.text
    await FSMAnketa.next()
    await bot.send_message(message.from_user.id, "какой пол?", reply_markup=direction_markup)


async def load_gender(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['gender'] = message.text
        await bot.send_message(message.from_user.id, f"id - {data['id']},\n"
                                                     f"имя - {data['name']},\nвозраст - {data['age']}, \n"
                                                     f"region - {data['region']}\nпол - {data['gender']}")

    await FSMAnketa.next()
    await message.answer("Все правильно?", reply_markup=submit_markup)


async def submit(message: types.Message, state: FSMContext):
    if message.text.lower() == 'да':
        await state.finish()
        await bot.send_message(message.from_user.id, "Регистрация завершена")
    elif message.text.lower() == 'нет':
        await state.finish()
        await message.answer("Отмена")
    else:
        await message.answer('Не получилось!')


async def cancel_reg(message: types.Message, state: FSMContext):
    curren_state = await state.get_state()
    if curren_state is not None:
        await state.finish()


def register_handlers_fsm_anketa(dp: Dispatcher):
    dp.register_message_handler(cancel_reg, state='*', commands=['cancel'])
    dp.register_message_handler(cancel_reg, Text(equals='cancel', ignore_case=True),
                                state='*')

    dp.register_message_handler(fsm_start, commands=['anketa'])
    dp.register_message_handler(load_id, state=FSMAnketa.id)
    dp.register_message_handler(load_name, state=FSMAnketa.name)
    dp.register_message_handler(load_age, state=FSMAnketa.age)
    dp.register_message_handler(load_region, state=FSMAnketa.region)
    dp.register_message_handler(load_gender, state=FSMAnketa.gender)
    dp.register_message_handler(submit, state=FSMAnketa.submit)