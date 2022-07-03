import os

from aiogram import types, Dispatcher
from data_base import sql_admin
from data_base.sql_admin import export_pandas
from loader import bot, dp


async def command(message: types.Message):
    await bot.send_message(message.from_user.id, 'обновлен')


#@bot.message_handler(content_types=['document'])
async def to_accept_xls(message):
    try:
        chat_id = message.chat.id


        file_info = await bot.get_file(message.document.file_id)
        downloaded_file = await bot.download_file(file_info.file_path)

        src = message.document.file_name
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file.getvalue())

        await bot.send_message(message.from_user.id, "Пожалуй, я сохраню это")
        export_pandas(src)
        await bot.send_message(message.from_user.id, "Обновил")

    except Exception as e:
        await bot.send_message(message.from_user.id, e)


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(to_accept_xls, content_types=['document'])
    dp.register_message_handler(command, commands=['up'])