import json

from pyrogram import Client, filters

from config import ADMINS

BUTTON_FILE = "buttons.json"


def load_buttons():
    with open(BUTTON_FILE, "r") as f:
        return json.load(f)


@Client.on_message(filters.command("getbutton") & filters.user(ADMINS))
async def get_button(client, message):

    buttons = load_buttons()

    if not buttons:
        return await message.reply_text(
            "Belum ada button."
        )

    text = "📋 LIST BUTTON\n\n"

    for x in buttons:
        text += f"• {x['name']}\n{x['link']}\n\n"

    await message.reply_text(text)
