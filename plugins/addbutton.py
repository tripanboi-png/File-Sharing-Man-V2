import json

from pyrogram import Client, filters
from pyrogram.types import Message

from config import ADMINS

BUTTON_FILE = "buttons.json"


def load_buttons():
    with open(BUTTON_FILE, "r") as f:
        return json.load(f)


def save_buttons(buttons):
    with open(BUTTON_FILE, "w") as f:
        json.dump(buttons, f)


@Client.on_message(filters.command("addbutton") & filters.user(ADMINS))
async def add_button(client, message: Message):

    if len(message.command) < 3:
        return await message.reply_text(
            "Usage:\n/addbutton Nama https://t.me/link"
        )

    name = message.command[1]
    link = message.command[2]

    buttons = load_buttons()

    buttons.append({
        "name": name,
        "link": link
    })

    save_buttons(buttons)

    await message.reply_text(
        f"✅ Button berhasil ditambahkan\n\n{name}"
    )
