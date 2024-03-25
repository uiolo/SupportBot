from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart


router = Router()

@router.message(CommandStart())
async def send_user_id(message: Message):
    await message.answer(f'Write what should i send to the admin.')