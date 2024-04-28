from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from text import courses



menu = []

for i in range(number_of_courses):
    menu.append([InlineKeyboardButton(text=courses[i], callback_data="couse_number{i}")])

"""]
    [InlineKeyboardButton(text=courses[0], callback_data="generate_text"),
    InlineKeyboardButton(text=courses[1], callback_data="generate_image")],
    [InlineKeyboardButton(text=courses[2], callback_data="buy_tokens"),
    InlineKeyboardButton(text="текст 4", callback_data="balance")],
    [InlineKeyboardButton(text="текст 5", callback_data="ref"),
    InlineKeyboardButton(text="", callback_data="ref"),
    InlineKeyboardButton(text="🎁 Бесплатные токены", callback_data="free_tokens")],
    [InlineKeyboardButton(text="🔎 Помощь", callback_data="help")]
]
"""
menu = InlineKeyboardMarkup(inline_keyboard=menu)
exit_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="◀️ Выйти в меню")]], resize_keyboard=True)
iexit_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="◀️ Выйти в меню", callback_data="menu")]])

