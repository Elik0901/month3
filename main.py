from aiogram import executor
import logging
from config import db

from handlers import client,callback,admin,extra
client.reg_client(db)
extra.reg_hand_extra(db)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(db, skip_updates=True)