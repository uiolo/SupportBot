from aiogram import Router
from aiogram.types import Message


router = Router()


async def incorrect_messages(message: Message):
    await message.answer('Please, type /help to check all avaliable commands')