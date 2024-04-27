import os
import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from dotenv import load_dotenv
from keyboard import kb, ikb, buy_ikb

from commad import commands

BOT_TOKEN1 = os.getenv('BOT_TOKEN1')


# bot = Bot(token=BOT_TOKEN1)
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer("Assalomu Aleykum!\n Do'konimizga xush kelibsiz!\n"
                         "Iltimos ro'yxatdan o'ting /registration", reply_markup=kb)


@dp.message(Command('products'))
async def cmd_products(message: types.Message):
    await message.answer("Mahsulotlarni boshqarish!", reply_markup=ikb)


# async def main():
#     await  .set_my_commands(commands=commands)
#     await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
