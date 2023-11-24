from pyrogram import Client, enums, filters
from pyrogram.types import Message
from config import BLACKLIST_CHAT
from config import HANDLER as cmd
from bunny.helpers.basic import edit_or_reply
from bunny.core.clients import bunny as Client


@Client.on_message(filters.command("join", cmd) & filters.me)
async def join(client: Client, message: Message):
    bunny = message.command[1] if len(message.command) > 1 else message.chat.id
    rabbit = await edit_or_reply(message, "`Processing...`")
    try:
        await rabbit.edit(f"**Successfully Joined ** `{bunny}` ⚡")
        await client.join_chat(bunny)
    except Exception as ex:
        await rabbit.edit(f"**ERROR:** \n\n{str(ex)}")


@Client.on_message(filters.command(["leave", "kickme"], cmd) & filters.me)
async def leave(client: Client, message: Message):
    bunny = message.command[1] if len(message.command) > 1 else message.chat.id
    rabbit = await edit_or_reply(message, "`Processing...`")
    if message.chat.id in BLACKLIST_CHAT:
        return await rabbit.edit("**__This command is not used in this group__**")
    try:
        await rabbit.edit_text(f"**__{client.me.first_name}  has left this group, bye bye 😪 !!**__")
        await client.leave_chat(bunny)
    except Exception as ex:
        await rabbit.edit_text(f"**ERROR:** \n\n{str(ex)}")


@Client.on_message(filters.command(["leaveallgc"], cmd) & filters.me)
async def kickmeall(client: Client, message: Message):
    bunny = await edit_or_reply(message, "`Leaving all group chats...⚡`")
    er = 0
    done = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type in (enums.ChatType.GROUP, enums.ChatType.SUPERGROUP):
            chat = dialog.chat.id
            try:
                done += 1
                await client.leave_chat(chat)
            except BaseException:
                er += 1
    await bunny.edit(
        f"__**๏ Successfully Leave {done} Group ⚡\n\n๏ Failed to Leave {er} Group ⚡**__"
    )


@Client.on_message(filters.command(["leaveallch"], cmd) & filters.me)
async def kickmeallch(client: Client, message: Message):
    bunny = await edit_or_reply(message, "`leaving all channels...⚡`")
    er = 0
    done = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type in (enums.ChatType.CHANNEL):
            chat = dialog.chat.id
            try:
                done += 1
                await client.leave_chat(chat)
            except BaseException:
                er += 1
    await bunny.edit(
        f"__**๏ Successfully Leave {done} channel ⚡\n\n๏ Failed to Leave {er} channel ⚡**__"
  )
