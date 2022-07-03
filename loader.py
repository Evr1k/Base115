from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import sqlite3 as sq

from data.config import TOKEN
bot = Bot(TOKEN)
dp = Dispatcher(bot)
