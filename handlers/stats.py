from aiogram import types

from db.database import get_stats


async def stats_handler(message: types.Message):
    stats = await get_stats()

    if not stats:
        await message.answer("Статистика пока пуста.")
        return

    text = "📊 <b>Статистика игроков</b>\n\n"
    for i, (user_id, score) in enumerate(stats, start=1):
        text += f"{i}. ID {user_id} — {score} баллов\n"

    await message.answer(text, parse_mode="HTML")
