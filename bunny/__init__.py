from pyrogram import Client
from config import *
from pyrogram import idle
import sys
import os

user = Client(":bunny:",
                      api_id=API_ID,
                      api_hash=API_HASH, 
                      session_string=STRING_SESSION,
                      plugins = dict(root="Rabbit")
                      )

bot = Client(":bunny:",
                     api_id=API_ID,
                     api_hash=API_HASH, 
                     bot_token=BOT_TOKEN,
                     plugins = dict(root="Rabbit")
                     )
