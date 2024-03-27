from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

from config_reader import config


router = Router()
# works only with current chat, not with other ones and not in private
router.message.filter(F.chat.id == config.main_chat_id)


@router.message(Command('ban'), F.reply_to_message)
async def ban_user(message: Message, admins: list[int]):
    # some actions to ban user
    await message.answer('User banned!')