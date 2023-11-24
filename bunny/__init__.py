from pyrogram import Client
from config import *
from pyrogram import idle
import sys
import os

bot = Client(
    name="app",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="bunny/modules/bot"),
    in_memory=True,
)

user = Client(name="one", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION, plugins=dict(root="bunny/modules"))
