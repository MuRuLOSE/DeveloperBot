import asyncio
from os import getenv
from dotenv import load_dotenv
from .utils import get_lang

from aiogram import Bot, Dispatcher, Router, types
# from aiogram.types import InlineQuery, InlineQueryResultArticle
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, BotCommand
from aiogram.filters import Command
# from aiogram.utils.markdown import hbold, hitalic, hcode, hlink, hpre, hstrikethrough, hunderline 
router = Router()

load_dotenv()

TOKEN = getenv("BOT_TOKEN")

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()
commands = [
    BotCommand(command="/start", description="Перезапустить бота"),
    BotCommand(command="/source", description="Получить ссылку на исходный код бота")
]
lang = {}


@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    user_lang = message.from_user.language_code
    strings = get_lang(user_lang)
    await message.answer(
        strings["start"].format(message.from_user.first_name)
    )

@router.message(Command(commands=["source"]))
async def source_cmd(message: Message) -> None:

    # Please, dont delete this command
    await message.answer(
        "<a href='https://github.com/MuRuLOSE/DeveloperBot'>GitHub</a>\n"
    )

@router.message()
async def get_query(message: Message) -> None:
    user_lang = message.from_user.language_code
    strings = get_lang(user_lang)
    query = lambda x: message.text.lower().startswith(x) 
    reply = message.reply_to_message

    if query("sticker") or query("стикер"):
        if reply:
            try:
                await message.reply(
                    strings["sticker"].format(reply.sticker.file_id)
                )
            except AttributeError:
                await message.reply(strings["no-sticker"])
        if not reply:
            await message.reply(strings["no-reply"])

    if query("message") or query("сообщение") or query("смс") or query("sms"):
        if reply:
            await message.reply(strings["sms"].format(reply))
        if not reply:
            await message.reply(strings["no-reply"])
    
    if query("text") or query("текст"):
        if reply:
            await message.reply(
                strings["text"].format(reply.html_text),
                parse_mode="MARKDOWN"
            )
        if not reply:
            await message.reply(strings["no-reply"])

    if query("myid"):
        await message.reply(strings["myid"].format(message.from_user.id))

        
    

async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    # And the run events dispatching
    await bot.set_my_commands(commands=commands)
    dp.include_router(router=router)
    await dp.start_polling(bot)
    


if __name__ == "__main__":
    asyncio.run(main())