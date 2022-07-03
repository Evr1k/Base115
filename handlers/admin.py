from aiogram import types, Dispatcher
from data_base import sql_admin



@bot.message_handler(content_types=['document'])
def to_accept_xls(message):
    try:
        chat_id = message.chat.id

        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        src = "E:/Base115/data/files/" + message.document.file_name
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)

        bot.reply_to(message, "Пожалуй, я сохраню это")
        export_pandas(scr)
        bot.reply_to(message, "Обновил")

    except Exception as e:
        bot.reply_to(message, e)

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(to_accept_xls, content_types=['document'])