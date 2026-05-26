from pyrogram import Client, filters
from plugins.check_admin import is_admin
from database.mongo import add_button


@Client.on_message(filters.command("addbutton") & filters.create(is_admin))
async def add_button_command(client, message):

    if len(message.command) < 3:
        return await message.reply_text(
            "Usage:\n/addbutton Nama https://t.me/link"
        )

    name = message.command[1]
    url = message.command[2]

    await add_button(name, url)

    await message.reply_text(
        f"✅ Button berhasil ditambahkan\n\n{name}"
    )
