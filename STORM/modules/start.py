#MIT License



#Copyright (c) 2024 ᴋᴜɴᴀʟ [AFK]



#Permission is hereby granted, free of charge, to any person obtaining a copy

#of this software and associated documentation files (the "Software"), to deal

#in the Software without restriction, including without limitation the rights

#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell

#copies of the Software, and to permit persons to whom the Software is

#furnished to do so, subject to the following conditions:



#The above copyright notice and this permission notice shall be included in all

#copies or substantial portions of the Software.



#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR

#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,

#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE

#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER

#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,

#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE

#SOFTWARE.



from telethon import version, events, Button

from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10



START_OP = [

    [

        Button.url("ꜱᴇɴꜱᴇɪ 🥀", "https://t.me/TEST_V21"),

        Button.url("ꜱᴜᴘᴘᴏʀᴛ ✨", "https://t.me/TEST_V21"),

    ],

    [

        Button.url(

            "ɢʀᴏᴜᴘ 🧸", "https://t.me/TEST_V21"

        ),

    ],

    [

        Button.url("ꜱᴏᴜʀᴄᴇ ᴄᴏᴅᴇ ❄️", "LAWDE SAALE TU KON? CHAL @SATHYA_0P SE MAANG REPO DE DEGA"),

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

        KEX = await event.client.get_me()

        bot_name = KEX.first_name

        bot_id = KEX.id

        TEXT = f"ʜᴇʏ [{event.sender.first_name}]\n\nɪ ᴀᴍ [{bot_name}](tg://user?id={bot_id})\n➖➖➖➖➖➖➖➖➖➖➖\n"

        TEXT += f"» ꜱᴇɴꜱᴇɪ : [⏤‌〲SATHYA](https://t.me/SATHYA_0P)\n"

        TEXT += f"» SATHYA SPAM : M3.0 \n"

        TEXT += f"» ᴘʏᴛʜᴏɴ : 3.11 \n"

        TEXT += f"» ᴛᴇʟᴇᴛʜᴏɴ : {version}\n➖➖➖➖➖➖➖➖➖➖➖"        

        await event.client.send_file(

                    event.chat_id,  

                    "https://telegra.ph/file/20e905f22c14c40d9bba7.jpg",

                    caption=TEXT, 

                    buttons=START_OP

      )
