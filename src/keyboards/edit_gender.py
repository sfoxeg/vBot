from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def edit_gender_kb(prefix) -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.add(InlineKeyboardButton(text="🧔", callback_data=f"{prefix}_m"))
    kb.add(InlineKeyboardButton(text="👩", callback_data=f"{prefix}_f"))
    return kb.as_markup()
