import sqlite3 as sq
from loader import bot


def sql_start():
    global base, cur
    base = sq.connect('data/database.db')
    cur = base.cursor()
    if base:
        print('Data base connected - OK')


async def get_all_details(message):
    for ret in cur.execute('SELECT DISTINCT Деталь FROM details_operation').fetchall():
        await bot.send_message(message.from_user.id, *ret)


async def get_time_operation(message):
    for ret in cur.execute(
            'SELECT "номер операции", "время от БТЗ"  FROM details_operation WHERE Деталь = "148.40.301" AND "время от БТЗ" IS NOT NULL').fetchall():
        await bot.send_message(message.from_user.id, f'Операция {ret[0]} - {ret[1]} минут')
