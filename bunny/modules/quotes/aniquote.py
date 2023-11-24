import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from config import HANDLER as cmd
from bunny.helpers.tools import get_arg
from bunny.core.clients import bunny as Client

@Client.on_message(filters.me & filters.command(["ani", "aniqu"], cmd))
async def quotly(client: Client, message: Message):
    args = get_arg(message)
    if not message.reply_to_message and not args:
        return await message.edit("**__ᴘʟᴇᴀsᴇ ʀᴇᴘʟʏ ᴛᴏ ᴛʜᴇ ᴍᴇssᴀɢᴇ...__!!**")
    bot = "QuotAfBot"
    if message.reply_to_message:
        await message.edit("**__ᴍᴀᴋɪɴɢ ᴀɴɪᴍᴀᴛᴇᴅ ǫᴜᴏᴛᴇ...**__")
        await client.unblock_user(bot)
        if args:
            await client.send_message(bot, f"/qcolor {args}")
            await asyncio.sleep(1)
        else:
            pass
        await message.reply_to_message.forward(bot)
        await asyncio.sleep(5)
        async for quotly in client.search_messages(bot, limit=1):
            if quotly:
                await message.delete()
                await message.reply_sticker(
                    sticker=quotly.sticker.file_id,
                    reply_to_message_id=message.reply_to_message.id
                    if message.reply_to_message
                    else None,
                )
            else:
                return await message.edit("**__ғᴀɪʟᴇᴅ ᴛᴏ ᴍᴀᴋᴇ sᴛɪᴄᴋᴇʀ ᴀɴɪᴍᴀᴛɪᴏɴ ǫᴜᴏᴛᴇ__**")
