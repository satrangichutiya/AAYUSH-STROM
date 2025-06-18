from telethon import version, events, Button
from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10

START_OP = [
    [
        Button.url("ꜱᴇɴꜱᴇɪ 🥀", "https://t.me/TEST_V21"),
        Button.url("ꜱᴜᴘᴘᴏʀᴛ ✨", "https://t.me/TEST_V21"),
    ],
    [
        Button.url("ɢʀᴏᴜᴘ 🧸", "https://t.me/TEST_V21"),
    ],
    [
        Button.url("ꜱᴏᴜʀᴄᴇ ᴄᴏᴅᴇ ❄️", "https://t.me/SATHYA_0P"),
        Button.url("ᴄʜᴀɴɴᴇʟ ☁️", "https://t.me/TEST_V21"),
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
        me = await event.client.get_me()
        bot_name = me.first_name
        bot_id = me.id

        TEXT = f"ʜᴇʏ [{event.sender.first_name}]\n\n"
        TEXT += f"ɪ ᴀᴍ [{bot_name}](tg://user?id={bot_id})\n"
        TEXT += "➖➖➖➖➖➖➖➖➖➖➖\n"
        TEXT += "» ꜱᴇɴꜱᴇɪ : [⏤‌〲SATHYA](https://t.me/SATHYA_0P)\n"
        TEXT += "» SATHYA SPAM : M3.0\n"
        TEXT += "» ᴘʏᴛʜᴏɴ : 3.11\n"
        TEXT += f"» ᴛᴇʟᴇᴛʜᴏɴ : {version.__version__}\n"
        TEXT += "➖➖➖➖➖➖➖➖➖➖➖"

        await event.client.send_file(
            event.chat_id,
            "https://telegra.ph/file/20e905f22c14c40d9bba7.jpg",
            caption=TEXT,
            buttons=START_OP
        )
