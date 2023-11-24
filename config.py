from os import getenv

# API_IDS
API_ID = int(getenv("API_ID", None)) # API_ID get it from my.telegram.org
API_HASH = getenv("API_HASH", None) # API_HASH get ut from my.telegram.org

# SESSIONS
STRING_SESSION = getenv("STRING_SESSION", None) # SESSION get it by run cmd "python3 RaBBiTgram.py" in heroku consol or locally 
BOT_TOKEN = getenv("BOT_TOKEN",None) # BOT_TOKEN get it from @BotFather Bot on telegram

# DATABASES
MONGO_DB_URI = getenv("MONGO_DB_URI", None) # MONGO_DB_URL get it from mongodb.com

# LOGGGERS
LOG_GROUP_ID = getenv("LOG_GROUP_ID", None) # LOG_GROUP_ID get it by creating private group on telegram and fill here that's group id

# HANDLER
HANDLER = getenv("HANDLER", None) # HANDLER choose your bot command handler

# IMAGES
ALIVE_PIC = getenv("ALIVE_PIC", None) # ALIVE_PIC a pic link for alive command in bot
HELP_PIC = getenv("HELP_PIC", None) # HELP_PIC a pic link for help commad in bot
