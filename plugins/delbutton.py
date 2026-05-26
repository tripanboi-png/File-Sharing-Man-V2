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


@Client.on_message(filters.command("delbutton") & filters.user(ADMINS))
async def del_button(client, message: Message):

    if len(message.command) < 2:
        return await message.reply_text(
            "Usage:\n/delbutton Nama"
        )

    name = message.command[1]

    buttons = load_buttons()

    new_buttons = []

    deleted = False

    for x in buttons:

        if x["name"] != name:
            new_buttons.append(x)
        else:
            deleted = True

    save_buttons(new_buttons)

    if deleted:
        await message.reply_text(
            f"❌ Button {name} berhasil dihapus"
        )
    else:
        await message.reply_text(
            "Button tidak ditemukan."
        )
