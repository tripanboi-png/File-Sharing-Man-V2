from pyrogram.types import InlineKeyboardButton
from database.mongo import get_buttons


async def start_button(client):

    buttons = []

    db_buttons = await get_buttons()

    row = []

    for button in db_buttons:

        try:

            url = str(button["url"]).strip()

            if not url.startswith("https://"):
                continue

            row.append(
                InlineKeyboardButton(
                    text=button["name"],
                    url=url
                )
            )

            if len(row) == 2:
                buttons.append(row)
                row = []

        except:
            continue

    if row:
        buttons.append(row)

    buttons.append(
        [
            InlineKeyboardButton(
                text="ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs",
                callback_data="help"
            )
        ]
    )

    buttons.append(
        [
            InlineKeyboardButton(
                text="ᴛᴜᴛᴜᴘ",
                callback_data="close"
            )
        ]
    )

    return buttons


async def fsub_button(client, message):

    buttons = []

    db_buttons = await get_buttons()

    row = []

    for button in db_buttons:

        try:

            url = str(button["url"]).strip()

            if not url.startswith("https://"):
                continue

            row.append(
                InlineKeyboardButton(
                    text=button["name"],
                    url=url
                )
            )

            if len(row) == 2:
                buttons.append(row)
                row = []

        except:
            continue

    if row:
        buttons.append(row)

    try:

        buttons.append(
            [
                InlineKeyboardButton(
                    text="🔄 COBA LAGI",
                    url=f"https://t.me/{client.username}?start={message.command[1]}"
                )
            ]
        )

    except:
        pass

    return buttons
