from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types


def quiz_keyboard(options: list, correct_option: str):
    builder = InlineKeyboardBuilder()

    for option in options:
        builder.add(
            types.InlineKeyboardButton(
                text=option,
                callback_data="right_answer" if option == correct_option else "wrong_answer"
            )
        )

    builder.adjust(1)
    return builder.as_markup()
