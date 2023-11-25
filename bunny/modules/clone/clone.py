import os
from pyrogram import *
from pyrogram.types import *
from config import HANDLER as hl
from config import BIO
from bunny.helpers.basic import edit_or_reply, get_text, get_user
from bunny.core.clients import bunny as Client

OWNER = os.environ.get("OWNER", None)

@Client.on_message(filters.command("clone", cmd) & filters.me)
async def clone(client: Client, message: Message):
    text = get_text(message)
    bunny = await edit_or_reply(message, "`ƈℓσиιиg...⚡`")
    userk = get_user(message, text)[0]
    user_ = await client.get_users(userk)
    if not user_:
        await bunny.edit("`Decide who you want to clone...`")
        return

    get_bio = await client.get_chat(user_.id)
    f_name = user_.first_name
    c_bio = get_bio.bio
    pic = user_.photo.big_file_id
    poto = await client.download_media(pic)

    await client.set_profile_photo(photo=poto)
    await client.update_profile(
        first_name=f_name,
        bio=c_bio,
    )
    await message.edit(f"**__successfully cloned as__** __{f_name}__")


@Client.on_message(filters.command("revert", cmd) & filters.me)
async def revert(client: Client, message: Message):
    await message.edit("`яєνєятιиg...`")
    r_bio = BIO

    
    await client.update_profile(
        first_name=OWNER,
        bio=r_bio,
    )
    
    photos = [p async for p in client.get_chat_photos("me")]
    await client.delete_profile_photos(photos[0].file_id)
    await message.edit("**__I am back !!__**")
