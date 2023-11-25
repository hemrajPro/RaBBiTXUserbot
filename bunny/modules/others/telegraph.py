from pyrogram import Client, filters
from pyrogram.types import Message
from telegraph import Telegraph, exceptions, upload_file
from config import HANDLER as hl
from bunny.helpers.basic import edit_or_reply, get_text
from bunny.helpers.tools import *
from bunny.core.clients import bunny as Client

telegraph = Telegraph()
r = telegraph.create_account(short_name="PyroMan-Userbot")
auth_url = r["auth_url"]


@Client.on_message(filters.command(["tgm", "telegraph"], hl) & filters.me)
async def uptotelegraph(client: Client, message: Message):
    bunny = await edit_or_reply(message, "`ρɾσƈҽʂʂιɳɠ...⚡`")
    if not message.reply_to_message:
        await bunny.edit(
            "**__reply to the message, to get a link from Telegraph....__**"
        )
        return
    if message.reply_to_message.media:
        if message.reply_to_message.sticker:
            m_d = await convert_to_image(message, client)
        else:
            m_d = await message.reply_to_message.download()
        try:
            media_url = upload_file(m_d)
        except exceptions.TelegraphException as exc:
            await bunny.edit(f"**ERROR:** `{exc}`")
            os.remove(m_d)
            return
        dones = (
            f"**๏ Successfully uploaded to** [Telegraph](https://telegra.ph/{media_url[0]})"
        )
        await bunny.edit(dones)
        os.remove(m_d)
    elif message.reply_to_message.text:
        page_title = get_text(message) if get_text(message) else client.me.first_name
        page_text = message.reply_to_message.text
        page_text = page_text.replace("\n", "<br>")
        try:
            response = telegraph.create_page(page_title, html_content=page_text)
        except exceptions.TelegraphException as exc:
            await bunny.edit(f"**ERROR:** `{exc}`")
            return
        geek = f"**๏ Successfully uploaded to** [Telegraph](https://telegra.ph/{response['path']})"
        await bunny.edit(geek)
