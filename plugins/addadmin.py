from pyrogram import Client, filters

@Client.on_message(filters.command("addadmin"))
async def add_admin_command(client, message):
    await message.reply_text("ADDADMIN TERPANGGIL")
