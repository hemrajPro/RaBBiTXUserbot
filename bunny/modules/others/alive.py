


@Client.on_message(filters.command(["alive", "rabbit", "rabbitx"], ".") & filters.me)
async def alive(client: Client, message: Message):
    await message.edit("hn")
    await asyncio.sleep(0.3)
    await message.edit("hnn")
    await asyncio.sleep(0.2)
    await message.edit("hnn")
    await asyncio.sleep(0.5)
    await message.edit("hnn")
