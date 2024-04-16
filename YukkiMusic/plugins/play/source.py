import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from typing import Union
from pyrogram.types import InlineKeyboardButton

from config import GITHUB_REPO, SUPPORT_CHANNEL, SUPPORT_GROUP
from YukkiMusic import app
from config import BANNED_USERS, MUSIC_BOT_NAME

import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

BOT_USERNAME = getenv("BOT_USERNAME")


@app.on_message(
    command(["سورس لول","سورس","السورس","يا سورس"])
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_video(
        video=f"https://t.me/YMMYr/132",
        caption=f"""**╭── • [⌯𝗦𝗢𝗨𝗥𝗖𝗘 𝗟𝗢𝗟⌯](https://t.me/K55DD) • ──╮**

**[⌯𝗗𝗘𝗩 𝗦𝗢𝗨𝗥𝗖𝗘 𝗟𝗢𝗟⌯](https://t.me/F_A_6)**

**[⌯𝗦𝗨𝗣𝗣𝗨𝗥𝗧: 𝗟𝗢𝗟⌯](https://t.me/K55DD)**

**[⌯𝗖𝗛𝗔𝗡𝗡𝗘𝗟: 𝗟𝗢𝗟⌯](https://t.me/K55DD)**

**[⌯𝗠𝗔𝗞𝗘𝗥: 𝗟𝗢𝗟⌯](https://t.me/MA_YBot)**

**╰── • [⌯𝗦𝗢𝗨𝗥𝗖𝗘 𝗟𝗢𝗟⌯](https://t.me/K55DD) • ──╯**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "صانع ميوزك مجانا ◍", url=f"https://t.me/MA_YBot"), 
                ],[
                    InlineKeyboardButton(
                        "𝗗𝗘𝗩 𝗞𝗛𝗔𝗬𝗔𝗟 ◍", url=f"https://t.me/F_A_6"),
                ],[
                    InlineKeyboardButton(
                        "أضغط لاضافه ألبوت لمجموعتك ◍", url=f"https://t.me/LL0_BOT?startgroup=true"),
                ],

            ]

        ),

    )
    
    