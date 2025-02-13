from config import BOT_TOKEN
from aiogram import Bot, Dispatcher
from handlers import start, profile


async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    dp.include_routers(start.router)
    dp.include_routers(profile.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
