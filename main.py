from aiogram.utils import executor
from loader import dp
from handlers import client, admin
from data_base import sql_db


def on_startup():
    print('Bot - online')
    sql_db.sql_start()


client.register_handlers_client(dp)
admin.register_handlers_admin(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup())
