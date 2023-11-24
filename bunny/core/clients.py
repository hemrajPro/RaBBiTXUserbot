from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN, STRING_SESSION

bot = Client(
     name="bunny",
     api_id=API_ID,
     api_hash=API_HASH,
     bot_token=BOT_TOKEN
   )

bunny = Client(name="bunny", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION)
