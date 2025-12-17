from aiogram import types

from keyboards.reply import start_keyboard


async def start_handler(message: types.Message):
    await message.answer(
        "Добро пожаловать в квиз!",
        reply_markup=start_keyboard()
    )
