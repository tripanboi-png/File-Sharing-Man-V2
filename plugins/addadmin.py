from pyrogram import Client, filters
from plugins.check_admin import is_admin
from database.mongo import add_admin


@Client.on_message(filters.command("addadmin") & filters.create(is_admin))
async def add_admin_command(client, message):

    if len(message.command) < 2:
        return await message.reply_text(
            "Usage:\n/addadmin user_id"
        )

    try:
        user_id = int(message.command[1])
    except ValueError:
        return await message.reply_text(
            "❌ User ID tidak valid"
        )

    await add_admin(user_id)

    await message.reply_text(
        f"✅ Admin berhasil ditambahkan\n\nID: <code>{user_id}</code>"
    )
