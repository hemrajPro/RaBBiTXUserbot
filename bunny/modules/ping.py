from pyrogram import Client, filters
from bunny.core.clients import bunny as Client

@Client.on_message(filters.command("ping", prefixes=".") & filters.me)
async def ping(client, message):
    await message.edit("Pong!")
