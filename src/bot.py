from config import BOT_TOKEN
from aiogram import Bot, Dispatcher
from handlers import start, profile, search_setting
from aiogram.types import BotCommand


async def setup_bot_commands():
    bot_commands = [
        BotCommand(command="/start", description="Нажми сюда и сможешь познать глубока ли кроличья нора"),
        BotCommand(command="/profile", description="Настройки профиля"),
        BotCommand(command="/search_setting", description="Настройки поиска"),
        BotCommand(command="/search", description="Удиви меня")
    ]
    await bot.set_my_commands(bot_commands)


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


async def main():
    dp.include_routers(start.router)
    dp.include_routers(profile.router)
    dp.include_routers(search_setting.router)

    await setup_bot_commands()
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

