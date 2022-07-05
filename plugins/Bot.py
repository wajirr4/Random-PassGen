import random, string
from pyrogram import Client as sree
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from resources.str import (NUMARIC, alpha, ALPHA)


@sree.on_message(filters.command('pgen'))
async def radniompass(sree, m: Message):
    msgg = await m.reply('__Generating your password plish wait..__')
    
    Pass = string.ascii_letters + string.digits + string.punctuation
    P = ''.join(random.choice(Pass) for _ in range(10))
    await msgg.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="ping_")]]))
  
