# Powered by @HYPER_AD13 | @ShiningOff. 
# Dear Pero ppls Plish Don't remove this line from here🌚

import random, string
from asyncio import sleep as s
from pyrogram import Client as sree
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from resources.string import (pgentxt, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, pmmsg, grpmsg)
from resources.replyKeyboard import (btn1, b10, b9, b8, b7, b6, b5, b4, b3, b2, b1)


@sree.on_message(filters.command(['password', 'passgen', 'pgen']))
async def radniompass(sree, m: Message):
    nm = m.from_user.first_name
    chtID = m.chat.id
    if m.chat.id != m.from_user.id:
        l = await m.reply('<i>Generating Your Answer 🥲..</i>')
        await s(1.5)
        k = await l.edit_text(grpmsg.format(nm, chtID), reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Go To My Pm!", url=f'https://t.me/{BOT_USERNAME}?start=true')],[InlineKeyboardButton("Close Menu!", callback_data="close_")]]))       
        await m.delete()
        await s(20)
        await k.delete()
    if m.chat.id == m.from_user.id:
        await m.reply(pgentxt.format(nm), reply_markup=ReplyKeyboardMarkup(btn1, one_time_keyboard=True))


@sree.on_message(filters.command(['gen', 'create', 'sgen']))
async def radniompass(sree, m: Message):
    nm = m.from_user.first_name
    chtID = m.chat.idl
    if m.chat.id != m.from_user.id:
        msgg = await m.reply('__Generating your password plish wait..__')   
        Pass = string.ascii_letters + string.digits + string.punctuation
        P = ''.join(random.choice(Pass) for _ in range(10))
        await msgg.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass1")]]))
    if m.chat.id == m.from_user.id:
        l = await m.reply('<i>Generating Your Answer 🥲..</i>')
        await s(1.5)
        await l.edit_text(pmmsg.format(nm, chtID), reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Go To My Pm!", url=f'https://t.me/{BOT_USERNAME}?startgroup=true')]]))
        await m.delete()


##-----------------–-———------------



@sree.on_message(filters.regex('••Go To Home Menu••') & filters.private)
async def home(sree, m: Message):
    nm = m.from_user.first_name
    await m.reply(pgentxt.format(nm), reply_markup=ReplyKeyboardMarkup(btn1))




##----------------------------------




#Selecting password generating mode {}
@sree.on_message(filters.regex('Password-1') & filters.private)
async def rndpas1(sree, m: Message):   
    nm = m.from_user.first_name 
    await m.reply(t1.format(nm), reply_markup=ReplyKeyboardMarkup(b1, one_time_keyboard=True, resize_keyboard=True))


@sree.on_message(filters.regex('Password-2') & filters.private)
async def rndpas2(sree, m: Message): 
    nm = m.from_user.first_name   
    await m.reply(t2.format(nm), reply_markup=ReplyKeyboardMarkup(b2, one_time_keyboard=True, resize_keyboard=True))


@sree.on_message(filters.regex('Password-3') & filters.private)
async def rndpas3(sree, m: Message):  
    nm = m.from_user.first_name  
    await m.reply(t3.format(nm), reply_markup=ReplyKeyboardMarkup(b3, one_time_keyboard=True, resize_keyboard=True))


@sree.on_message(filters.regex('Password-4') & filters.private)
async def rndpas4(sree, m: Message): 
    nm = m.from_user.first_name   
    await m.reply(t4.format(nm), reply_markup=ReplyKeyboardMarkup(b4, one_time_keyboard=True, resize_keyboard=True))


@sree.on_message(filters.regex('Password-5') & filters.private)
async def rndpas5(sree, m: Message):
    nm = m.from_user.first_name    
    await m.reply(t5.format(nm), reply_markup=ReplyKeyboardMarkup(b5, one_time_keyboard=True, resize_keyboard=True))


@sree.on_message(filters.regex('Password-6') & filters.private)
async def rndpas6(sree, m: Message): 
    nm = m.from_user.first_name  
    await m.reply(t6.format(nm), reply_markup=ReplyKeyboardMarkup(b6, one_time_keyboard=True, resize_keyboard=True))


@sree.on_message(filters.regex('Password-7') & filters.private)
async def rndpas7(sree, m: Message): 
    nm = m.from_user.first_name  
    await m.reply(t7.format(nm), reply_markup=ReplyKeyboardMarkup(b7, one_time_keyboard=True, resize_keyboard=True))


@sree.on_message(filters.regex('Password-8') & filters.private)
async def rndpas8(sree, m: Message): 
    nm = m.from_user.first_name 
    await m.reply(t8.format(nm), reply_markup=ReplyKeyboardMarkup(b8, one_time_keyboard=True, resize_keyboard=True))


@sree.on_message(filters.regex('Password-9') & filters.private)
async def rndpas9(sree, m: Message):
    nm = m.from_user.first_name   
    await m.reply(t9.format(nm), reply_markup=ReplyKeyboardMarkup(b9, one_time_keyboard=True, resize_keyboard=True))


@sree.on_message(filters.regex('Password-10') & filters.private)
async def rndpas10(sree, m: Message):  
    nm = m.from_user.first_name  
    await m.reply(t10.format(nm), reply_markup=ReplyKeyboardMarkup(b10, one_time_keyboard=True, resize_keyboard=True))





##----------------------------------



## Reply keyboard {10}
@sree.on_message(filters.regex('Generate-1-10') & filters.private)
async def randompass1(sree, m: Message):
    msgg1 = await m.reply('__Generating your password plish wait..__')   
    Pass1 = string.ascii_letters + string.digits
    P1 = ''.join(random.choice(Pass1) for _ in range(10))
    await msgg1.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P1}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass1")]]))

@sree.on_message(filters.regex('Generate-2-10') & filters.private)
async def randompass2(sree, m: Message):
    msgg2 = await m.reply('__Generating your password plish wait..__')   
    Pass2 = string.ascii_letters + string.punctuation 
    P2 = ''.join(random.choice(Pass2) for _ in range(10))
    await msgg2.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P2}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass2")]]))

@sree.on_message(filters.regex('Generate-3-10') & filters.private)
async def randompass3(sree, m: Message):
    msgg3 = await m.reply('__Generating your password plish wait..__')   
    Pass3 = string.ascii_letters + string.digits + string.punctuation
    P3 = ''.join(random.choice(Pass3) for _ in range(10))
    await msgg3.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P3}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass3")]]))

@sree.on_message(filters.regex('Generate-4-10') & filters.private)
async def randompass4(sree, m: Message):
    msgg4 = await m.reply('__Generating your password plish wait..__')   
    Pass4 = string.ascii_uppercase + string.digits
    P4 = ''.join(random.choice(Pass4) for _ in range(10))
    await msgg4.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P4}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass4")]]))

@sree.on_message(filters.regex('Generate-5-10') & filters.private)
async def randompass5(sree, m: Message):
    msgg5 = await m.reply('__Generating your password plish wait..__')   
    Pass5 = string.ascii_lowercase + string.digits
    P5 = ''.join(random.choice(Pass5) for _ in range(10))
    await msgg5.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P5}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass5")]]))

@sree.on_message(filters.regex('Generate-6-10') & filters.private)
async def randompass6(sree, m: Message):
    msgg6 = await m.reply('__Generating your password plish wait..__')   
    Pass6 = string.ascii_lowercase + string.punctuation
    P6 = ''.join(random.choice(Pass6) for _ in range(10))
    await msgg6.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P6}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass6")]]))

@sree.on_message(filters.regex('Generate-7-10') & filters.private)
async def randompass7(sree, m: Message):
    msgg7 = await m.reply('__Generating your password plish wait..__')   
    Pass7 = string.ascii_uppercase + string.punctuation
    P7 = ''.join(random.choice(Pass7) for _ in range(10))
    await msgg7.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P7}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass7")]]))

@sree.on_message(filters.regex('Generate-8-10') & filters.private)
async def randompass8(sree, m: Message):
    msgg8 = await m.reply('__Generating your password plish wait..__')   
    Pass8 = string.ascii_lowercase + string.digits + string.punctuation
    P8 = ''.join(random.choice(Pass8) for _ in range(10))
    await msgg8.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P8}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass8")]]))

@sree.on_message(filters.regex('Generate-9-10') & filters.private)
async def randompass9(sree, m: Message):
    msgg9 = await m.reply('__Generating your password plish wait..__')   
    Pass9 = string.ascii_uppercase + string.digits + string.punctuation
    P9 = ''.join(random.choice(Pass9) for _ in range(10))
    await msgg9.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P9}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass9")]]))

@sree.on_message(filters.regex('Generate-10-10') & filters.private)
async def randompass10(sree, m: Message):
    msgg10 = await m.reply('__Generating your password plish wait..__')   
    Pass10 = string.punctuation + string.digits
    P10 = ''.join(random.choice(Pass10) for _ in range(10))
    await msgg10.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P10}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass10")]]))



## Reply keyboard {6}
@sree.on_message(filters.regex('GenPass-1-6') & filters.private)
async def randompass11(sree, m: Message):
    msgg11 = await m.reply('__Generating your password plish wait..__')   
    Pass11 = string.ascii_letters + string.digits
    P11 = ''.join(random.choice(Pass11) for _ in range(6))
    await msgg11.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P11}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass11")]]))

@sree.on_message(filters.regex('GenPass-2-6') & filters.private)
async def randompass12(sree, m: Message):
    msgg12 = await m.reply('__Generating your password plish wait..__')   
    Pass12 = string.ascii_letters + string.punctuation 
    P12 = ''.join(random.choice(Pass12) for _ in range(6))
    await msgg12.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P12}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass12")]]))

@sree.on_message(filters.regex('GenPass-3-6') & filters.private)
async def randompass13(sree, m: Message):
    msgg13 = await m.reply('__Generating your password plish wait..__')   
    Pass13 = string.ascii_letters + string.digits + string.punctuation
    P13 = ''.join(random.choice(Pass13) for _ in range(6))
    await msgg13.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P13}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass13")]]))

@sree.on_message(filters.regex('GenPass-4-6') & filters.private)
async def randompass14(sree, m: Message):
    msgg14 = await m.reply('__Generating your password plish wait..__')   
    Pass14 = string.ascii_uppercase + string.digits
    P14 = ''.join(random.choice(Pass14) for _ in range(6))
    await msgg14.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P14}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass14")]]))

@sree.on_message(filters.regex('GenPass-5-6') & filters.private)
async def randompass15(sree, m: Message):
    msgg15 = await m.reply('__Generating your password plish wait..__')   
    Pass15 = string.ascii_lowercase + string.digits
    P15 = ''.join(random.choice(Pass15) for _ in range(6))
    await msgg15.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P15}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass15")]]))

@sree.on_message(filters.regex('GenPass-6-6') & filters.private)
async def randompass16(sree, m: Message):
    msgg16 = await m.reply('__Generating your password plish wait..__')   
    Pass16 = string.ascii_lowercase + string.punctuation
    P16 = ''.join(random.choice(Pass16) for _ in range(6))
    await msgg16.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P16}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass16")]]))

@sree.on_message(filters.regex('GenPass-7-6') & filters.private)
async def randompass17(sree, m: Message):
    msgg17 = await m.reply('__Generating your password plish wait..__')   
    Pass17 = string.ascii_uppercase + string.punctuation
    P17 = ''.join(random.choice(Pass17) for _ in range(6))
    await msgg17.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P17}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass17")]]))

@sree.on_message(filters.regex('GenPass-8-6') & filters.private)
async def randompass18(sree, m: Message):
    msgg18 = await m.reply('__Generating your password plish wait..__')   
    Pass18 = string.ascii_lowercase + string.digits + string.punctuation
    P18 = ''.join(random.choice(Pass18) for _ in range(6))
    await msgg18.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P18}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass18")]]))

@sree.on_message(filters.regex('GenPass-9-6') & filters.private)
async def randompass19(sree, m: Message):
    msgg19 = await m.reply('__Generating your password plish wait..__')   
    Pass19 = string.ascii_uppercase + string.digits + string.punctuation
    P19 = ''.join(random.choice(Pass19) for _ in range(6))
    await msgg19.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P19}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass19")]]))

@sree.on_message(filters.regex('GenPass-10-6') & filters.private)
async def randompass20(sree, m: Message):
    msgg20 = await m.reply('__Generating your password plish wait..__')   
    Pass20 = string.punctuation + string.digits
    P20 = ''.join(random.choice(Pass20) for _ in range(6))
    await msgg20.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P20}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass20")]]))




## Reply keyboard {8}
@sree.on_message(filters.regex('Generates-1-8') & filters.private)
async def randompass21(sree, m: Message):
    msgg21 = await m.reply('__Generating your password plish wait..__')   
    Pass21 = string.ascii_letters + string.digits
    P21 = ''.join(random.choice(Pass21) for _ in range(8))
    await msgg21.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P21}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass21")]]))

@sree.on_message(filters.regex('Generates-2-8') & filters.private)
async def randompass22(sree, m: Message):
    msgg22 = await m.reply('__Generating your password plish wait..__')   
    Pass22 = string.ascii_letters + string.punctuation 
    P22 = ''.join(random.choice(Pass22) for _ in range(8))
    await msgg22.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P22}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass22")]]))

@sree.on_message(filters.regex('Generates-3-8') & filters.private)
async def randompass23(sree, m: Message):
    msgg23 = await m.reply('__Generating your password plish wait..__')   
    Pass23 = string.ascii_letters + string.digits + string.punctuation
    P23 = ''.join(random.choice(Pass23) for _ in range(8))
    await msgg23.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P23}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass23")]]))

@sree.on_message(filters.regex('Generates-4-8') & filters.private)
async def randompass24(sree, m: Message):
    msgg24 = await m.reply('__Generating your password plish wait..__')   
    Pass24 = string.ascii_uppercase + string.digits
    P24 = ''.join(random.choice(Pass24) for _ in range(8))
    await msgg24.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P24}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass24")]]))

@sree.on_message(filters.regex('Generates-5-8') & filters.private)
async def randompass25(sree, m: Message):
    msgg25 = await m.reply('__Generating your password plish wait..__')   
    Pass25 = string.ascii_lowercase + string.digits
    P25 = ''.join(random.choice(Pass25) for _ in range(8))
    await msgg25.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P25}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass25")]]))

@sree.on_message(filters.regex('Generates-6-8') & filters.private)
async def randompass26(sree, m: Message):
    msgg26 = await m.reply('__Generating your password plish wait..__')   
    Pass26 = string.ascii_lowercase + string.punctuation
    P26 = ''.join(random.choice(Pass26) for _ in range(8))
    await msgg26.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P26}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass26")]]))

@sree.on_message(filters.regex('Generates-7-8') & filters.private)
async def randompass27(sree, m: Message):
    msgg27 = await m.reply('__Generating your password plish wait..__')   
    Pass27 = string.ascii_uppercase + string.punctuation
    P27 = ''.join(random.choice(Pass27) for _ in range(8))
    await msgg27.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P27}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass27")]]))

@sree.on_message(filters.regex('Generates-8-8') & filters.private)
async def randompass28(sree, m: Message):
    msgg28 = await m.reply('__Generating your password plish wait..__')   
    Pass28 = string.ascii_lowercase + string.digits + string.punctuation
    P28 = ''.join(random.choice(Pass28) for _ in range(8))
    await msgg28.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P28}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass28")]]))

@sree.on_message(filters.regex('Generates-9-8') & filters.private)
async def randompass29(sree, m: Message):
    msgg29 = await m.reply('__Generating your password plish wait..__')   
    Pass29 = string.ascii_uppercase + string.digits + string.punctuation
    P29 = ''.join(random.choice(Pass29) for _ in range(8))
    await msgg29.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P29}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass29")]]))

@sree.on_message(filters.regex('Generates-10-8') & filters.private)
async def randompass30(sree, m: Message):
    msgg30 = await m.reply('__Generating your password plish wait..__')   
    Pass30 = string.punctuation + string.digits
    P30 = ''.join(random.choice(Pass30) for _ in range(8))
    await msgg30.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P30}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass30")]]))




## Reply keyboard {12}
@sree.on_message(filters.regex('GenPas-1-12') & filters.private)
async def randompass31(sree, m: Message):
    msgg31 = await m.reply('__Generating your password plish wait..__')   
    Pass31 = string.ascii_letters + string.digits
    P31 = ''.join(random.choice(Pass31) for _ in range(12))
    await msgg31.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P31}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass31")]]))

@sree.on_message(filters.regex('GenPas-2-12') & filters.private)
async def randompass32(sree, m: Message):
    msgg32 = await m.reply('__Generating your password plish wait..__')   
    Pass32 = string.ascii_letters + string.punctuation 
    P32 = ''.join(random.choice(Pass32) for _ in range(12))
    await msgg32.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P32}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass32")]]))

@sree.on_message(filters.regex('GenPas-3-12') & filters.private)
async def randompass33(sree, m: Message):
    msgg33 = await m.reply('__Generating your password plish wait..__')   
    Pass33 = string.ascii_letters + string.digits + string.punctuation
    P33 = ''.join(random.choice(Pass33) for _ in range(12))
    await msgg33.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P33}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass33")]]))

@sree.on_message(filters.regex('GenPas-4-12') & filters.private)
async def randompass34(sree, m: Message):
    msgg34 = await m.reply('__Generating your password plish wait..__')   
    Pass34 = string.ascii_uppercase + string.digits
    P34 = ''.join(random.choice(Pass34) for _ in range(12))
    await msgg34.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P34}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass34")]]))

@sree.on_message(filters.regex('GenPas-5-12') & filters.private)
async def randompass35(sree, m: Message):
    msgg35 = await m.reply('__Generating your password plish wait..__')   
    Pass35 = string.ascii_lowercase + string.digits
    P35 = ''.join(random.choice(Pass35) for _ in range(12))
    await msgg35.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P35}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass35")]]))

@sree.on_message(filters.regex('GenPas-6-12') & filters.private)
async def randompass36(sree, m: Message):
    msgg36 = await m.reply('__Generating your password plish wait..__')   
    Pass36 = string.ascii_lowercase + string.punctuation
    P36 = ''.join(random.choice(Pass36) for _ in range(12))
    await msgg36.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P36}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass36")]]))

@sree.on_message(filters.regex('GenPas-7-12') & filters.private)
async def randompass37(sree, m: Message):
    msgg37 = await m.reply('__Generating your password plish wait..__')   
    Pass37 = string.ascii_uppercase + string.punctuation
    P37 = ''.join(random.choice(Pass37) for _ in range(12))
    await msgg37.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P37}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass37")]]))

@sree.on_message(filters.regex('GenPas-8-12') & filters.private)
async def randompass38(sree, m: Message):
    msgg38 = await m.reply('__Generating your password plish wait..__')   
    Pass38 = string.ascii_lowercase + string.digits + string.punctuation
    P38 = ''.join(random.choice(Pass38) for _ in range(12))
    await msgg38.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P38}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass38")]]))

@sree.on_message(filters.regex('GenPas-9-12') & filters.private)
async def randompass39(sree, m: Message):
    msgg39 = await m.reply('__Generating your password plish wait..__')   
    Pass39 = string.ascii_uppercase + string.digits + string.punctuation
    P39 = ''.join(random.choice(Pass39) for _ in range(12))
    await msgg39.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P39}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass39")]]))

@sree.on_message(filters.regex('GenPas-10-12') & filters.private)
async def randompass40(sree, m: Message):
    msgg40 = await m.reply('__Generating your password plish wait..__')   
    Pass40 = string.punctuation + string.digits
    P40 = ''.join(random.choice(Pass40) for _ in range(12))
    await msgg40.edit_text(f"<b><u>Your Password is Generated Successfully✅</u>\n\nPassword</b>:- <code>{P40}</code>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Change Password", callback_data="chngpass40")]]))









