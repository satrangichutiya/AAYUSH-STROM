from telethon import __version__, events, Button
from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10

START_OP = [
    [
        Button.url("ꜱᴇɴꜱᴇɪ 🥀", "https://t.me/HOD_AYUSH_PYROGRAM_CLIENT"),
        Button.url("ꜱᴜᴘᴘᴏʀᴛ ✨", "https://t.me/HOD_AYUSH_PYROGRAM_CLIENT"),
    ],
    [
        Button.url(
            "ɢʀᴏᴜᴘ 🧸", "https://t.me/HOD_AYUSH_PYROGRAM_CLIENT"
        ),
    ],
    [
        Button.url("ꜱᴏᴜʀᴄᴇ ᴄᴏᴅᴇ ❄️", "https://github.com/VARC9210/STORM"),
        Button.url("ᴄʜᴀɴɴᴇʟ ☁️", "https://t.me/HOD_AYUSH_PYROGRAM_CLIENT"),
    ],
]

@X1.on(events.NewMessage(pattern="/start"))
@X2.on(events.NewMessage(pattern="/start"))
@X3.on(events.NewMessage(pattern="/start"))
@X4.on(events.NewMessage(pattern="/start"))
@X5.on(events.NewMessage(pattern="/start"))
@X6.on(events.NewMessage(pattern="/start"))
@X7.on(events.NewMessage(pattern="/start"))
@X8.on(events.NewMessage(pattern="/start"))
@X9.on(events.NewMessage(pattern="/start"))
@X10.on(events.NewMessage(pattern="/start"))
async def start(event):
    if event.is_private:
        KEX = await event.client.get_me()
        bot_name = KEX.first_name
        bot_id = KEX.id
        TEXT = f"**ʜᴇʏ [{event.sender.first_name}]\n\nɪ ᴀᴍ [{bot_name}](tg://user?id={bot_id})​**\n➖➖➖➖➖➖➖➖➖➖➖\n"
        TEXT += f"» **ꜱᴇɴꜱᴇɪ : [ꜱᴇɴꜱᴇɪ](https://t.me/HOD_AYUSH_PYROGRAM_CLIENT)**\n"
        TEXT += f"» **ᴘʏʀᴏɢʀᴀᴍ x ꜱᴘᴀᴍ :** `M1.0` \n"
        TEXT += f"» **ᴘʏᴛʜᴏɴ :** `3.11` \n"
        TEXT += f"» **ᴛᴇʟᴇᴛʜᴏɴ :** `{__version__}`\n➖➖➖➖➖➖➖➖➖➖➖"        
        await event.client.send_file(
                    event.chat_id,  
                    "https://graph.org/file/fb1ae9fa7f75d73efb5f2.jpg",
                    caption=TEXT, 
                    buttons=START_OP
                )
