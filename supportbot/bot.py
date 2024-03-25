import asyncio
import logging
from aiogram import Bot, Dispatcher

from handlers import my_id, start, send_to_admin, on_edited
from config_reader import config

async def main():
    bot = Bot(config.bot_token.get_secret_value())
    dp = Dispatcher()
    dp.include_routers(
        start.router,
        on_edited.router,
        my_id.router,
        # recieve_message must be the last because he recieve all messages without filter
        send_to_admin.router, 
    )

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    asyncio.run(main())