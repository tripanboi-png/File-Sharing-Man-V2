# Heroku Config Manager Safe Version

import os
import socket
import dotenv
import heroku3
import urllib3

from bot import Bot
from config import ADMINS, HEROKU_API_KEY, HEROKU_APP_NAME
from pyrogram import filters
from pyrogram.types import Message

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

if HEROKU_APP_NAME and HEROKU_API_KEY:
    Heroku = heroku3.from_key(HEROKU_API_KEY)
    HAPP = Heroku.app(HEROKU_APP_NAME)
else:
    HAPP = None


async def is_heroku():
    return "heroku" in socket.getfqdn()


@Bot.on_message(filters.command("getvar") & filters.user(ADMINS))
async def get_var(client: Bot, message: Message):
    if len(message.command) != 2:
        return await message.reply_text(
            "<b>Usage:</b>\n/getvar [VAR_NAME]"
        )

    var_name = message.command[1]

    if await is_heroku():
        if HAPP is None:
            return await message.reply_text(
                "HEROKU_API_KEY atau HEROKU_APP_NAME belum diatur."
            )

        config = HAPP.config()

        if var_name in config:
            return await message.reply_text(
                f"<b>{var_name}:</b>\n<code>{config[var_name]}</code>"
            )

        return await message.reply_text("Variable tidak ditemukan.")

    else:
        path = dotenv.find_dotenv("config.env")

        if not path:
            return await message.reply_text("config.env tidak ditemukan.")

        value = dotenv.get_key(path, var_name)

        if value:
            await message.reply_text(
                f"<b>{var_name}:</b>\n<code>{value}</code>"
            )
        else:
            await message.reply_text("Variable tidak ditemukan.")


@Bot.on_message(filters.command("setvar") & filters.user(ADMINS))
async def set_var(client: Bot, message: Message):
    if len(message.command) < 3:
        return await message.reply_text(
            "<b>Usage:</b>\n/setvar [VAR_NAME] [VALUE]"
        )

    var_name = message.command[1]
    value = message.text.split(None, 2)[2]

    if await is_heroku():
        if HAPP is None:
            return await message.reply_text(
                "HEROKU_API_KEY atau HEROKU_APP_NAME belum diatur."
            )

        config = HAPP.config()
        config[var_name] = value

        await message.reply_text(
            f"Berhasil mengatur:\n<b>{var_name}</b>"
        )

    else:
        path = dotenv.find_dotenv("config.env")

        if not path:
            return await message.reply_text("config.env tidak ditemukan.")

        dotenv.set_key(path, var_name, value)

        await message.reply_text(
            f"Berhasil mengatur:\n<b>{var_name}</b>"
        )

        os.system(f"kill -9 {os.getpid()} && bash start")


@Bot.on_message(filters.command("delvar") & filters.user(ADMINS))
async def del_var(client: Bot, message: Message):
    if len(message.command) != 2:
        return await message.reply_text(
            "<b>Usage:</b>\n/delvar [VAR_NAME]"
        )

    var_name = message.command[1]

    if await is_heroku():
        if HAPP is None:
            return await message.reply_text(
                "HEROKU_API_KEY atau HEROKU_APP_NAME belum diatur."
            )

        config = HAPP.config()

        if var_name in config:
            del config[var_name]
            return await message.reply_text(
                f"Berhasil menghapus:\n<b>{var_name}</b>"
            )

        return await message.reply_text("Variable tidak ditemukan.")

    else:
        path = dotenv.find_dotenv("config.env")

        if not path:
            return await message.reply_text("config.env tidak ditemukan.")

        dotenv.unset_key(path, var_name)

        await message.reply_text(
            f"Berhasil menghapus:\n<b>{var_name}</b>"
        )

        os.system(f"kill -9 {os.getpid()} && bash start")
