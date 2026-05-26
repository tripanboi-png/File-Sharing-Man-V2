from pyrogram import Client, filters
from pyrogram.types import Message
from config import ADMINS

admins = ADMINS.copy()

@Client.on_message(filters.command("addadmin") & filters.user(ADMINS))
async def add_admin(client, message: Message):

    if len(message.command) < 2:
        return await message.reply_text(
            "Usage:\n/addadmin user_id"
        )

    user_id = int(message.command[1])

    if user_id in admins:
        return await message.reply_text("Admin sudah ada.")

    admins.append(user_id)

    await message.reply_text(
        f"✅ Admin berhasil ditambahkan\n\nID: <code>{user_id}</code>"
    )
