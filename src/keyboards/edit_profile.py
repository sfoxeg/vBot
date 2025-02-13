from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def edit_profile_kb():
    buttons = [
        [InlineKeyboardButton(text="Задать имя", callback_data="edit_name")],
        [
            InlineKeyboardButton(text="Задать пол", callback_data="edit_gender"),
            InlineKeyboardButton(text="Задать возраст", callback_data="edit_age"),
        ],
        [InlineKeyboardButton(text="Пару слов о себе", callback_data="edit_desc")],
        [InlineKeyboardButton(text="Сменить фото", callback_data="edit_photo")],
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard
