from bunny import user, bot

async def start_bot():
  await user.start()
  for all_module in ALL_MODULES:
        importlib.import_module("bunny.modules" + all_module)
        print(f"Successfully Imported {all_module} 💥")
try:
  user.send_message(-1001901276605, "Userbot Started Successfully.... !")
except:
    print("Did you add the userbot to the logger group? please check again...")
  await bot.start()

