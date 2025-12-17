from data.quiz_data import quiz_data
from db.database import get_quiz_index, update_quiz_state
from keyboards.inline import quiz_keyboard


async def new_quiz(message):
    user_id = message.from_user.id
    await update_quiz_state(user_id, question_index=0, score=0)
    await get_question(message, user_id)


async def get_question(message, user_id: int):
    index = await get_quiz_index(user_id)
    question = quiz_data[index]
    correct = question["options"][question["correct_option"]]

    await message.answer(
        question["question"],
        reply_markup=quiz_keyboard(question["options"], correct)
    )
