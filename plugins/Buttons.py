from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup


strtbtn = [
    [
        InlineKeyboardButton(text='Support', url="https://t.me/anonbots1"),
        InlineKeyboardButton(text='Source', callback_data="repo_")
    ],
    [        
        InlineKeyboardButton(text='Commands', callback_data="help_")
    ]
]


homebtn = [
    [      
        InlineKeyboardButton(text='Go Home!', callback_data="home_")
    ]
]
