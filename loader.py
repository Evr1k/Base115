from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os

TOKEN = os.getenv("TOKEN")
bot = Bot(TOKEN)
dp = Dispatcher(bot)
