from aiogram import Dispatcher,Bot
from decouple import config
TOKEN = config('TOKEN')
ADMIN = 1882059885


bot = Bot(TOKEN)
db = Dispatcher(bot=bot)
