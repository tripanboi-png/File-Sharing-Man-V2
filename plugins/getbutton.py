from pyrogram import Client, filters
from plugins.check_admin import is_admin
from database.mongo import get_buttons


@Client.on_message(filters.command("getbutton") & filters.create(is_admin))
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
