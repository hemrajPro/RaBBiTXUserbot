from pyrogram import Client, filters
from . import eor, hl, verify, add_command, get_id, capsify
from bunny.Database.pm import *
from .watchers import pm_watcher

KOWSHIK = "https://telegra.ph/file/d3de01a9f572f71841edf.jpg"

TEXT = """**๏ ʜᴇʏ** {}

**__๏ ᴛʜɪs ɪs  ᴘᴍ sᴇᴄᴜʀɪᴛʏ ᴏғ {}__**

**__๏ ʏᴏᴜ ᴍᴇssᴀɢᴇᴅ ʜᴇʀᴇ. ɴᴏᴡ ᴡʜᴇɴ ᴍʏ ᴍᴀsᴛᴇʀ ᴄᴏᴍᴇs ᴏɴʟɪɴᴇ, ʜᴇ ᴡɪʟʟ sᴇᴇ ʏᴏᴜʀ message ᴀɴᴅ ʀᴇᴘʟʏ ᴛᴏ ʏᴏᴜ.__**

**__๏ ᴅᴏɴ'ᴛ ᴍᴇssᴀɢᴇ ᴜɴᴛɪʟ ᴍʏ ᴍᴀsᴛᴇʀ ᴄᴏᴍᴇs ᴏɴʟɪɴᴇ ᴏᴛʜᴇʀᴡɪsᴇ ʏᴏᴜ ᴡɪʟʟ ʙᴇ ʙʟᴏᴄᴋᴇᴅ.__**

**__๏ ʏᴏᴜ ᴡɪʟʟ ʙᴇ ʙʟᴏᴄᴋᴇᴅ ᴀғᴛᴇʀ `{}` ᴡᴀʀɴs ʙᴇ ᴄᴀʀᴇғᴜʟ__**

__**๏ ʏᴏᴜʀ ᴡᴀʀɴs »**__ `{}`

**๏──────【[ᴛʜᴇ ʀᴀʙʙɪᴛx](https://t.me/S_T_F_U_09)】──────๏**
"""

@Client.on_message(filters.command("pmprotect", hl) & filters.me)
async def pmpro(_, m):
    x = await is_pm_on()
    try:
        tg = m.text.split()[1].lower()
    except:
        return await eor(m, f"{hl}pmprotect [on | off]")
    if not tg in ["on", "off"]:
        return await eor(m, f"{hl}pmprotect [on | off]")
    if tg == "on":
        if x:
            return await eor(m, capsify("ᴘᴍ ᴘʀᴏᴛᴇᴄᴛɪᴏɴ ᴀʟʀᴇᴀᴅʏ ᴇɴᴀʙʟᴇᴅ !"))
        await toggle_pm()
        if await limit() == 0:
            await update_warns(3)
        return await eor(m, capsify("ᴘᴍ ᴘʀᴏᴛᴇᴄᴛɪᴏɴ ᴇɴᴀʙʟᴇᴅ !"))
    if not x:
        return await eor(m, capsify("ᴘᴍ ᴘʀᴏᴛᴇᴄᴛɪᴏɴ ɪsɴ'ᴛ ᴇɴᴀʙʟᴇᴅ !"))
    await toggle_pm()
    return await eor(m, capsify("ᴘᴍ ᴘʀᴏᴛᴇᴄᴛɪᴏɴ ᴅɪsᴀʙʟᴇᴅ !"))

@Client.on_message(filters.command(["approve", "disapprove", "a", "da", "allow", "disallow"], hl) & filters.me)
async def appro_dis(_, m):
    if str(m.chat.id)[0] == "-":
        try:
            id = await get_id(_, m)
        except:
            return await eor(m, capsify("ʀᴇᴘʟʏ ᴏʀ ɢɪᴠᴇ ɪᴅ !"))
    else:
        id = m.chat.id
    tg = m.text.split()[0][1]
    x = await is_approved(id)
    if tg == "d":
        if not x:
            return await eor(m, capsify("ᴜsᴇʀ ᴡᴀsɴ'ᴛ ᴀᴘᴘʀᴏᴠᴇᴅ !"))
        await disapprove(id)
        return await eor(m, capsify("ᴅɪsᴀᴘᴘʀᴏᴠᴇᴅ ᴜsᴇʀ ᴛᴏ ᴘᴍ !"))
    if x:
        return await eor(m, capsify("ᴜsᴇʀ ᴀʟʀᴇᴀᴅʏ ᴀᴘᴘʀᴏᴠᴇᴅ !"))
    await approve(id) 
    await reset_warns(id)
    return await eor(m, capsify("ᴜsᴇʀ ᴀᴘᴘʀᴏᴠᴇᴅ ᴛᴏ ᴘᴍ !"))

@Client.on_message(filters.command("setwarns", hl) & filters.me)
async def setter(_, m):
    try:
        count = int(m.text.split()[1])
    except:
        return await eor(m, f"{hl}setwarns [value]")
    if count == 0:
        return await eor(m, capsify("ɢɪᴠᴇ ᴠᴀʟᴜᴇ ᴀʙᴏᴠᴇ 0 !"))
    await update_warns(count)
    await eor(m, capsify(f"ᴘᴍ ᴡᴀʀɴs sᴇᴛ ᴛᴏ {count} !"))
    
@Client.on_message(filters.private, group=pm_watcher)
async def cwf(_, m):
    if m.from_user.is_self:
        if await is_approved(m.chat.id) is False:
            await approve(m.chat.id)
            await m.reply(capsify("ᴜsᴇʀ ᴀᴘᴘʀᴏᴠᴇᴅ ᴛᴏ ᴘᴍ ᴅᴜᴇ ᴛᴏ sᴇʟғ ᴍᴇssᴀɢɪɴɢ !"))
    if not await is_pm_on():
        return
    if await verify(_, m):
        return
    if await is_approved(m.from_user.id):
        return
    await add_warn(m.from_user.id)
    if await limit() <= await get_warns(m.from_user.id):
        await m.reply("ɢᴏᴏᴅ ʙʏᴇ ᴜɴᴛɪʟ ᴍʏ ᴍᴀsᴛᴇʀ ᴀʀʀɪᴠᴇs !")
        await reset_warns(m.from_user.id)
        return await _.block_user(m.from_user.id)
    await m.reply_photo(KOWSHIK, caption=TEXT.format(m.from_user.first_name, (await _.get_me()).first_name, await limit(), await get_warns(m.from_user.id)))
 
command = "PmPermit"
help = f"`» {hl}pmprotect [on | off] - Toggles pm protection.\n\n» {hl}a - approves user to PM.\n\n» {hl}da - disapproves user to PM.\n\n» {hl}setwarns [count] - set warn limit.`"

add_command(command, help)
