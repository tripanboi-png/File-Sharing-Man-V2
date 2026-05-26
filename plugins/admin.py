from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from plugins.check_admin import is_admin


@Client.on_message(filters.command("admin") & filters.create(is_admin))
async def admin_menu(client, message):

    text = f"""
<b>⚡ MENU ADMIN ⚡</b>

<code>/users</code> - cek total users
<code>/broadcast</code> - broadcast pesan
<code>/ping</code> - cek speed bot
<code>/uptime</code> - cek uptime

<code>/batch</code> - buat link banyak file
<code>/genlink</code> - buat link 1 file

<code>/logs</code> - lihat logs
<code>/restart</code> - restart bot
"""

    btn = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "🔥 CHANNEL", url="https://t.me/USERNAMECHANNEL"
                )
            ],
            [
                InlineKeyboardButton(
                    "❌ TUTUP", callback_data="close"
                )
            ]
        ]
    )

    await message.reply_text(
        text=text,
        reply_markup=btn,
        disable_web_page_preview=True
    )
