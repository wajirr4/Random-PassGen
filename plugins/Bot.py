import random, string
from pyrogram import Client as sree
from pyrogram import filters
from pyrogram.types import Message
from resources.str import (NUMARIC, alpha, ALPHA)


@sree.on_message(filters.command('start', prefixes="/"))
async def passgen(sree, m: Message):
    await sree.send_message(m.chat.id, "i am jinda sur") 
@sree.on_message(filters.command('pgen'))
async def radniompass(sree, m: Message):
    msgg = await m.reply('__Generating your password plish wait..__')
    
    a = random.choice(ALPHA)    
    b = random.choice(alpha)   
    c = random.choice(NUMARIC)    
    symbol = string.punctuation
    d = random.choice(symbol)
    for i in range(10):
    Pass = (f"{a}{b}{c}{d}")
    P = ''.join(random.choice(Pass) for _ in range(10))
    await msgg.edit_text(f"Your Password is {P}")
  
