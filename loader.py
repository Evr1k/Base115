from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import sqlite3 as sq

from data.config import TOKEN
bot = Bot(TOKEN)
dp = Dispatcher(bot)


def sql_start():
    """ Подключение к базе данных """
    global base, cur
    base = sq.connect('data/database.db')
    cur = base.cursor()
    if base:
        print('Data base connected - OK')
