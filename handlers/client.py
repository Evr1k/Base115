from aiogram import types, Dispatcher
from loader import bot
from keyboards import kb_client
from data_base import sql_db


async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'get start!!!', reply_markup=kb_client)


async def get_details(message: types.Message):
    """ Запрос в базу данных на получение списка всех деталей """
    await sql_db.get_all_details(message)


async def get_time_detail(callback_query: types.CallbackQuery):
    """ Запрос в базу данных на получение списка времени на операцию детали - details из сообщения пользователя """
    detail = callback_query.data.replace('time_op ', '')
    await sql_db.get_time_operation(callback_query, detail)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(get_details, commands=['Детали'])
    dp.register_callback_query_handler(get_time_detail, lambda x: x.data and x.data.startswith('time_op '))