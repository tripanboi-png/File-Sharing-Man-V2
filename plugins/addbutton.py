from pyrogram import Client, filters
from config import ADMINS
from database.mongo import add_button


@Client.on_message(filters.command("addbutton") & filters.user(ADMINS))
async def add_button_command(client, message):

    parts = message.text.split(maxsplit=2)

    if len(parts) < 3:
        return await message.reply_text(
            "Usage:\n/addbutton Nama https://t.me/link"
        )

    name = parts[1]
    url = parts[2]

    if not url.startswith("https://t.me/"):
        return await message.reply_text(
            "❌ Link harus format:\nhttps://t.me/username"
        )

    await add_button(name, url)

    await message.reply_text(
        f"✅ Button berhasil ditambahkan\n\n📌 Nama: {name}\n🔗 URL: {url}"
    )
