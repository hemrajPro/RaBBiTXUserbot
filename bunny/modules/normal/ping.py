from pyrogram import Client, filters
from bunny import user as Client

@Client.on_message(filters.command("ping", prefixes=".") & filters.me)
async def ping(client, message):
    await message.edit("Pong!")
