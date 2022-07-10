from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup


strtbtn = [
    [
        InlineKeyboardButton(
            'Support',
            url="https://t.me/silentverse"
        ),
        InlineKeyboardButton(
            'Source',
            callback_data="repo_"
        ),
    ],
    [        
        InlineKeyboardButton(
            'Commands',
            callback_data="help_"
        ),
    ],
]


homebtn = [
    [      
        InlineKeyboardButton(
            'Go Home!',
            callback_data="home_"
        ),
    ]
]
