import logging

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext

from db.commands import check_user_exists, add_user_to_db

router = Router()

@router.message(CommandStart())
async def start_cmd(message: Message, connection, state: FSMContext):
    await state.clear()
    if not check_user_exists(
        user=message.from_user,
        connection=connection
    ):
        add_user_to_db(
            user=message,
            connection=connection
        )
        logging.debug(f'User {message.from_user.id} added successfully')

    await message.answer(f'If you want to order food, please write: /food')