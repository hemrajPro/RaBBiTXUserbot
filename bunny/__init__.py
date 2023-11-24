from config import *
import sys
import asyncio
from pyrogram import Client, idle

x = False

if not API_ID:
  print("API_ID not found please check again... ⚡")
  x = True

if not API_HASH:
  print("API_HASH not found please check again... ⚡")
  x = True

if not BOT_TOKEN:
  print("BOT_TOKEN not found please check again... ⚡")
  x = True
  
if not STRING_SESSION:
  print("STRING_SESSION not found please check again.... ⚡")
  x = True
  
if not MONGO_DB_URI:
  print("MONGO_DB_URI nit found please check again... ⚡")
  x = True
