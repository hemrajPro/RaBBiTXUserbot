async def eor(ok, t):
    try:
        return await ok.edit(t)
    except:
        return await ok.reply(t)
