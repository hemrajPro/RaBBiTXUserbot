from bunny import user, bot

LOG = "S_T_F_U_09"

user.start()
if LOG:
  try:
    user.send_message(S_T_F_U_09, "Userbot Started Successfully.... !")
  except:
      print("Did you add the userbot to the logger group? please check again...")
print("assistant started....")
bot.start()
