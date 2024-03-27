from aiogram.fsm.state import StatesGroup, State


class OrderFood(StatesGroup):
    choosing_food_title = State()
    choosing_food_size = State()