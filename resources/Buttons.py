from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup


strtbtn = [
    [
        InlineKeyboardButton(
            'Creator',
            url='tg://user?id=5313879570'
        ),
        InlineKeyboardButton(
            'Support',
            url="https://silentverse"
        ),
    ],
    [
        InlineKeyboardButton(
            'Commands',
            callback_data="repo_"
        ),
        InlineKeyboardButton(
            'Commands',
            callback_data="help_"
        ),
    ],
]
