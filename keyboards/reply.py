from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_main_keyboard():
    buttons = [
        [KeyboardButton(text="💰 Рассчитать чистую прибыль")],
        [KeyboardButton(text="🔍 Анализ цен приложений")]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)