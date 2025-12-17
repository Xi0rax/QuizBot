from data.quiz_data import quiz_data
from db.database import (
    get_quiz_index,
    get_score,
    update_quiz_state
)

from services.quiz_service import get_question


async def right_answer(callback):
    user_id = callback.from_user.id

    index = await get_quiz_index(user_id)
    score = await get_score(user_id)

    await update_quiz_state(
        user_id,
        question_index=index + 1,
        score=score + 1
    )

    await callback.message.edit_reply_markup(None)
    await callback.message.answer("✅ Верно!")

    if index + 1 < len(quiz_data):
        await get_question(callback.message, user_id)
    else:
        await callback.message.answer(
            f"🎉 Квиз завершён!\n🏆 Результат: {score + 1} / {len(quiz_data)}"
        )


async def wrong_answer(callback):
    user_id = callback.from_user.id

    index = await get_quiz_index(user_id)
    score = await get_score(user_id)

    correct = quiz_data[index]["options"][quiz_data[index]["correct_option"]]

    await update_quiz_state(
        user_id,
        question_index=index + 1,
        score=score
    )

    await callback.message.edit_reply_markup(None)
    await callback.message.answer(
        f"❌ Неправильно\n✅ Правильный ответ: {correct}"
    )

    if index + 1 < len(quiz_data):
        await get_question(callback.message, user_id)
    else:
        await callback.message.answer(
            f"🎉 Квиз завершён!\n🏆 Результат: {score} / {len(quiz_data)}"
        )
