from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def food_keyboard(all_titles: list[str]) -> ReplyKeyboardMarkup:
    rows = [KeyboardButton(text=item) for item in all_titles]
    return ReplyKeyboardMarkup(keyboard=[rows], resize_keyboard=True)