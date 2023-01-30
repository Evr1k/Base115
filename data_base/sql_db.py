import os
import sqlite3 as sq

from loader import bot
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def sql_start():
    """ Подключение к базе данных """
    global base, cur
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, 'database.db')
    base = sq.connect(db_path)
    cur = base.cursor()
    if base:
        print('Data base connected - OK')


def on_startup():
    print('Bot - online')
    sql_start()


async def get_head_details(message):
    """ Создает инлайн кнопки для всех деталей группируя по голове чертежа"""
    keyboard = InlineKeyboardMarkup(row_width=3, resize_keyboard=True)
    answer_bd = (str(i).split(".", 1)[0] for i in cur.execute('''SELECT DISTINCT Деталь 
                                                                FROM operation 
                                                                ORDER BY Деталь''').fetchall())
    for ret in set(answer_bd):
        keyboard.insert(InlineKeyboardButton(f'{ret[0]}..', callback_data=f'head_detail {ret[0]}'))
    await bot.send_message(message.from_user.id, text='Выберите голову чертежа детали', reply_markup=keyboard)


async def get_all_detail_head(callback_query, head_detail):
    """ Создает инлайн кнопки для всех деталей выбранной головы чертежа"""
    keyboard = InlineKeyboardMarkup(row_width=3, resize_keyboard=True)
    ret = cur.execute('''SELECT "номер операции", "название операции", "время по станку", "время по ТП", "расценка" 
                            FROM operation 
                            WHERE Деталь LIKE ?
                            ORDER BY Деталь''', (head_detail + "%",)).fetchall()
    for i in ret:
        keyboard.insert(InlineKeyboardButton(f'{ret[0]}..', callback_data=f'detail {ret[0]}'))
    await bot.send_message(callback_query.from_user.id, text='Выберите деталь', reply_markup=keyboard)


async def get_time_operation(callback_query, detail):
    """ Получает время на операцию и передает данные пользователю """
    text_massage = ''
    await bot.send_message(callback_query.from_user.id, detail)

    ret = cur.execute('''SELECT "номер операции", "название операции", "время по станку", "время по ТП", "расценка" 
                            FROM operation 
                            WHERE Деталь = ?
                            ORDER BY Деталь''', (detail,)).fetchall()
    for num_operation, name_operation, time_machine, time_tp, price in ret:
        if time_tp is not None:
            text_massage += f'Оп {num_operation} - {name_operation} - {time_tp} мин.- {price} руб. \n'
        elif time_tp is None and time_machine is not None:
            text_massage += f'Оп {num_operation} - {name_operation} - {time_machine} мин. - время со станка \n'
        else:
            text_massage += f'Оп {num_operation} - {name_operation} - не нормирована \n'
    await bot.send_message(callback_query.from_user.id, text=text_massage)
