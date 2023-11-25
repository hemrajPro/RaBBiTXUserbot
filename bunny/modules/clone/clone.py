from config import HANDLER as hl
from pyrogram import Client, filters
from bunny.Database.clonedb import *
import os
from bunny.core.clients import bunny as Client
from bunny.helpers.tools import get_arg


@Client.on_message(filters.command("clone", hl))
async def cloner(_, m):
    try:
        id, args = await get_arg(_, m)
    except:
        return await m.edit(m, "Invalid User.")
    if not await details_exist():
        return await m.edit(m, f"Save your current details first by using ' `{hl}save` ', when you use revert, current details will be applied.")
    ok = await m.edit(m, "cloning...")
    user = await _.get_chat(id)
    dps = []
    async for y in _.get_chat_photos(id):
        dps.append(y.file_id)
    dp = dps[0]
    if user.bio:
        bio = user.bio
    else:
        bio = ""
    x = await _.send_photo("me", dp)
    dp = await x.download()
    await x.delete()
    try:
        await _.set_profile_photo(photo=dp)
    except:
        await _.set_profile_photo(video=dp)
    await _.update_profile(first_name=user.first_name, last_name=user.last_name if user.last_name else "", bio=bio)
    await ok.edit("Cloned successfully ✅")
    os.remove(dp)
    
@Client.on_message(filters.command("save", hl))
async def save(_, m):
    me = await _.get_chat((await my_info()).id)
    try:
        dps = []
        async for y in _.get_chat_photos(me.id):
            dps.append(y.file_id)
        dp_id = dps[0]
    except:
        dp_id = None
    details = {"first_name": me.first_name, "last_name": me.last_name if me.last_name else "", "bio": me.bio if me.bio else "", "file_id": dp_id}
    await save_details(details)
    await m.edit(m, "details saved successfully ✅")

@Client.on_message(filters.command("revert", hl))
async def revert(_, m):
    ok = await m.edit(m, "Reverting back...")
    details = await get_details()
    if details["file_id"]:
        x = await _.send_photo("me", details["file_id"])
        dp = await x.download()
        try:
            await _.set_profile_photo(photo=dp)
        except:
            await _.set_profile_photo(video=dp)
        await x.delete()
    await _.update_profile(first_name=details["first_name"], last_name=details["last_name"] if details["last_name"] else "", bio=details["bio"] if details["bio"] else "")
    await ok.edit("Reverted back ✅")
    os.remove(dp)
