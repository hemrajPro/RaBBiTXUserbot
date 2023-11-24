from bunny import user as cli
from bunny import bot as app
import asyncio
import importlib
from pyrogram import Client, idle
from bunny.modules import ALL_MODULES

async def start_bot():
    await app.start()
    print("LOG: Founded Bot token Booting..")
    for all_module in ALL_MODULES:
        importlib.import_module("bunny.modules" + all_module)
        print(f"Successfully Imported {all_module} 💥")
    await cli.start()
    ex = await cli.get_me()
    print(f"Started {ex.first_name} 🔥")
    await idle()

loop = asyncio.get_event_loop()
loop.run_until_complete(start_bot())
