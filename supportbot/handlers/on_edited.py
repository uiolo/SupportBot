from aiogram import Router, Bot
from aiogram.types import Message

from config_reader import config

router = Router()

@router.edited_message()
async def on_edited(message: Message, bot: Bot):
    # send to the admin all messages that have been edited
    await bot.edit_message_text(config.admins[0], text=message.text)