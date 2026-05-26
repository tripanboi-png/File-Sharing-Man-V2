from pyrogram import Client, filters
from pyrogram.types import Message

from config import ADMINS


@Client.on_message(filters.command("admin") & filters.user(ADMINS))
async def admin_menu(client, message: Message):
    text = """
<b>⚙️ MENU ADMIN V2 ⚙️</b>

/ping - cek bot
/users - cek users
/broadcast - broadcast pesan
/genlink - buat link file
/batch - buat link banyak file

🔥 V2 ACTIVE
"""

    await message.reply_text(text)
