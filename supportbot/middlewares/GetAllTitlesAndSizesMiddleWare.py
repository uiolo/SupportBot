from typing import Any, Awaitable, Callable, Dict
from aiogram.dispatcher.middlewares.base import BaseMiddleware
from aiogram.types import TelegramObject


from db.commands import get_all_titles, get_all_sizes

class GetAllTitlesAndSizesMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:
        all_titles = get_all_titles(
            connection=data['connection']
        )
        all_sizes = get_all_sizes(
            connection=data['connection']
        )
        if not all_titles:
            await event.answer("We actually don't have any food right now :(")
            return
        
        data['all_titles'] = all_titles
        data['all_sizes'] = all_sizes
        return await handler(event, data)
