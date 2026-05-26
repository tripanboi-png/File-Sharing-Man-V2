from pyrogram import Client, filters

from config import ADMINS


@Client.on_message(filters.command("addadmin") & filters.user(ADMINS))
async def add_admin(client, message):

    if len(message.command) < 2:
        return await message.reply_text(
            "Usage:\n/addadmin user_id"
        )

    user_id = message.command[1]

    await message.reply_text(
        f"✅ Admin berhasil ditambahkan:\n<code>{user_id}</code>"
    )
