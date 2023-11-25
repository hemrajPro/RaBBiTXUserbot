from pyrogram import Client, filters
from bunny.core.clients import bunny as Client 
from pyrogram.types import Message
from bunny import startTime
from bunny import get_uptime
import time 
import asyncio
import random
from pyrogram import __version__ as py_version
version = "v1.0"
from platform import python_version
from config import ALIVE_PIC

aliver = """
╭────────────────๏
╰๏⚡ __**яαввιтχ ιѕ αℓινє**__ ⚡
╭────────────────๏
╰๏ **__σωиєя »__** {}
╰๏ __**ρуяσgяαм »__** `{}`
╰๏ __**яαввιтχ »**__ `{}`
╰๏ __**ρутнσи »__** `{}`
╰๏ __**υρтιмє »__** `{}`
╰────────────────๏
╰๏      【[ƚԋҽ ɾαႦႦιƚx](https://t.me/RaBBit_guys)】       
╰────────────────๏
"""

@Client.on_message(filters.command(["alive", "rabbit", "rabbitx"], ".") & filters.me)
async def alive(client: Client, message: Message):
    await message.edit("`ρяσƈҽʂʂιɳɠ....`")
    await asyncio.sleep(0.3)
    user = (await Client.get_me()).mention
    upt = get_uptime(time.time())
    await message.edit("`яαввιтχ ιѕ αℓινє...⚡`")
    await asyncio.sleep(0.3)
    await message.edit("`gєттιиg вσт ∂єтαιℓѕ...⚡`")
    await asyncio.sleep(0.3)
    await message.delete()
    await message.reply_photo(ALIVE_PIC, caption=aliver.format(user, py_version, version, python_version(), upt)) 
