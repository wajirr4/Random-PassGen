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
    #---------change pass for {10} digits-------
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
    
    #---------change pass for {6} digits-------
    elif cb.data == "chngpass11":
        Pass11 = string.ascii_letters + string.digits
        P11 = ''.join(random.choice(Pass11) for _ in range(6))
        await cb.message.edit_text('__Generating another password plish wait..__')
        await cb.answer("Password Changed Successfully✅!")       
        await cb.message.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P11}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass11")]]))
    elif cb.data == "chngpass12":
        Pass12 = string.ascii_letters + string.punctuation
        P12 = ''.join(random.choice(Pass12) for _ in range(6))
        await cb.message.edit_text('__Generating another password plish wait..__')
        await cb.answer("Password Changed Successfully✅!")       
        await cb.message.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P12}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass12")]]))
    elif cb.data == "chngpass13":
        Pass13 = string.ascii_letters + string.digits + string.punctuation
        P13 = ''.join(random.choice(Pass13) for _ in range(6))
        await cb.message.edit_text('__Generating another password plish wait..__')
        await cb.answer("Password Changed Successfully✅!")       
        await cb.message.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P13}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass13")]]))
    elif cb.data == "chngpass14":
        Pass14 = string.ascii_uppercase + string.digits
        P14 = ''.join(random.choice(Pass14) for _ in range(6))
        await cb.message.edit_text('__Generating another password plish wait..__')
        await cb.answer("Password Changed Successfully✅!")       
        await cb.message.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P14}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass14")]]))
    elif cb.data == "chngpass15":
        Pass15 = string.ascii_lowercase + string.digits
        P15 = ''.join(random.choice(Pass15) for _ in range(6))
        await cb.message.edit_text('__Generating another password plish wait..__')
        await cb.answer("Password Changed Successfully✅!")       
        await cb.message.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P15}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass15")]]))
    elif cb.data == "chngpass16":
        Pass16 = string.ascii_lowercase + string.punctuation
        P16 = ''.join(random.choice(Pass16) for _ in range(6))
        await cb.message.edit_text('__Generating another password plish wait..__')
        await cb.answer("Password Changed Successfully✅!")       
        await cb.message.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P16}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass16")]]))
    elif cb.data == "chngpass17":
        Pass17 = string.ascii_uppercase + string.punctuation
        P17 = ''.join(random.choice(Pass17) for _ in range(6))
        await cb.message.edit_text('__Generating another password plish wait..__')
        await cb.answer("Password Changed Successfully✅!")       
        await cb.message.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P17}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass17")]]))
    elif cb.data == "chngpass18":
        Pass18 = string.ascii_lowercase + string.digits + string.punctuation
        P18 = ''.join(random.choice(Pass18) for _ in range(6))
        await cb.message.edit_text('__Generating another password plish wait..__')
        await cb.answer("Password Changed Successfully✅!")       
        await cb.message.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P18}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass18")]]))
    elif cb.data == "chngpass19":
        Pass19 = string.ascii_uppercase + string.digits + string.punctuation
        P19 = ''.join(random.choice(Pass19) for _ in range(6))
        await cb.message.edit_text('__Generating another password plish wait..__')
        await cb.answer("Password Changed Successfully✅!")       
        await cb.message.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P19}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass19")]]))
    elif cb.data == "chngpass20":
        Pass20 = string.punctuation + string.digits
        P20 = ''.join(random.choice(Pass20) for _ in range(6))
        await cb.message.edit_text('__Generating another password plish wait..__')
        await cb.answer("Password Changed Successfully✅!")       
        await cb.message.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P20}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass20")]]))










