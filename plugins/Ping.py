import time
from asyncio import sleep
from pyrogram import Client as sree
from pyrogram import filters
from pyrogram.types import Message


@sree.on_message(filters.command(["ping", "p", "on"]))
async def ping(sree, m: Message):
    start_time = time.time()
    end_time = time.time()
    pong = str(round((end_time - start_time) * 1000, 3)) + " ms"
    a = await m.reply("⚡")
    await sleep(1) 
    b = await a.edit_text("<b><i>Pinging...</i></b>")
    await sleep(1.5)
    await b.edit_text("<b>Ping Pong! 🏓\n\nPing Time✅</b>: <code>{}</code>".format(pong))             
