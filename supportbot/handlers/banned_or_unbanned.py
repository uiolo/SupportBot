from aiogram import Router
from aiogram.filters.chat_member_updated import ChatMemberUpdatedFilter, IS_ADMIN, IS_MEMBER, KICKED, PROMOTED_TRANSITION
from aiogram.types import ChatMemberUpdated

from db.commands import delete_user_from_db, add_user_to_db


router = Router()


@router.my_chat_member(
    ChatMemberUpdatedFilter(member_status_changed=PROMOTED_TRANSITION)
)
async def kicked_by_admin(event: ChatMemberUpdated):
    print(event.from_user.id, 'become admin!\n', event)


@router.my_chat_member(
    ChatMemberUpdatedFilter(member_status_changed=~PROMOTED_TRANSITION)
)
async def kicked_by_admin(event: ChatMemberUpdated):
    print(event.from_user.id, 'become not an admin!\n', event)


@router.my_chat_member(
    ChatMemberUpdatedFilter(member_status_changed=KICKED)
)
async def on_block_bot(event: ChatMemberUpdated, connection):
    delete_user_from_db(
        user=event.from_user,
        connection=connection
    )


@router.my_chat_member(
    ChatMemberUpdatedFilter(member_status_changed=IS_MEMBER)
)
async def on_unblock_bot(event: ChatMemberUpdated, connection):
    add_user_to_db(
        user=event.from_user,
        connection=connection
    )