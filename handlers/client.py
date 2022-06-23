from aiogram import types, Dispatcher
from loader import bot
from keyboards import kb_client
from data_base import sql_db

async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'get start!!!', reply_markup=kb_client)

async  def get_details(message: types.Message):
    await sql_db.get_all_details(message)


async  def get_time_detail(message: types.Message):
    await sql_db.get_time_operation(message)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(get_details, commands=['Детали'])
    dp.register_message_handler(get_time_detail, commands=['40.301'])
    # dp.register_message_handler(echo_send)
    # dp.register_message_handler(get_machine_time, commands=['start', 'help'])
