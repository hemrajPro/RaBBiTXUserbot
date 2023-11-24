from bunny.core.clients import bunny, bot
import asyncio
import importlib
from pyrogram import Client, idle
from bunny.modules import ALL_MODULES

async def start_user():
    await bot.start()
    print("[•bunny•]: єνєяутнιиg ιѕ σк, ѕтαятιиg... уσυя υѕєявσт ρℓєαѕє ωαιт... ⚡")
    for all_module in ALL_MODULES:
        importlib.import_module("bunny.modules" + all_module)
        print(f"[•bunny•] ѕυ¢¢єѕѕfυℓℓу ιмρσятє∂ {all_module} ⚡")
    await bunny.start()
    x = await bunny.get_me()
    print(f"υѕєявσт ѕυ¢¢єѕѕfυℓℓყ ѕтαятє∂ αѕ {x.first_name} ⚡ ")
    await idle()
