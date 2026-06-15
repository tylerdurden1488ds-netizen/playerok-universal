import asyncio
import os
import sys
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from dotenv import load_dotenv

sys.stdout.reconfigure(encoding='utf-8')

# Загружаем настройки из .env
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = os.getenv("ADMIN_ID")

if not BOT_TOKEN:
    print("ОШИБКА: Забыли указать BOT_TOKEN в файле .env")
    sys.exit(1)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    if str(message.from_user.id) == str(ADMIN_ID):
        await message.answer("🤖 Бот Playerok успешно запущен на Python 3.12!")
    else:
        await message.answer("Доступ ограничен.")

async def main():
    print("🚀 Бот успешно собран и запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
