from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def edit_search_setting_kb():
    buttons = [
        [InlineKeyboardButton(text="Задать пол", callback_data="edit_search_gender")],
        [
            InlineKeyboardButton(text="Возраст от", callback_data="age_min"),
            InlineKeyboardButton(text="Возраст до", callback_data="age_max"),
        ]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard
