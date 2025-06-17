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
API_ID = 18136872
API_HASH = "312d861b78efcd1b02183b2ab52a83a4"
CMD_HNDLR = getenv("CMD_HNDLR", default="!")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)

BOT_TOKEN = getenv("BOT_TOKEN", default=None)

# Owner & Sudo Setup
OWNER_ID = int(getenv("OWNER_ID", default="7021594661"))

# ✅ Define SUDO_USERS properly
SUDO_USERS = [OWNER_ID]

# ------------- CLIENTS -------------
X1 = TelegramClient(
    'ᴘʏʀᴏɢʀᴀᴍ x ꜱᴘᴀᴍ 1', API_ID, API_HASH
).start(bot_token=BOT_TOKEN)
