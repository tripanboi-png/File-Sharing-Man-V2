from pyrogram import Client, filters
from config import ADMINS
from database.mongo import remove_admin


@Client.on_message(filters.command("deladmin") & filters.user(ADMINS))
async def del_admin_command(client, message):

    if len(message.command) < 2:
        return await message.reply_text(
            "Usage:\n/deladmin user_id"
        )

    user_id = int(message.command[1])

    if user_id in ADMINS:
        ADMINS.remove(user_id)

    await remove_admin(user_id)

    await message.reply_text(
        f"❌ Admin berhasil dihapus\n\nID: <code>{user_id}</code>"
    )
