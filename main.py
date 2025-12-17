import asyncio
import logging
from aiogram import Bot, Dispatcher, F

from config import API_TOKEN
from db.database import create_table
from handlers.start import start_handler
from handlers.quiz import quiz_handler
from handlers.callbacks import right_answer, wrong_answer
from handlers.stats import stats_handler
from handlers.help import help_handler

logging.basicConfig(level=logging.INFO)


async def main():
    bot = Bot(token=API_TOKEN)
    dp = Dispatcher()

    dp.message.register(start_handler, F.text == "/start")
    dp.message.register(quiz_handler, F.text == "Начать игру")
    dp.message.register(quiz_handler, F.text == "/quiz")
    dp.message.register(stats_handler, F.text == "/stats")
    dp.message.register(stats_handler, F.text == "Статистика")
    dp.message.register(help_handler, F.text == "/help")
    dp.message.register(help_handler, F.text == "Помощь")



    dp.callback_query.register(right_answer, F.data == "right_answer")
    dp.callback_query.register(wrong_answer, F.data == "wrong_answer")

    await create_table()
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
