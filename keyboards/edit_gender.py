from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def edit_gender_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.add(InlineKeyboardButton(text="М", callback_data="m"))
    kb.add(InlineKeyboardButton(text="Ж", callback_data="f"))
    return kb.as_markup()