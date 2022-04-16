from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def kb1b(txt, cd):
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=txt, callback_data=cd)
            ]
        ]
    )
    return kb
