from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from AloneX import app
from config import BOT_USERNAME
#from AloneX.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """
**
┌┬─────────────────⦿
│├─────────────────╮
│├ 𝗧ɢ 𝗡ᴀᴍᴇ - [ɪɴɴᴏᴄᴇɴᴛ ʙᴀᴄʜᴀ ](https://t.me/UFC_INNOCENT)
│├ 𝗙ᴜʟʟ 𝗜ɴғᴏ - [𝐂ʟɪᴄᴋ 𝐇ᴇʀᴇ](https://t.me/UFC_NETWORK)
│├─────────────────╯
├┼─────────────────⦿
│├─────────────────╮
│├ 𝗢ᴡɴᴇʀ│ [ɪɴɴᴏᴄᴇɴᴛ ʙᴀᴄʜᴀ](https://t.me/UFC_INNOCENT)
│├─────────────────╯
└┴─────────────────⦿
**
"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("𝗢ᴡɴᴇʀ", url=f"https://t.me/UFC_INNOCENT")
        ],
        [
          InlineKeyboardButton("𝗔𝗹𝗹 𝗥𝗘𝗣𝗢", url="https://t.me/UFC_NETWORK"),
          InlineKeyboardButton("𝗥𝗘𝗣𝗢", url=f"https://t.me/UFC_LINK_ZONE"),
          ],
               [
                InlineKeyboardButton("𝗧𝗛𝗘 𝗨𝗡𝗢𝗙𝗙𝗖𝗜𝗔𝗟 𝗡𝗘𝗧𝗪𝗢𝗥𝗞 ꪜ", url=f"https://t.me/UFC_NETWORK"),
],
[
InlineKeyboardButton("\x4F\x46\x46\x49\x43\x49\x41\x4C\x20\x42\x4F\x54", url=f"https://t.me/RJ_92_MUSIC_BOT?start=_tgr_5Hvua7dkN2Fl"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://files.catbox.moe/ydqiwn.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
