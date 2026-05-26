from pyrogram import Client, filters
from config import ADMINS
from database.mongo import get_buttons


@Client.on_message(filters.command("getbutton") & filters.user(ADMINS))
async def get_button_command(client, message):

    buttons = await get_buttons()

    if not buttons:
        return await message.reply_text(
            "Tidak ada button."
        )

    text = "📋 LIST BUTTON\n\n"

    for button in buttons:

        text += (
            f"• {button['name']}\n"
            f"{button['url']}\n\n"
        )

    await message.reply_text(text)
