from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup


strtbtn = [
    [
        InlineKeyboardButton(
            'Support',
            url="https://silentverse"
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
