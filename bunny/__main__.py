from bunny import user, bot
user.start()
try:
  user.send_message(-1001901276605, "Userbot Started Successfully.... !")
except:
    print("Did you add the userbot to the logger group? please check again...")

print("assistant started....")
bot.start()
