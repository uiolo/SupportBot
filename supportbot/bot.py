from redis.asyncio.client import Redis
from psycopg2 import connect
import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage

from handlers import (
    my_id,
    start,
    on_edited,
    banned_or_unbanned,
    incorrect_messages,
    ban,
    order_food,
)

from config_reader import config


async def main():
    connection = connect(
        host=config.db_host,
        user=config.db_user,
        password=config.db_password.get_secret_value(),
        database=config.db_name,
    )

    bot = Bot(config.bot_token.get_secret_value())

    admins = await bot.get_chat_administrators(chat_id=config.main_chat_id)
    admins_ids = [admin.user.id for admin in admins]

    dp = Dispatcher(
        storage=RedisStorage(Redis()), connection=connection, admins=admins_ids
    )

    dp.include_routers(
        start.router,
        banned_or_unbanned.router,
        order_food.router,
        on_edited.router,
        my_id.router,
        ban.router,
        # incorrect_messages must be the last because he recieve all messages without filter
        incorrect_messages.router,
    )

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(
        bot, allowed_updates=["my_chat_member", "message", "callback_query"]
    )

    return connection


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )
    try:
        connection = asyncio.run(main())
    except KeyboardInterrupt:
        print("Finished.")
    finally:
        connection.close()
        print("Connection to database is closed.")
