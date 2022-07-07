import random, string
from pyrogram import Client as sree
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardButton
from resources.str import (NUMARIC, alpha, ALPHA)


@sree.on_message(filters.command('pgen'))
async def radniompass(sree, m: Message):
    msgg = await m.reply('__Generating your password plish wait..__')
    
    Pass = string.ascii_letters + string.digits + string.punctuation
    P = ''.join(random.choice(Pass) for _ in range(10))
    await msgg.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass1")]]))


##----------------------------------

#Selecting password generating mode {}
@sree.on_message(filters.regex('randpass1'))
async def rndpas1(sree, m: Message):
    await m.reply('')

@sree.on_message(filters.regex('randpass2'))
async def rndpas2(sree, m: Message):
    await m.reply('')

@sree.on_message(filters.regex('randpass3'))
async def rndpas3(sree, m: Message):
    await m.reply('')

@sree.on_message(filters.regex('randpass4'))
async def rndpas4(sree, m: Message):
    await m.reply('')

@sree.on_message(filters.regex('randpass5'))
async def rndpas5(sree, m: Message):
    await m.reply('')

@sree.on_message(filters.regex('randpass6'))
async def rndpas6(sree, m: Message):
    await m.reply('')

@sree.on_message(filters.regex('randpass7'))
async def rndpas7(sree, m: Message):
    await m.reply('')

@sree.on_message(filters.regex('randpass8'))
async def rndpas8(sree, m: Message):
    await m.reply('')

@sree.on_message(filters.regex('randpass9'))
async def rndpas9(sree, m: Message):
    await m.reply('')

@sree.on_message(filters.regex('randpass10'))
async def rndpas10(sree, m: Message):
    await m.reply('')





##----------------------------------


## Reply keyboard {10}
@sree.on_message(filters.regex('pgen1') & filters.private)
async def randompass1(sree, m: Message):
    msgg1 = await m.reply('__Generating your password plish wait..__')   
    Pass1 = string.ascii_letters + string.digits
    P1 = ''.join(random.choice(Pass1) for _ in range(10))
    await msgg1.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P1}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass1")]]))

@sree.on_message(filters.regex('pgen2') & filters.private)
async def randompass2(sree, m: Message):
    msgg2 = await m.reply('__Generating your password plish wait..__')   
    Pass2 = string.ascii_letters + string.punctuation 
    P2 = ''.join(random.choice(Pass2) for _ in range(10))
    await msgg2.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P2}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass1")]]))

@sree.on_message(filters.regex('pgen3') & filters.private)
async def randompass3(sree, m: Message):
    msgg3 = await m.reply('__Generating your password plish wait..__')   
    Pass3 = string.ascii_letters + string.digits + string.punctuation
    P3 = ''.join(random.choice(Pass3) for _ in range(10))
    await msgg3.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P3}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass1")]]))

@sree.on_message(filters.regex('pgen4') & filters.private)
async def randompass4(sree, m: Message):
    msgg4 = await m.reply('__Generating your password plish wait..__')   
    Pass4 = string.ascii_uppercase + string.digits
    P4 = ''.join(random.choice(Pass4) for _ in range(10))
    await msgg4.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P4}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass1")]]))

@sree.on_message(filters.regex('pgen5') & filters.private)
async def randompass5(sree, m: Message):
    msgg5 = await m.reply('__Generating your password plish wait..__')   
    Pass5 = string.ascii_lowercase + string.digits
    P5 = ''.join(random.choice(Pass5) for _ in range(10))
    await msgg5.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P5}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass1")]]))

@sree.on_message(filters.regex('pgen6') & filters.private)
async def randompass6(sree, m: Message):
    msgg = await m.reply('__Generating your password plish wait..__')   
    Pass = string.ascii_lowercase + string.punctuation
    P = ''.join(random.choice(Pass) for _ in range(10))
    await msgg.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass1")]]))

@sree.on_message(filters.regex('pgen7') & filters.private)
async def randompass7(sree, m: Message):
    msgg = await m.reply('__Generating your password plish wait..__')   
    Pass = string.ascii_uppercase + string.punctuation
    P = ''.join(random.choice(Pass) for _ in range(10))
    await msgg.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass1")]]))

@sree.on_message(filters.regex('pgen8') & filters.private)
async def randompass8(sree, m: Message):
    msgg = await m.reply('__Generating your password plish wait..__')   
    Pass = string.ascii_lowercase + string.digits + string.punctuation
    P = ''.join(random.choice(Pass) for _ in range(10))
    await msgg.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass1")]]))

@sree.on_message(filters.regex('pgen9') & filters.private)
async def randompass9(sree, m: Message):
    msgg = await m.reply('__Generating your password plish wait..__')   
    Pass = string.ascii_uppercase + string.digits + string.punctuation
    P = ''.join(random.choice(Pass) for _ in range(10))
    await msgg.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass1")]]))

@sree.on_message(filters.regex('pgen10') & filters.private)
async def randompass10(sree, m: Message):
    msgg = await m.reply('__Generating your password plish wait..__')   
    Pass = string.punctuation + string.digits
    P = ''.join(random.choice(Pass) for _ in range(10))
    await msgg.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass1")]]))


## Reply keyboard {6}
@sree.on_message(filters.regex('pgen1') & filters.private)
async def randompass11(sree, m: Message):
    msgg = await m.reply('__Generating your password plish wait..__')   
    Pass = string.ascii_letters + string.digits
    P = ''.join(random.choice(Pass) for _ in range(6))
    await msgg.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass1")]]))

@sree.on_message(filters.regex('pgen2') & filters.private)
async def randompass12(sree, m: Message):
    msgg = await m.reply('__Generating your password plish wait..__')   
    Pass = string.ascii_letters + string.punctuation 
    P = ''.join(random.choice(Pass) for _ in range(6))
    await msgg.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass1")]]))

@sree.on_message(filters.regex('pgen3') & filters.private)
async def randompass13(sree, m: Message):
    msgg = await m.reply('__Generating your password plish wait..__')   
    Pass = string.ascii_letters + string.digits + string.punctuation
    P = ''.join(random.choice(Pass) for _ in range(6))
    await msgg.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass1")]]))

@sree.on_message(filters.regex('pgen4') & filters.private)
async def randompass14(sree, m: Message):
    msgg = await m.reply('__Generating your password plish wait..__')   
    Pass = string.ascii_uppercase + string.digits
    P = ''.join(random.choice(Pass) for _ in range(6))
    await msgg.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass1")]]))

@sree.on_message(filters.regex('pgen5') & filters.private)
async def randompass15(sree, m: Message):
    msgg = await m.reply('__Generating your password plish wait..__')   
    Pass = string.ascii_lowercase + string.digits
    P = ''.join(random.choice(Pass) for _ in range(6))
    await msgg.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass1")]]))

@sree.on_message(filters.regex('pgen6') & filters.private)
async def randompass16(sree, m: Message):
    msgg = await m.reply('__Generating your password plish wait..__')   
    Pass = string.ascii_lowercase + string.punctuation
    P = ''.join(random.choice(Pass) for _ in range(6))
    await msgg.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass1")]]))

@sree.on_message(filters.regex('pgen7') & filters.private)
async def randompass17(sree, m: Message):
    msgg = await m.reply('__Generating your password plish wait..__')   
    Pass = string.ascii_uppercase + string.punctuation
    P = ''.join(random.choice(Pass) for _ in range(6))
    await msgg.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass1")]]))

@sree.on_message(filters.regex('pgen8') & filters.private)
async def randompass18(sree, m: Message):
    msgg = await m.reply('__Generating your password plish wait..__')   
    Pass = string.ascii_lowercase + string.digits + string.punctuation
    P = ''.join(random.choice(Pass) for _ in range(6))
    await msgg.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass1")]]))

@sree.on_message(filters.regex('pgen9') & filters.private)
async def randompass19(sree, m: Message):
    msgg = await m.reply('__Generating your password plish wait..__')   
    Pass = string.ascii_uppercase + string.digits + string.punctuation
    P = ''.join(random.choice(Pass) for _ in range(6))
    await msgg.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass1")]]))

@sree.on_message(filters.regex('pgen10') & filters.private)
async def randompass20(sree, m: Message):
    msgg = await m.reply('__Generating your password plish wait..__')   
    Pass = string.punctuation + string.digits
    P = ''.join(random.choice(Pass) for _ in range(6))
    await msgg.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass1")]]))


## Reply keyboard {8}
@sree.on_message(filters.regex('pgen1') & filters.private)
async def randompass21(sree, m: Message):
    msgg = await m.reply('__Generating your password plish wait..__')   
    Pass = string.ascii_letters + string.digits
    P = ''.join(random.choice(Pass) for _ in range(8))
    await msgg.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass1")]]))

@sree.on_message(filters.regex('pgen2') & filters.private)
async def randompass22(sree, m: Message):
    msgg = await m.reply('__Generating your password plish wait..__')   
    Pass = string.ascii_letters + string.punctuation 
    P = ''.join(random.choice(Pass) for _ in range(8))
    await msgg.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass1")]]))

@sree.on_message(filters.regex('pgen3') & filters.private)
async def randompass23(sree, m: Message):
    msgg = await m.reply('__Generating your password plish wait..__')   
    Pass = string.ascii_letters + string.digits + string.punctuation
    P = ''.join(random.choice(Pass) for _ in range(8))
    await msgg.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass1")]]))

@sree.on_message(filters.regex('pgen4') & filters.private)
async def randompass24(sree, m: Message):
    msgg = await m.reply('__Generating your password plish wait..__')   
    Pass = string.ascii_uppercase + string.digits
    P = ''.join(random.choice(Pass) for _ in range(8))
    await msgg.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass1")]]))

@sree.on_message(filters.regex('pgen5') & filters.private)
async def randompass25(sree, m: Message):
    msgg = await m.reply('__Generating your password plish wait..__')   
    Pass = string.ascii_lowercase + string.digits
    P = ''.join(random.choice(Pass) for _ in range(8))
    await msgg.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass1")]]))

@sree.on_message(filters.regex('pgen6') & filters.private)
async def randompass26(sree, m: Message):
    msgg = await m.reply('__Generating your password plish wait..__')   
    Pass = string.ascii_lowercase + string.punctuation
    P = ''.join(random.choice(Pass) for _ in range(8))
    await msgg.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass1")]]))

@sree.on_message(filters.regex('pgen7') & filters.private)
async def randompass27(sree, m: Message):
    msgg = await m.reply('__Generating your password plish wait..__')   
    Pass = string.ascii_uppercase + string.punctuation
    P = ''.join(random.choice(Pass) for _ in range(8))
    await msgg.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass1")]]))

@sree.on_message(filters.regex('pgen8') & filters.private)
async def randompass28(sree, m: Message):
    msgg = await m.reply('__Generating your password plish wait..__')   
    Pass = string.ascii_lowercase + string.digits + string.punctuation
    P = ''.join(random.choice(Pass) for _ in range(8))
    await msgg.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass1")]]))

@sree.on_message(filters.regex('pgen9') & filters.private)
async def randompass29(sree, m: Message):
    msgg = await m.reply('__Generating your password plish wait..__')   
    Pass = string.ascii_uppercase + string.digits + string.punctuation
    P = ''.join(random.choice(Pass) for _ in range(8))
    await msgg.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass1")]]))

@sree.on_message(filters.regex('pgen10') & filters.private)
async def randompass30(sree, m: Message):
    msgg = await m.reply('__Generating your password plish wait..__')   
    Pass = string.punctuation + string.digits
    P = ''.join(random.choice(Pass) for _ in range(8))
    await msgg.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass1")]]))



## Reply keyboard {12}
@sree.on_message(filters.regex('pgen1') & filters.private)
async def randompass31(sree, m: Message):
    msgg = await m.reply('__Generating your password plish wait..__')   
    Pass = string.ascii_letters + string.digits
    P = ''.join(random.choice(Pass) for _ in range(12))
    await msgg.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass1")]]))

@sree.on_message(filters.regex('pgen2') & filters.private)
async def randompass32(sree, m: Message):
    msgg = await m.reply('__Generating your password plish wait..__')   
    Pass = string.ascii_letters + string.punctuation 
    P = ''.join(random.choice(Pass) for _ in range(12))
    await msgg.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass1")]]))

@sree.on_message(filters.regex('pgen3') & filters.private)
async def randompass33(sree, m: Message):
    msgg = await m.reply('__Generating your password plish wait..__')   
    Pass = string.ascii_letters + string.digits + string.punctuation
    P = ''.join(random.choice(Pass) for _ in range(12))
    await msgg.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass1")]]))

@sree.on_message(filters.regex('pgen4') & filters.private)
async def randompass34(sree, m: Message):
    msgg = await m.reply('__Generating your password plish wait..__')   
    Pass = string.ascii_uppercase + string.digits
    P = ''.join(random.choice(Pass) for _ in range(12))
    await msgg.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass1")]]))

@sree.on_message(filters.regex('pgen5') & filters.private)
async def randompass35(sree, m: Message):
    msgg = await m.reply('__Generating your password plish wait..__')   
    Pass = string.ascii_lowercase + string.digits
    P = ''.join(random.choice(Pass) for _ in range(12))
    await msgg.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass1")]]))

@sree.on_message(filters.regex('pgen6') & filters.private)
async def randompass36(sree, m: Message):
    msgg = await m.reply('__Generating your password plish wait..__')   
    Pass = string.ascii_lowercase + string.punctuation
    P = ''.join(random.choice(Pass) for _ in range(12))
    await msgg.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass1")]]))

@sree.on_message(filters.regex('pgen7') & filters.private)
async def randompass37(sree, m: Message):
    msgg = await m.reply('__Generating your password plish wait..__')   
    Pass = string.ascii_uppercase + string.punctuation
    P = ''.join(random.choice(Pass) for _ in range(12))
    await msgg.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass1")]]))

@sree.on_message(filters.regex('pgen8') & filters.private)
async def randompass38(sree, m: Message):
    msgg = await m.reply('__Generating your password plish wait..__')   
    Pass = string.ascii_lowercase + string.digits + string.punctuation
    P = ''.join(random.choice(Pass) for _ in range(12))
    await msgg.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass1")]]))

@sree.on_message(filters.regex('pgen9') & filters.private)
async def randompass39(sree, m: Message):
    msgg = await m.reply('__Generating your password plish wait..__')   
    Pass = string.ascii_uppercase + string.digits + string.punctuation
    P = ''.join(random.choice(Pass) for _ in range(12))
    await msgg.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass1")]]))

@sree.on_message(filters.regex('pgen10') & filters.private)
async def randompass40(sree, m: Message):
    msgg = await m.reply('__Generating your password plish wait..__')   
    Pass = string.punctuation + string.digits
    P = ''.join(random.choice(Pass) for _ in range(12))
    await msgg.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass1")]]))













