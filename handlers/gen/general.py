from aiogram import types
from aiogram.types.web_app_info import WebAppInfo

import time

from . import calc



async def start(message):
    await message.answer("Hello!")
