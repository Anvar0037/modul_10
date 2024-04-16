from aiogram.filters import CommandStart, Command
from db_modul10 import get_all_product
from aiogram import Bot, Dispatcher, types
from config import BOT_TOKEN
import asyncio


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer("Hello")


@dp.message(Command("all_product"))
async def cmd_all_product(message: types.Message):
    products = get_all_product()
    if not products:
        await message.answer("Bizda mahsulotlar voxtinchalik mavjud emas")
    for i in products:
        await message.answer(i.title)


async def main():
    print("Bot started")
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
