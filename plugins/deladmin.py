import json

from pyrogram import Client, filters
from pyrogram.types import Message
from config import ADMINS

ADMIN_FILE = "admins.json"


def load_admins():
    with open(ADMIN_FILE, "r") as f:
        return json.load(f)


def save_admins(admins):
    with open(ADMIN_FILE, "w") as f:
        json.dump(admins, f)


@Client.on_message(filters.command("deladmin") & filters.user(ADMINS))
async def del_admin(client, message: Message):

    if len(message.command) < 2:
        return await message.reply_text(
            "Usage:\n/deladmin user_id"
        )

    user_id = int(message.command[1])

    admins = load_admins()

    if user_id not in admins:
        return await message.reply_text(
            "User bukan admin."
        )

    admins.remove(user_id)
    save_admins(admins)

    await message.reply_text(
        f"❌ Admin berhasil dihapus\n\nID: <code>{user_id}</code>"
    )
