import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters.command import Command

from handlers.gen import general
from handlers.h1 import auctions

bot = Bot(token='7035946635:AAHgHVVwbsmJu2XagmMUTcByzd1IhTYYVkc')
dp = Dispatcher()




### [General]
@dp.message(Command("start"))
async def start(message: Message):
    await general.start(message)


### [Auctions]
@dp.message(F.text.lower() == "1")
async def link_to_webApp(message: Message):
    await auctions.appButton(message)




async def main():
    await dp.start_polling(bot)
if __name__ == "__main__":
    asyncio.run(main())