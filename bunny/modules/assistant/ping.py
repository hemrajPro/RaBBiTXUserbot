from pyrogram import Client, filters
from bunny.core.clients import bot as Client

@Client.on_message(filters.command("ping", prefixes="/"))
async def ping(_, message):
    await message.reply_text("Pong!")
