from src.bot import bot


async def send_message(chat_id, text):
    await bot.send_message(chat_id=chat_id, text=text)
