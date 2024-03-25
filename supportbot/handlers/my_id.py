from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command


router = Router()

@router.message(Command('my_id'))
async def send_user_id(message: Message):
    await message.reply(f'Your id is {message.from_user.id}\nChat id: {message.chat.id}')