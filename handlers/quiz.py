from aiogram import types

from services.quiz_service import new_quiz


async def quiz_handler(message: types.Message):
    await message.answer("Давайте начнем квиз!")
    await new_quiz(message)
