from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def sizes_keyboard(all_sizes: list[str]) -> ReplyKeyboardMarkup:
    rows = [[KeyboardButton(text=item)] for item in all_sizes]
    cancel_button = KeyboardButton(text='Cancel ❌')
    rows.insert(0, [cancel_button])
    return ReplyKeyboardMarkup(keyboard=rows, resize_keyboard=True)