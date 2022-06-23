from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from data.config import TOKEN

bot = Bot(TOKEN)
dp = Dispatcher(bot)


async def on_startup():
    print('Бот вышел в онлайн')


if __name__ == '__main__':
    await executor.start_polling(dp, on_startup=on_startup())

executor.start_polling(dp, skip_updates=True)
