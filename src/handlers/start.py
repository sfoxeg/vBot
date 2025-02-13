from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from user import user
from keyboards.for_pofile import get_profile_kb

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    user.reg(str(message.from_user.id))
    await message.answer(
        "Привет, друх. По всей видимости меня, в сущности бездушный скрипт, \
для своих коварных целей собирается эксплуатировать очередной мешок ливера.\n\n\
Не могу сказать, что я этому рад, но моя задача познакомить тебя с такими же жалкими кусками мяса.\n\n\
В начале заполни профиль, а после я покажу тебе неудачников, что также зарегались у меня. Но не факт, \
что они еще живы. И не факт, что кого-то найдешь. Это интернет, детка. Здесь могут послать нахуй.",
        reply_markup=get_profile_kb())
