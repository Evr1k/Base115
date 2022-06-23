from aiogram import Bot
from aiogram.dispatcher import Dispatcher


from data.config import TOKEN

bot = Bot(TOKEN)
dp = Dispatcher(bot)
