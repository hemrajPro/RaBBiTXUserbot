from bunny.core.clients import bunny, bot
import asyncio
import time
import importlib
from pyrogram import Client, idle
from bunny.modules import ALL_MODULES

startTime = time.time()

def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]
    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)
    for i in range(len(time_list)):
        time_list[i] = str(time_list[i]) + time_suffix_list[i]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "
    time_list.reverse()
    ping_time += ":".join(time_list)
    return ping_time

def get_uptime(x):
    z = get_readable_time(int(x-startTime))
    return z

grt = get_readable_time


async def start_user():
    await bot.start()
    print("[•bunny•]: єνєяутнιиg ιѕ σк, ѕтαятιиg... уσυя υѕєявσт ρℓєαѕє ωαιт... ⚡")
    for all_module in ALL_MODULES:
        importlib.import_module("bunny.modules" + all_module)
        print(f"[•bunny•] ѕυ¢¢єѕѕfυℓℓу ιмρσятє∂ {all_module} ⚡")
    await bunny.start()
    x = await bunny.get_me()
    print(f"υѕєявσт ѕυ¢¢єѕѕfυℓℓყ ѕтαятє∂ αѕ {x.first_name} ⚡ ")
    try:
     await bunny.join_chat("RaBBiT_GuYs")
     await bunny.join_chat("S_T_F_U_09")
    except:
      pass
    try:
     await bunny.send_message(-1001901276605, "__**ѕтαятє∂ !!**__")
    except:
      pass
    await idle()
  
loop = asyncio.get_event_loop()
loop.run_until_complete(start_user())
