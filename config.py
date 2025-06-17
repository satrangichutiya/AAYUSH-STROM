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
    getenv("BOT_TOKEN1"),
    getenv("BOT_TOKEN2"),
    getenv("BOT_TOKEN3"),
    getenv("BOT_TOKEN4"),
    getenv("BOT_TOKEN5"),
    getenv("BOT_TOKEN6"),
    getenv("BOT_TOKEN7"),
    getenv("BOT_TOKEN8"),
    getenv("BOT_TOKEN9"),
    getenv("BOT_TOKEN10"),
]

clients = []
for i, token in enumerate(BOT_TOKENS):
    if token:
        try:
            client = TelegramClient(f"X{i+1}", API_ID, API_HASH).start(bot_token=token)
            logging.warning(f"[X{i+1}] started successfully")
            clients.append(client)
        except Exception as e:
            logging.warning(f"[X{i+1}] failed to start: {e}")
            clients.append(None)
    else:
        logging.warning(f"[X{i+1}] BOT_TOKEN{i+1} is not set.")
        clients.append(None)

# Assign named clients
X1, X2, X3, X4, X5, X6, X7, X8, X9, X10 = clients
