from datetime import datetime
from pyrogram import Client, enums, filters
from pyrogram.types import Message
from bunny.helpers.basic import edit_or_reply
from config import HANDLER as cmd
from bunny.core.clients import bunny as Client


@Client.on_message(filters.command(["mystats", "mystatus"], cmd) & filters.me)
async def stats(client: Client, message: Message):
    Man = await edit_or_reply(message, "`ᴄᴏʟʟᴇᴄᴛɪɴɢ sᴛᴀᴛs...`")
    start = datetime.now()
    u = 0
    g = 0
    sg = 0
    c = 0
    b = 0
    a_chat = 0
    Meh = await client.get_me()
    async for dialog in client.get_dialogs():
        if dialog.chat.type == enums.ChatType.PRIVATE:
            u += 1
        elif dialog.chat.type == enums.ChatType.BOT:
            b += 1
        elif dialog.chat.type == enums.ChatType.GROUP:
            g += 1
        elif dialog.chat.type == enums.ChatType.SUPERGROUP:
            sg += 1
            user_s = await dialog.chat.get_member(int(Meh.id))
            if user_s.status in (
                enums.ChatMemberStatus.OWNER,
                enums.ChatMemberStatus.ADMINISTRATOR,
            ):
                a_chat += 1
        elif dialog.chat.type == enums.ChatType.CHANNEL:
            c += 1

    end = datetime.now()
    ms = (end - start).seconds
    await Man.edit_text(
        """
__** нєяє ιѕ уσυ ѕтαтѕ ву яαввιтχ**__

__**๏ `{}` ᴘʀɪᴠᴀᴛᴇ ᴍᴇssᴀɢᴇs.**__
__**๏ `{}` ɢʀᴏᴜᴘs.**__
__**๏ `{}` sᴜᴘᴇʀ ɢʀᴏᴜᴘs.**__
__**๏ `{}` ᴄʜᴀɴɴᴇʟs.**__
__**๏ `{}` ᴄʜᴀᴛs ᴜʀ ᴀᴅᴍɪɴ ɪɴ.**__
__**๏ `{}` ʙᴏᴛs.**__""".format(
            ms, u, g, sg, c, a_chat, b
        )
    )
