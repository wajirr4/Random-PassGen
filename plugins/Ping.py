import time
from datetime import datetime
from asyncio import sleep
from pyrogram import Client as sree
from pyrogram import filters
from pyrogram.types import Message


@sree.on_message(filters.command(["ping", "p", "on"]))
async def ping(sree, m: Message):
    start = datetime.now()
    start_time = time.time()
    a = await m.reply("⚡")
    end_time = time.time()
    await sleep(1) 
    b = await a.edit_text("<b><i>Pinging...</i></b>")
    await sleep(1.5)
    pong1 = (datetime.now() - start).microseconds / 1000
    pong2 = str(round((end_time - start_time) * 1000, 3)) + " ms"
    await b.edit_text("<b>Ping Pong!🏓\n\n✅Server Ping: <code>{} ms</code>\n✅Bot Ping</b>: <code>{}</code>".format(pong1, pong2))             
