from RAUSHAN import app, API_ID, API_HASH
from config import ALIVE_PIC
from pyrogram import filters
import os
import re
import asyncio
import time
from pyrogram import *
from pyrogram.types import * 

PHONE_NUMBER_TEXT = (
    "[𝐑ɪʏᴀ 𝐔sᴇʀ 𝐁ᴏᴛ](https://t.me/Riya_user_robot) ᴛʜᴇ ꜱᴜᴘᴇʀғᴀꜱᴛ ᴜsᴇʀʙᴏᴛ ⚡\n\n➪ ʙᴇsᴛ sᴛɪᴄᴋᴇʀs , ᴀɴɪᴍᴀᴛɪᴏɴs \n➪ ʙᴇsᴛ sᴘᴀᴍ ᴍᴇssᴀɢᴇs \n ➪ ʙᴇsᴛ ʀᴀɪᴅ ᴍᴇssᴀɢᴇs \n ➪ ʙᴇsᴛ ʀᴇᴘʟʏ ʀᴀɪᴅ ᴍᴇssᴀɢᴇs \n ➪ ᴍᴀᴋᴇ ʏᴏᴜʀ ɪᴅ-ᴜsᴇʀʙᴏᴛ ʙʏ /clone [ send your PyroGram ᴠ2 String Session ] \n\n 
๏ ᴛᴏᴛᴀʟ ᴜꜱᴇʀꜱ : 270\n๏ ᴛᴏᴛᴀʟ ᴀᴄᴛɪᴠᴇ ᴜsᴇʀs : 215\n๏ ᴜᴘᴛɪᴍᴇ » 1h:23m:19s\n\n╔═════════════════╗\n║ ➻ sᴛʀɪɴɢ ʙᴏᴛ ➪ ᴄʟɪᴄᴋ ʜᴇʀᴇ \n║ ➻ ᴅᴇᴠᴇʟᴏᴘᴇʀ ➪ ʜᴜɴᴛᴇʀ xᴅ \n╚═════════════════╝"
)

@app.on_message(filters.command("start"))
async def hello(client: app, message):
    buttons = [
           [
                InlineKeyboardButton("⚡𝙾𝚆𝙽𝙴𝚁 💕⚡", url="t.me/oy_rishu"),
            ],
            [
                InlineKeyboardButton("⚡𝙲𝙷𝙰𝙽𝙽𝙴𝙻 💕⚡", url="t.me/ajisbackk"),
            ],
            [
                InlineKeyboardButton("⚡𝚂𝚄𝙿𝙿𝙾𝚁𝚃 💕⚡", url="t.me/TEAM_RIYA_SUPPORT"),
            ],
            ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await client.send_photo(message.chat.id, ALIVE_PIC, caption=PHONE_NUMBER_TEXT, reply_markup=reply_markup)

# © By itzshukla Your motherfucker if uh Don't gives credits.
@app.on_message(filters.command("clone"))
async def clone(bot: app, msg: Message):
    chat = msg.chat
    text = await msg.reply("Usage:\n\n /clone session")
    cmd = msg.command
    phone = msg.command[1]
    try:
        await text.edit("ᴡᴀɪᴛ ʙᴀʙʏ ғᴇᴡ sᴇᴄᴏɴᴅs...💌")
                   # change this Directry according to ur repo
        client = Client(name="Melody", api_id=API_ID, api_hash=API_HASH, session_string=phone, plugins=dict(root="RAUSHAN/modules"))
        await client.start()
        user = await client.get_me()
        await msg.reply(f" ᴊᴀ ᴘᴇʟ ᴅᴇ sᴀʙᴋᴏ ᴀʙ ʟᴇɢᴇɴᴅ ᴋᴏ ʙᴀᴀᴘ ʙᴏʟ ᴋᴇ ᴊᴀɴᴀ 🥵 {user.first_name} 💨.")
    except Exception as e:
        await msg.reply(f"**ERROR:** `{str(e)}`\nPress /start to Start again.")
