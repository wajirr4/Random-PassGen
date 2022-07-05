import re
import random, string
from pyrogram import Client as sree
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

@sree.on_callback_query()
async def close_(Client, cb: CallbackQuery):
    if cb.data == "close_":
        await cb.answer("Menu Closed!")
        await cb.message.delete()
'''
    elif cb.data == "chngpass1":
        Pass = string.ascii_letters + string.digits + string.punctuation
        P = ''.join(random.choice(Pass) for _ in range(10))
        callback_data = CallbackQuery.data.strip()
        callback_request = callback_data.split(None, 1)[1]
        query, user_id = callback_request.split("|")
        if cb.from_user.id != int(user_id):
            try:
                return await cb.answer(
                    "You are Not allowed to change this", show_alert=True
                )
            except:
                return 
        await cb.message.edit_text('__Generating another password plish wait..__')          
        await cb.message.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="ping_")]]))
'''

@sree.on_callback_query(filters.regex("chngpass1"))
async def command(_, CallbackQuery):
    Pass = string.ascii_letters + string.digits + string.punctuation
    P = ''.join(random.choice(Pass) for _ in range(10))
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    query, user_id = callback_request.split("|")
    if CallbackQuery.from_user.id != int(user_id):
        try:
            return await CallbackQuery.answer(
                "You're not allowed to close this.", show_alert=True
            )
        except:
            return
    await cb.message.edit_text('__Generating another password plish wait..__')          
    await cb.message.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="ping_")]]))
