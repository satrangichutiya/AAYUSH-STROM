import logging
from telethon import TelegramClient
from os import getenv
from STORM.data import DEV

# Logging setup
logging.basicConfig(
    format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
    level=logging.WARNING
)

# API credentials
API_ID = int(getenv("API_ID", default="25742938"))
API_HASH = getenv("API_HASH", default="b35b715fe8dc0a58e8048988286fc5b6")
CMD_HNDLR = getenv("CMD_HNDLR", default="!")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)

BOT_TOKEN = getenv("BOT_TOKEN", default=None)

# Owner & Sudo Setup
OWNER_ID = int(getenv("OWNER_ID", default="123456789"))
SUDO_USERS = [OWNER_ID]

# ---------- CLIENTS ----------
X1 = TelegramClient("X1", API_ID, API_HASH).start(bot_token=BOT_TOKEN)

# These require manual session login (won't work on Render without session files)
try:
    X2 = TelegramClient("X2", API_ID, API_HASH).start()
    X3 = TelegramClient("X3", API_ID, API_HASH).start()
    X4 = TelegramClient("X4", API_ID, API_HASH).start()
    X5 = TelegramClient("X5", API_ID, API_HASH).start()
    X6 = TelegramClient("X6", API_ID, API_HASH).start()
    X7 = TelegramClient("X7", API_ID, API_HASH).start()
    X8 = TelegramClient("X8", API_ID, API_HASH).start()
    X9 = TelegramClient("X9", API_ID, API_HASH).start()
    X10 = TelegramClient("X10", API_ID, API_HASH).start()
except Exception as e:
    logging.warning(f"Some clients failed to start: {e}")
    X2 = X3 = X4 = X5 = X6 = X7 = X8 = X9 = X10 = None
