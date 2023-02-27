from aiogram import executor
import logging
from config import db

from handlers import client,callback,admin,fsmdaivinchik,extra
client.reg_client(db)
fsmdaivinchik.register_handlers_fsm_anketa(db)
extra.reg_hand_extra(db)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(db, skip_updates=True)