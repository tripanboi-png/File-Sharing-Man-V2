from pyrogram import Client, filters
from config import ADMINS

admins = ADMINS.copy()

@Client.on_message(filters.command("getadmin") & filters.user(ADMINS))
async def get_admin(client, message):

    text = "📋 LIST ADMIN\n\n"

    for admin in admins:
        text += f"• <code>{admin}</code>\n"

    await message.reply_text(text)
