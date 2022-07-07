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
    elif cb.data == "chngpass1":
        Pass1 = string.ascii_letters + string.digits
        P1 = ''.join(random.choice(Pass1) for _ in range(10))
        await cb.message.edit_text('__Generating another password plish wait..__')
        await cb.answer("Password Changed Successfully✅!")       
        await cb.message.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P1}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass1")]]))
    elif cb.data == "chngpass2":
        Pass2 = string.ascii_letters + string.punctuation
        P2 = ''.join(random.choice(Pass2) for _ in range(10))
        await cb.message.edit_text('__Generating another password plish wait..__')
        await cb.answer("Password Changed Successfully✅!")       
        await cb.message.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P2}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass2")]]))
    elif cb.data == "chngpass3":
        Pass3 = string.ascii_letters + string.digits + string.punctuation
        P3 = ''.join(random.choice(Pass3) for _ in range(10))
        await cb.message.edit_text('__Generating another password plish wait..__')
        await cb.answer("Password Changed Successfully✅!")       
        await cb.message.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P3}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass3")]]))
    elif cb.data == "chngpass4":
        Pass4 = string.ascii_uppercase + string.digits
        P4 = ''.join(random.choice(Pass4) for _ in range(10))
        await cb.message.edit_text('__Generating another password plish wait..__')
        await cb.answer("Password Changed Successfully✅!")       
        await cb.message.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P4}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass4")]]))
    elif cb.data == "chngpass5":
        Pass5 = string.ascii_lowercase + string.digits
        P5 = ''.join(random.choice(Pass5) for _ in range(10))
        await cb.message.edit_text('__Generating another password plish wait..__')
        await cb.answer("Password Changed Successfully✅!")       
        await cb.message.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P5}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass5")]]))
    elif cb.data == "chngpass6":
        Pass6 = string.ascii_lowercase + string.punctuation
        P6 = ''.join(random.choice(Pass6) for _ in range(10))
        await cb.message.edit_text('__Generating another password plish wait..__')
        await cb.answer("Password Changed Successfully✅!")       
        await cb.message.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P6}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass6")]]))
    elif cb.data == "chngpass7":
        Pass7 = string.ascii_uppercase + string.punctuation
        P7 = ''.join(random.choice(Pass7) for _ in range(10))
        await cb.message.edit_text('__Generating another password plish wait..__')
        await cb.answer("Password Changed Successfully✅!")       
        await cb.message.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P7}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass7")]]))
    elif cb.data == "chngpass8":
        Pass8 = string.ascii_lowercase + string.digits + string.punctuation
        P8 = ''.join(random.choice(Pass8) for _ in range(10))
        await cb.message.edit_text('__Generating another password plish wait..__')
        await cb.answer("Password Changed Successfully✅!")       
        await cb.message.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P8}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass8")]]))
    elif cb.data == "chngpass9":
        Pass9 = string.ascii_uppercase + string.digits + string.punctuation
        P9 = ''.join(random.choice(Pass9) for _ in range(10))
        await cb.message.edit_text('__Generating another password plish wait..__')
        await cb.answer("Password Changed Successfully✅!")       
        await cb.message.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P9}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass9")]]))
    elif cb.data == "chngpass10":
        Pass10 = string.punctuation + string.digits
        P10 = ''.join(random.choice(Pass10) for _ in range(10))
        await cb.message.edit_text('__Generating another password plish wait..__')
        await cb.answer("Password Changed Successfully✅!")       
        await cb.message.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P10}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass10")]]))











