import json

from pyrogram import Client, filters
from config import ADMINS

ADMIN_FILE = "admins.json"


def load_admins():
    with open(ADMIN_FILE, "r") as f:
        return json.load(f)


@Client.on_message(filters.command("getadmin") & filters.user(ADMINS))
async def get_admin(client, message):

    admins = load_admins()

    if not admins:
        return await message.reply_text(
            "Belum ada admin tambahan."
        )

    text = "📋 LIST ADMIN\n\n"

    for admin in admins:
        text += f"• <code>{admin}</code>\n"

    await message.reply_text(text)
