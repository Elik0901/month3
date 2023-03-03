from aiogram import Dispatcher,Bot
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage

TOKEN = config('TOKEN')
ADMIN = [1882059885]


bot = Bot(TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
