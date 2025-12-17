from aiogram import types


async def help_handler(message: types.Message):
    await message.answer(
        "ℹ️ <b>Помощь по боту</b>\n\n"
        "/start — запуск бота\n"
        "/quiz — начать квиз\n"
        "/stats — статистика игроков\n"
        "/help — помощь\n\n"
        "📌 Во время квиза выбирайте ответ с помощью кнопок.",
        parse_mode="HTML"
    )
