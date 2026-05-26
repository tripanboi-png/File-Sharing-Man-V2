from pyrogram import Client, filters
from plugins.check_admin import is_admin
from database.mongo import remove_button


@Client.on_message(filters.command("delbutton") & filters.create(is_admin))
async def del_button_command(client, message):

    if len(message.command) < 2:
        return await message.reply_text(
            "Usage:\n/delbutton NamaButton"
        )

    name = message.command[1]

    await remove_button(name)

    await message.reply_text(
        f"❌ Button berhasil dihapus\n\n{name}"
    )
