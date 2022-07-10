from asyncio import sleep
import platform
from resources.Buttons import strtbtn
from pyrogram import Client as sree
from pyrogram import filters, __version__ as pyro
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup


@sree.on_message(filters.command('start'))
async def start(sree, m: Message):
    nm = m.from_user.first_name
    uid = m.from_user.id
    chtid = m.chat.id
    await m.reply_sticker('CAACAgUAAx0CWOSA3AABBtl5YspfsV3UeUpFs3pfmeoy0UMM_tMAAn8FAAIvIkBW70JZlNo13zcpBA')
    a = await m.reply(chtid, f"Hey, [{nm}](tg://user?id={uid}) 🙋")
    await sleep(0.5)
    b = await a.edit_text("Starting Bot Server For You..")
    await sleep(1)
    c = await b.edit_text("Server Started Successfully ✅\n\nHere we Go🥳!!")
    await sleep(0.4)
    await c.edit_text(statxt.format(nm, platform.python_version(), pyro), reply_markup=InlineKeyboardMarkup(strtbtn))     
    
