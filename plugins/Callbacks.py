from pyrogram import Client as sree
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

@sree.on_callback_query()
def close_(Client, cb: CallbackQuery):
    if cb.data == "close_":
        cb.answer("Menu Closed!", show_alert=True)
        cb.m.delete()
