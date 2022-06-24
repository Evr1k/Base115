from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


details_button = KeyboardButton('/Детали')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client.add(details_button)
