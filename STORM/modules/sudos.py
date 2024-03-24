import sys
import heroku3
from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, OWNER_ID, SUDO_USERS, HEROKU_APP_NAME, HEROKU_API_KEY, CMD_HNDLR as hl
from os import execl, getenv
from telethon import events

async def promote_sudo(event, target):
    Heroku = heroku3.from_key(HEROKU_API_KEY)
    sudousers = getenv("SUDO_USERS", default="")

    ok = await event.reply("» ᴘʀᴏᴍᴏᴛɪɴɢ ᴜꜱᴇʀ ɪɴ ꜱᴜᴅᴏ 🫂...")
    
    if not HEROKU_APP_NAME:
        await ok.edit("`[HEROKU]:`\nPlease Setup Your **HEROKU_APP_NAME**")
        return
    
    app = Heroku.app(HEROKU_APP_NAME)
    heroku_var = app.config()
    
    if str(target) in sudousers.split():
        await ok.edit("ᴛʜɪꜱ ᴜꜱᴇʀ ɪꜱ ᴀʟʀᴇᴀᴅʏ ɪɴ ꜱᴜᴅᴏ ʟɪꜱᴛ 💕 !!")
    else:
        newsudo = f"{sudousers} {target}".strip()
        await ok.edit(f"» **ɴᴇᴡ ꜱᴜᴅᴏ ᴜꜱᴇʀ**: `{target}`\n» ʀᴇꜱᴛᴀʀᴛɪɴɢ ⌛...")
        heroku_var["SUDO_USERS"] = newsudo

async def addsudo(event):
    if event.sender_id == OWNER_ID:
        try:
            target = int(event.pattern_match.group(1))
        except ValueError:
            await event.reply("» ɪɴᴠᴀʟɪᴅ ɪᴅ ꜰᴏʀᴍᴀᴛ, ɪɴᴅɪᴄᴀᴛᴇ ᴀɴ ɪᴅ ɴᴜᴍʙᴇʀ.")
            return
        
        await promote_sudo(event, target)
    elif event.sender_id in SUDO_USERS:
        await event.reply("» ꜱʀʏ, ᴏɴʟʏ ᴏᴡɴᴇʀ ᴄᴀɴ ᴀᴄᴄᴇꜱ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ 🔰 ")

async def sudolist(event):
    if event.sender_id == OWNER_ID:
        sudousers = getenv("SUDO_USERS", default="")
        if sudousers:
            await event.reply("» **SUDO USERS LIST:**\n" + sudousers)
        else:
            await event.reply("» **ꜱᴜᴅᴏ ᴜꜱᴇʀꜱ ʟɪꜱᴛ ɪꜱ ᴇᴍᴘᴛʏ**")
    elif event.sender_id in SUDO_USERS:
        await event.reply("» ꜱʀʏ, ᴏɴʟʏ ᴏᴡɴᴇʀ ᴄᴀɴ ᴀᴄᴄᴇꜱ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ 🔰 ")

for X in [X1, X2, X3, X4, X5, X6, X7, X8, X9, X10]:
    X.on(events.NewMessage(incoming=True, pattern=f"\\{hl}addsudo(?: |$)(.*)"))(addsudo)
    X.on(events.NewMessage(incoming=True, pattern=f"\\{hl}sudolist"))(sudolist)
