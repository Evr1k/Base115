from aiogram import types, Dispatcher
from loader import bot
from keyboards import kb_client
from data_base import sql_db


async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'get start!!!', reply_markup=kb_client)


async def get_head_details(message: types.Message):
    """ Запрос в базу данных на получение списка деталей по голове чертежа """
    await sql_db.get_head_details(message)


async def get_all_head_detail(callback_query: types.CallbackQuery):
    """ Запрос в базу данных на получение списка времени на операцию детали - details из сообщения пользователя """
    head_detail = callback_query.data.replace('head_detail ', '')
    await sql_db.get_all_detail_head(callback_query, head_detail)


async def get_time_detail(callback_query: types.CallbackQuery):
    """ Запрос в базу данных на получение списка времени на операцию детали - details из сообщения пользователя """
    detail = callback_query.data.replace('detail_op_time ', '')
    await sql_db.get_time_operation(callback_query, detail)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(get_head_details, commands=['Детали'])
    dp.register_callback_query_handler(get_all_head_detail, lambda x: x.data and x.data.startswith('head_detail '))
    dp.register_callback_query_handler(get_time_detail, lambda x: x.data and x.data.startswith('detail_op_time '))
