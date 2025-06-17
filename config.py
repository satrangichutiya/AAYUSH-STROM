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

# Owner & Sudo Setup
OWNER_ID = int(getenv("OWNER_ID", default="7680595441"))
SUDO_USERS = [OWNER_ID]

# ---------- CLIENTS ----------
BOT_TOKENS = [
    getenv("BOT_TOKEN1", default=None),
    getenv("BOT_TOKEN2", default=None),
    getenv("BOT_TOKEN3", default=None),
    getenv("BOT_TOKEN4", default=None),
    getenv("BOT_TOKEN5", default=None),
    getenv("BOT_TOKEN6", default=None),
    getenv("BOT_TOKEN7", default=None),
    getenv("BOT_TOKEN8", default=None),
    getenv("BOT_TOKEN9", default=None),
    getenv("BOT_TOKEN10", default=None),
]

clients = []

for i in range(10):
    token = BOT_TOKENS[i]
    if token:
        try:
            client = TelegramClient(f"X{i+1}", API_ID, API_HASH).start(bot_token=token)
            clients.append(client)
        except Exception as e:
            logging.warning(f"[X{i+1}] failed to start: {e}")
            clients.append(None)
    else:
        clients.append(None)

# Assign named clients
X1, X2, X3, X4, X5, X6, X7, X8, X9, X10 = clients
