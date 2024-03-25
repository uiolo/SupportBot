from aiogram import Router
from aiogram.types import Message


router = Router()

@router.message()
async def send_to_admin(message: Message):
    pass