import sqlite3 as sq
from sqlite3 import Connection

from loader import bot
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def sql_start():
    global base, cur
    base: Connection = sq.connect('data/database.db')
    cur = base.cursor()
    if base:
        print('Data base connected - OK')


async def get_all_details(message):
    keyboard = InlineKeyboardMarkup(row_width=4, resize_keyboard=True)
    for ret in cur.execute('''SELECT DISTINCT Деталь FROM details_operation''').fetchall():
        keyboard.insert(InlineKeyboardButton(f'{ret[0]}', callback_data=f'time_op {ret[0]}'))
    await bot.send_message(message.from_user.id, text='Детали - нажми что бы узнать время', reply_markup=keyboard)


async def get_time_operation(callback_query, detail):
    text_massage = ''
    await bot.send_message(callback_query.from_user.id, detail)

    ret = cur.execute('''SELECT "номер операции", "время от БТЗ" 
                            FROM details_operation 
                            WHERE Деталь = ? AND "время от БТЗ" IS NOT NULL''', (detail,)).fetchall()
    for i in ret:
        text_massage += f'Оп {i[0]} - {i[1]} мин. \n'
    await bot.send_message(callback_query.from_user.id, text=text_massage)
