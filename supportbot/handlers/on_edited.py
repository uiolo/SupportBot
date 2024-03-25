from aiogram import Router, Bot
from aiogram.types import Message
from aiogram.filters import Command

from config_reader import config

router = Router()

@router.edited_message()
async def on_edited(message: Message, bot: Bot):
    await bot.edit_message_text(config.admins[0], text=message.text)