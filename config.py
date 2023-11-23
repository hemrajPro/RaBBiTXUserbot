from os import getenv
from dotenv import load_dotenv

load_dotenv()

# necessary api_ids 
API_ID = int(getenv("API_ID", None))
API_HASH = getenv("API_HASH", None)
STRING_SESSION = getenv("STRING_SESSION", None)
MONGO_DB_URI = getenv("MONGO_DB_URI", None)
BOT_TOKEN = getenv("BOT_TOKEN",None)

# logs
LOG_ID = getenv("LOG_ID", None)

# handler
COMMAND_HANDLER = getenv("COMMAND_HANDLER", None)

# pics
ALIVE_PIC = getenv("ALIVE_PIC", None)
PING_PIC = getenv("PING_PIC", None)
HELP_PIC = getenv("HELP_PIC", None)
