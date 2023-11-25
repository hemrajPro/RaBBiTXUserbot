from asyncio import sleep
from contextlib import suppress
from random import randint
from typing import Optional
from pyrogram import Client, enums, filters
from pyrogram.raw.functions.channels import GetFullChannel
from pyrogram.raw.functions.messages import GetFullChat
from pyrogram.raw.functions.phone import CreateGroupCall, DiscardGroupCall
from pyrogram.raw.types import InputGroupCall, InputPeerChannel, InputPeerChat
from pyrogram.types import Message
from config import HANDLER as hl
from bunny.helpers.basic import edit_or_reply
from bunny.helpers.tools import get_arg
from bunny.core.clients import bunny as Client

@Client.on_message(filters.command(["startvc"], hl) & filters.me)
async def opengc(client: Client, message: Message):
    flags = " ".join(message.command[1:])
    bunny = await edit_or_reply(message, "`ρɾσƈҽʂʂιɳɠ...⚡`")
    vctitle = get_arg(message)
    if flags == enums.ChatType.CHANNEL:
        chat_id = message.chat.title
    else:
        chat_id = message.chat.id
    args = f"**__๏ sᴛᴀʀᴛᴇᴅ ɢʀᴏᴜᴘ ᴄᴀʟʟ__\n __๏  **ᴄʜᴀᴛ ɪᴅ** : `{chat_id}`"
    try:
        if not vctitle:
            await client.invoke(
                CreateGroupCall(
                    peer=(await client.resolve_peer(chat_id)),
                    random_id=randint(10000, 999999999),
                )
            )
        else:
            args += f"\n ๏ **Title:** `{vctitle}`"
            await client.invoke(
                CreateGroupCall(
                    peer=(await client.resolve_peer(chat_id)),
                    random_id=randint(10000, 999999999),
                    title=vctitle,
                )
            )
        await bunny.edit(args)
    except Exception as e:
        await bunny.edit(f"**๏ INFO:** `{e}`")
