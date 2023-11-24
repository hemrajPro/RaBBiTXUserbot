ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
ALL_CAPS = "ᴀʙᴄᴅᴇғɢʜɪᴊᴋʟᴍɴᴏᴘǫʀsᴛᴜᴠᴡxʏᴢ"

def capsify(text: str) -> str:
  txt: str = ""
  for x in text.split():
    for y in x:
      if y.lower() in ALPHABETS:
        ind = ALPHABETS.index(y.lower())
        txt += ALL_CAPS[ind]
      else:
        txt += y
    txt += " "
  return txt
  
def capsify_parts(text: str, splitter: str = "*") -> str:
  if not splitter in text:
    return text
  spl = text.split("*")
  a = 0
  for i in range(0, len(spl)):
    if i % 2 == 0:
      continue
    spl[i] = capsify(spl[i])
  txt: str = ""
  for x in spl:
    txt += x
  return txt
    