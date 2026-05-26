from pyrogram import Client, filters
from plugins.check_admin import is_admin
from database.mongo import get_admins


@Client.on_message(filters.command("getadmin") & filters.create(is_admin))
async def get_admin_list(client, message):

    admins = await get_admins()

    if not admins:
        return await message.reply_text("Tidak ada admin.")

    text = "📋 LIST ADMIN\n\n"

    for admin in admins:
        text += f"• <code>{admin}</code>\n"

    await message.reply_text(text)
