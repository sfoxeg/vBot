from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from keyboards.edit_gender import edit_gender_kb
from keyboards.edit_search_setting import edit_search_setting_kb
from user import user
from utils import extract_number

router = Router()

min_age = 0


class EditSearchSetting(StatesGroup):
    edit_gender = State()
    edit_age_min = State()
    edit_age_max = State()


@router.message(Command('search_setting'))
async def edit_profile(message: Message):
    user.get_profile(str(message.from_user.id))
    if user.search_gender:
        gender = '🧔'
    else:
        gender = '👩'
    text = (f'Шукать: {gender}\n'
            f'В возрасте от {user.search_age_min} до {user.search_age_max}')
    await (message.answer(text=text, reply_markup=edit_search_setting_kb()))


@router.callback_query(F.data == "edit_search_gender")
async def edit_gender_cmd(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text=f"Не пойму, ты вообще кто?", reply_markup=edit_gender_kb('search'))
    await state.set_state(EditSearchSetting.edit_gender)
    await callback.answer()


@router.callback_query(EditSearchSetting.edit_gender,
                       (F.data.lower().contains('search_m')) |
                       (F.data.lower().contains('search_f')))
async def gender(callback: CallbackQuery):
    await callback.message.answer(text="Спасибо")
    user.get_profile(str(callback.from_user.id))
    if callback.data.lower() == 'search_m':
        user.search_gender = True
    elif callback.data.lower() == 'search_f':
        user.search_gender = False
    user.update_search_setting()
    await callback.answer()


@router.callback_query(F.data == "age_min")
async def edit_age_min_cmd(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text="Минимальный возраст")
    await state.set_state(EditSearchSetting.edit_age_min)
    await callback.answer()


@router.message(EditSearchSetting.edit_age_min, F.text)
async def edit_age_min(message: Message, state: FSMContext):
    check_age = extract_number(message.text)
    user.get_profile(str(message.from_user.id))

    if not check_age or not (18 <= int(message.text) <= 100):
        await message.reply("Пожалуйста, введите корректный возраст (число от 18 до 100).")
        return

    user.search_age_min = int(message.text)
    if user.search_age_max is None:
        user.update_search_setting()
    else:
        if user.search_age_min < user.search_age_max:
            user.update_search_setting()
        else:
            await message.reply('Хуйло криворукое')
            return

    await state.update_data(age=check_age)
    await message.answer('Збс')


@router.callback_query(F.data == "age_max")
async def edit_age_max_cmd(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text="Максимальный возраст")
    await state.set_state(EditSearchSetting.edit_age_max)
    await callback.answer()


@router.message(EditSearchSetting.edit_age_max, F.text)
async def edit_age_max(message: Message, state: FSMContext):
    check_age = extract_number(message.text)
    user.get_profile(str(message.from_user.id))

    if user.search_age_min is None:
        min_age = 18
    else:
        min_age = user.search_age_min

    if not check_age or not (min_age <= int(message.text) <= 100):
        await message.reply(f"Пожалуйста, введите корректный возраст (число от {min_age} до 100).")
        return

    user.search_age_max = int(message.text)
    user.update_search_setting()
    await state.update_data(age=check_age)
    await message.answer('Збс')
