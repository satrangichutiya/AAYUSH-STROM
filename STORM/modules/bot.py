from telethon import __version__, events, Button
import asyncio
import sys
import heroku3
from time import time
from datetime import datetime
from telethon import events
from telethon.errors import ForbiddenError
from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, OWNER_ID, SUDO_USERS, HEROKU_APP_NAME, HEROKU_API_KEY, CMD_HNDLR as hl
from telethon import events, version, Button
from telethon.tl.custom import button
from os import execl, getenv
from telethon.tl.functions.channels import LeaveChannelRequest

pongg = "SATHYA X SPAM"
PIC = "https://files.catbox.moe/jckm1q.jpg"
Alivemsg = "SATHYA SPAM x ꜱᴘᴀᴍ ʜᴇʀᴇ"

TEXT = f"‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌ㅤㅤㅤ • ᴘʏʀᴏɢʀᴀᴍ x ꜱᴘᴀᴍ ɪꜱ ᴀʟɪᴠᴇ • ㅤㅤㅤ\n"
TEXT = f"‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌ㅤ ʙᴏᴛ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ‌🪽\n"
TEXT += f"➖➖➖➖➖➖➖➖➖➖➖\n"
TEXT += f"**• ᴘʏᴛʜᴏɴ ᴠᴇʀꜱɪᴏɴ** 🐍: `3.11.3`\n"
TEXT += f"**• ʙᴏᴛ ᴠᴇʀꜱɪᴏɴ** ⚙️: `M3.0`\n"
TEXT += f"**• ɢʀᴏᴜᴘ 💫: [ɢʀᴏᴜᴘ 🥀](https://t.me/TEST_V21)**\n"
TEXT += f"**• ᴄʜᴀɴɴᴇʟ ✨: [ᴄʜᴀɴɴᴇʟ 🥀](https://t.me/TEST_V21)**\n"
TEXT += f"**• ꜱᴇɴꜱᴇɪ 🫂: [AYUSH 🥀](https://t.me/TEST_V21)**\n"
TEXT += f"➖➖➖➖➖➖➖➖➖➖➖"
                                  
@X1.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))

async def alive(event):
  if event.sender_id in SUDO_USERS:
     await event.client.send_file(event.chat_id,
                                  PIC,
                                  caption=TEXT,
                                  buttons=[
        [
        Button.url("• ᴄʜᴀɴɴᴇʟ •", "https://t.me/TEST_V21"),
        Button.url("• ꜱᴜᴘᴘᴏʀᴛ •", "https://t.me/TEST_V21")
        ],
        ]
        )
    
def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time

@X1.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))

async def logs(KEX):
    if KEX.sender_id == OWNER_ID:
        if (HEROKU_APP_NAME is None) or (HEROKU_API_KEY is None):
            await KEX.reply(
                KEX.chat_id,
                "ꜰɪʀꜱᴛ ꜱᴇᴛ ᴛʜᴇꜱᴇ ᴠᴀʀꜱ :  `HEROKU_API_KEY` And `HEROKU_APP_NAME`.",
            )
            return

        try:
            Heroku = heroku3.from_key(HEROKU_API_KEY)
            app = Heroku.app(HEROKU_APP_NAME)
        except BaseException:
            await KEX.reply(
                "ᴍᴀᴋᴇ ꜱᴜʀᴇ ʏᴏᴜʀ ʜᴇʀᴏᴋᴜ ᴋᴇʏ ᴀɴᴅ ᴀᴘᴘ ɴᴀᴍᴇ ᴀʀᴇ ᴄᴏɴꜰɪɢᴜᴇᴅ ᴄᴏʀʀᴇᴄᴛʟʏ"
            )
            return

        logs = app.get_log()
        start = datetime.now()
        fetch = await KEX.reply(f"ꜰᴇᴛᴄʜʜɪɴɢ ʟᴏɢꜱ ᴘʟᴇᴀꜱᴇ ᴡᴀɪᴛ 📄...")
    
        with open("Logs.txt", "w") as logfile:
            logfile.write("ꜱᴛᴏʀᴍ 𝚇 🍷 [ Bot Logs ]\n\n" + logs)

        end = datetime.now()
        ms = (end-start).seconds
        await asyncio.sleep(1)

        try:
            await X1.send_file(KEX.chat_id, "ʟᴏɢꜱ.ᴛxᴛ", caption=f"⚡ **ʙᴏᴛ ʟᴏɢꜱ 🍷** ⚡\n  » **ᴛɪᴍᴇ ᴛᴀᴋᴇɴ ⌛:** `{ms} ꜱᴇᴄᴏɴᴅꜱ`")
            await fetch.delete()
        except Exception as e:
            await fetch.edit(f"**ᴇʀᴏᴏʀ:** {str(e)}")

    elif KEX.sender_id in SUDO_USERS:
        await KEX.reply("» YEH COMMAND SIRF MERA BAAP KAR SAKTA HAI JO H @SATHYA_0P🤖 ")

@X1.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))

async def leave(e):
    if e.sender_id in SUDO_USERS:

        if len(e.text) > 7:
            event = await e.reply("» ʟᴇᴀᴠɪɴɢ ⌛...")
            mkl = e.text.split(" ", 1)
            try:
                await event.client(LeaveChannelRequest(int(mkl[1])))
            except Exception as e:
from telethon import __version__, events, Button
import asyncio
import sys
import heroku3
from time import time
from datetime import datetime
from telethon.errors import ForbiddenError
from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, OWNER_ID, SUDO_USERS, HEROKU_APP_NAME, HEROKU_API_KEY, CMD_HNDLR as hl
from os import execl, getenv
from telethon.tl.functions.channels import LeaveChannelRequest

pongg = "SATHYA X SPAM"
PIC = "https://files.catbox.moe/jckm1q.jpg"

TEXT = "‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌ㅤㅤㅤ • ᴘʏʀᴏɢʀᴀᴍ x ꜱᴘᴀᴍ ɪꜱ ᴀʟɪᴠᴇ • ㅤㅤㅤ\n"
TEXT += "‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌ㅤ ʙᴏᴛ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ‌🪽\n"
TEXT += "➖➖➖➖➖➖➖➖➖➖➖\n"
TEXT += "**• ᴘʏᴛʜᴏɴ ᴠᴇʀꜱɪᴏɴ** 🐍: `3.11.3`\n"
TEXT += "**• ʙᴏᴛ ᴠᴇʀꜱɪᴏɴ** ⚙️: `M3.0`\n"
TEXT += "**• ɢʀᴏᴜᴘ 💫: [ɢʀᴏᴜᴘ 🥀](https://t.me/TEST_V21)**\n"
TEXT += "**• ᴄʜᴀɴɴᴇʟ ✨: [ᴄʜᴀɴɴᴇʟ 🥀](https://t.me/TEST_V21)**\n"
TEXT += "**• ꜱᴇɴꜱᴇɪ 🫂: [AYUSH 🥀](https://t.me/TEST_V21)**\n"
TEXT += "➖➖➖➖➖➖➖➖➖➖➖"

@X1.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
async def alive(event):
    if event.sender_id in SUDO_USERS:
        await event.client.send_file(
            event.chat_id,
            PIC,
            caption=TEXT,
            buttons=[
                [
                    Button.url("• ᴄʜᴀɴɴᴇʟ •", "https://t.me/TEST_V21"),
                    Button.url("• ꜱᴜᴘᴘᴏʀᴛ •", "https://t.me/TEST_V21")
                ]
            ]
        )

def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time

@X1.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
async def logs(KEX):
    if KEX.sender_id == OWNER_ID:
        if (HEROKU_APP_NAME is None) or (HEROKU_API_KEY is None):
            await KEX.reply("ꜰɪʀꜱᴛ ꜱᴇᴛ ᴛʜᴇꜱᴇ ᴠᴀʀꜱ :  `HEROKU_API_KEY` And `HEROKU_APP_NAME`.")
            return
        try:
            Heroku = heroku3.from_key(HEROKU_API_KEY)
            app = Heroku.app(HEROKU_APP_NAME)
        except BaseException:
            await KEX.reply("ᴍᴀᴋᴇ ꜱᴜʀᴇ ʏᴏᴜʀ ʜᴇʀᴏᴋᴜ ᴋᴇʏ ᴀɴᴅ ᴀᴘᴘ ɴᴀᴍᴇ ᴀʀᴇ ᴄᴏɴꜰɪɢᴜʀᴇᴅ ᴄᴏʀʀᴇᴄᴛʟʏ")
            return
        logs = app.get_log()
        start = datetime.now()
        fetch = await KEX.reply("ꜰᴇᴛᴄʜʜɪɴɢ ʟᴏɢꜱ ᴘʟᴇᴀꜱᴇ ᴡᴀɪᴛ 📄...")
        with open("Logs.txt", "w") as logfile:
            logfile.write("ꜱᴛᴏʀᴍ 𝚇 🍷 [ Bot Logs ]\n\n" + logs)
        end = datetime.now()
        ms = (end-start).seconds
        await asyncio.sleep(1)
        try:
            await X1.send_file(KEX.chat_id, "Logs.txt", caption=f"⚡ **ʙᴏᴛ ʟᴏɢꜱ 🍷** ⚡\n  » **ᴛɪᴍᴇ ᴛᴀᴋᴇɴ ⌛:** `{ms} ꜱᴇᴄᴏɴᴅꜱ`")
            await fetch.delete()
        except Exception as e:
            await fetch.edit(f"**ᴇʀʀᴏʀ:** {str(e)}")
    elif KEX.sender_id in SUDO_USERS:
        await KEX.reply("» YEH COMMAND SIRF MERA BAAP KAR SAKTA HAI JO H @SATHYA_0P🤖 ")

@X1.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
async def leave(e):
    if e.sender_id in SUDO_USERS:
        if len(e.text) > 7:
            event = await e.reply("» ʟᴇᴀᴠɪɴɢ ⌛...")
            mkl = e.text.split(" ", 1)
            try:
                await event.client(LeaveChannelRequest(int(mkl[1])))
            except Exception as e:
                await event.edit(str(e))
        else:
            if e.is_private:
                await e.reply(f"**» ʏᴏᴜ ᴄᴀɴ'ᴛ ᴅᴏ ᴛʜɪꜱ ʜᴇʀᴇ !!**\n\n» {hl}ʟᴇᴀᴠᴇ : ᴛʏᴘᴇ ᴛʜɪꜱ ɪɴ ɢʀᴏᴜᴘ")
            else:
                event = await e.reply("» ʟᴇᴀᴠɪɴɢ ⌛...")
                try:
                    await event.client(LeaveChannelRequest(int(e.chat_id)))
                except Exception as e:
                    await event.edit(str(e))

@X1.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
async def ping(e):
    if e.sender_id in SUDO_USERS:
        start = datetime.now()
        KEX = await e.reply("🌩")
        end = datetime.now()
        mp = (end - start).microseconds / 10000
        await KEX.edit(f"**SATHYA SPAM X SABKI MAA CHODNE KE LIYE READY HAIN 💸❤️‍🔥** ⚡\n» `{mp} ᴍꜱ`")

@X1.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
async def addsudo(event):
    if event.sender_id == OWNER_ID:
        Heroku = heroku3.from_key(HEROKU_API_KEY)
        sudousers = getenv("SUDO_USERS", default=None)
        ok = await event.reply("» YEH SATHYA KI AULAD HAI ISPE RAID MAT KARO🙂...")
        target = ""
        if HEROKU_APP_NAME is not None:
            app = Heroku.app(HEROKU_APP_NAME)
        else:
            await ok.edit("`[HEROKU]:` Please Setup Your **HEROKU_APP_NAME**")
            return
        heroku_var = app.config()
        try:
            reply_msg = await event.get_reply_message()
            target = reply_msg.sender_id
        except:
            await ok.edit("» ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ !!")
            return
        if str(target) in sudousers:
            await ok.edit(f"ARE YEH TO MERA BETA HAI !!")
        else:
            newsudo = f"{sudousers} {target}" if sudousers else f"{target}"
            await ok.edit(f"» **ɴᴇᴡ ꜱᴜᴅᴏ ᴜꜱᴇʀ**: `{target}`\n» ʀᴇsᴛᴀʀᴛɪɴɢ ʙᴏᴛ...")
            heroku_var["SUDO_USERS"] = newsudo
    elif event.sender_id in SUDO_USERS:
        await event.reply("» LODA CHOOSO NA SOR KYA NAAM HAIN AAPKA?.")

@X1.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
async def restart(e):
    if e.sender_id in SUDO_USERS:
        await e.reply("`ME WAPIS AAUNGA BHOSDIWALo😭...`")
        for bot in [X1, X2, X3, X4, X5, X6, X7, X8, X9, X10]:
            try:
                await bot.disconnect()
            except Exception:
                pass
        execl(sys.executable, sys.executable, *sys.argv)
