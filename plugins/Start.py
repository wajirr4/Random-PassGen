from asyncio import sleep
from pyrogram import Client as sree
from pyrogram import filters
from pyrogram.types import Message

@sree.on_message(filters.command('start'))
async def start(sree, m: Message):
    nm = m.from_user.first_name
    uid = m.from_user.id
    chtid = m.chat.id
    a = await sree.send_message(chtid, f"Hey, [{nm}](tg://user?id={uid}) 🙋")
    await sleep(0.5)
    b = await a.edit_text("Starting Bot Server For You..")
    await sleep(1)
    c = await b.edit_text("Server Started Successfully ✅\n\nHere we Go🥳!!")
    await sleep(0.4)
    await c.delete()
    await m.reply_photo(photo="https://telegra.ph/file/92df9a7eb2a28fa462342.jpg", caption=f"Hey {nm},\n\nI am strong random Password Generator For your social media accounts so that you can keep your accounts safe from cheaters//hackers\n\nTry /pgen to generate your random password  \n\nNote* :- This Bot Is Under __maintenance__ More info will add soon! 🔜👷")
    await sleep(0.2)
    await m.delete()   
