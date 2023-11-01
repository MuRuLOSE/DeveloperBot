import asyncio
import logging
import sys
from os import getenv, path
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, Router, types
# from aiogram.types import InlineQuery, InlineQueryResultArticle
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
# from aiogram.utils.markdown import hbold, hitalic, hcode, hlink, hpre, hstrikethrough, hunderline 

router = Router()

load_dotenv()

TOKEN = getenv("BOT_TOKEN")

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()


@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:

    await message.answer(
        f"Hello, <b>{message.from_user.first_name}</b>\n"
        "I'm an assistant to the developers\n"
        f"<i>only in Russian for now</i>"
    )

@router.message()
async def get_query(message: Message) -> None:
    query = lambda x: message.text.lower().startswith(x) 
    reply = message.reply_to_message

    if query("sticker") or query("стикер"):
        if reply:
            try:
                await message.reply(f"Айди стикера: <code>{reply.sticker.file_id}</code>")
            except AttributeError:
                await message.reply("Вы ответили НЕ НА СТИКЕР")
        if not reply:
            await message.reply("Вы не ответили на стикер / сообщение")

    if query("message") or query("сообщение") or query("смс"):
        if reply:
            await message.reply(f"Тело сообщения: \n<code>{reply}</code>")
        if not reply:
            await message.reply("Вы не ответили на стикер / сообщение")
    
    if query("text") or query("текст"):
        if reply:
            await message.reply(f"Текст: ```\n{reply.html_text}```",parse_mode="MARKDOWN")
        if not reply:
            await message.reply("Вы не ответили на стикер / сообщение")

        
    

async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    # And the run events dispatching
    dp.include_router(router=router)
    await dp.start_polling(bot)
    


if __name__ == "__main__":
    asyncio.run(main())