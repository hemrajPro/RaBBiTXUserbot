from pyrogram import *
from pyrogram import filters
from pyrogram.types import *
from config import HANDLER as cmd
from bunny.core.clients import bunny as Client

@Client.on_message(filters.command(["save"], cmd) & filters.me)
async def save_message(client: Client, message: Message):
    if message.reply_to_message:
        saved_message = message.reply_to_message
        await client.set_value("saved_message", saved_message)
        await message.edit_text("Message saved successfully!")
    else:
        await message.edit_text("Please reply to a message to save it.")

@Client.on_message(filters.command(["forward"], cmd) & filters.me)
async def forward_saved_message(client: Client, message: Message):
    saved_message = await client.get_value("saved_message")
    if saved_message:
        await saved_message.forward(message.chat.id)
    else:
        await message.edit_text("No message saved.")
