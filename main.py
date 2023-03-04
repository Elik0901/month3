from aiogram import executor
import logging
from config import dp
from handlers import client, callback, admin, fsmdaivinchik, extra


admin.register_handlers_admin(dp)
client.reg_client(dp)
fsmdaivinchik.register_handlers_fsm_anketa(dp)
callback.register_client(dp)
extra.reg_hand_extra(dp)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)