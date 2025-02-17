from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from keyboards.edit_gender import edit_gender_kb
from keyboards.edit_profile import edit_profile_kb
from user import user
from utils import extract_number

router = Router()


class EditProfile(StatesGroup):
    edit_name = State()
    edit_gender = State()
    edit_age = State()
    edit_desc = State()
    edit_photo = State()


@router.message(Command('profile'))
async def edit_profile(message: Message):
    user.get_profile(str(message.from_user.id))
    user.update_profile()

    if user.gender:
        gender = 'М'
    else:
        gender = 'Ж'

    text = (f"Имя: {user.name}\n"
            f"Пол: {gender}\n"
            f"Возраст: {user.age}\n"
            f"О себе: {user.desc}\n")

    if user.photo:
        await (message.answer_photo(photo=user.photo, caption=text, reply_markup=edit_profile_kb()))
    else:
        await (message.answer(text=text, reply_markup=edit_profile_kb()))


@router.callback_query(F.data == "edit_name")
async def edit_name_cmd(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text=f"Представьтесь")
    # Устанавливаем пользователю состояние
    await state.set_state(EditProfile.edit_name)
    await callback.answer()


@router.message(EditProfile.edit_name, F.text)
async def edit_name(message: Message):
    await message.answer(text="Спасибо")
    user.get_profile(str(message.from_user.id))
    user.name = message.text
    user.update_profile()


@router.callback_query(F.data == "edit_gender")
async def edit_gender_cmd(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text=f"Не пойму, ты вообще кто?", reply_markup=edit_gender_kb('profile'))
    await state.set_state(EditProfile.edit_gender)
    await callback.answer()


@router.callback_query(EditProfile.edit_gender,
                       (F.data.lower().contains('profile_m')) |
                       (F.data.lower().contains('profile_f')))
async def gender(callback: CallbackQuery):
    await callback.message.answer(text="Спасибо")
    user.get_profile(str(callback.from_user.id))
    if callback.data.lower() == 'profile_m':
        user.gender = True
    elif callback.data.lower() == 'profile_f':
        user.gender = False
    user.update_profile()
    await callback.answer()


@router.callback_query(F.data == "edit_desc")
async def edit_desc_cmd(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text=f"Поясни за базар")
    await state.set_state(EditProfile.edit_desc)
    await callback.answer()


@router.message(EditProfile.edit_desc, F.text)
async def edit_desc(message: Message):
    await message.answer(text="Спасибо")
    user.get_profile(str(message.from_user.id))
    user.desc = message.text
    user.update_profile()


@router.callback_query(F.data == "edit_age")
async def edit_age_cmd(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text=f"У тя сколько ходок, фраерок?")
    await state.set_state(EditProfile.edit_age)
    await callback.answer()


@router.message(EditProfile.edit_age, F.text)
async def edit_age(message: Message, state: FSMContext):
    check_age = extract_number(message.text)

    if not check_age or not (18 <= int(message.text) <= 100):
        await message.reply("Пожалуйста, введите корректный возраст (число от 18 до 100).")
        return

    user.get_profile(str(message.from_user.id))
    user.age = int(message.text)
    user.update_profile()
    await state.update_data(age=check_age)
    await message.answer('Збс')


@router.callback_query(F.data == "edit_photo")
async def edit_photo_cmd(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text=f"Ебани дикпик")
    await state.set_state(EditProfile.edit_photo)
    await callback.answer()


@router.message(EditProfile.edit_photo, F.photo)
async def get_photo(message: Message):
    user.get_profile(str(message.from_user.id))
    user.photo = str(message.photo[-1].file_id)
    user.update_profile()
