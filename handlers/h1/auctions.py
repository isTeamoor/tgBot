from aiogram import types
from aiogram.types.web_app_info import WebAppInfo

import time

from . import calc

webApp_URL = 'https://isteamoor.github.io/webApp.github.io/'


async def appButton(message):
    timestamp = str( int(time.time()) )
    url = webApp_URL + "?timestamp=" + timestamp

    inline_btn = types.InlineKeyboardButton(text='Открыть сайт внутри телеграм', web_app=WebAppInfo(url=url))
    inline_kb = types.InlineKeyboardMarkup(inline_keyboard=[[inline_btn]])
    
    await message.reply("Веб приложение", reply_markup=inline_kb)




