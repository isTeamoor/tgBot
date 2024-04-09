import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, PreCheckoutQuery
from aiogram.filters.command import Command
from aiogram.enums.content_type import ContentType


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

@dp.message(F.text.lower() == "2")
async def userPayment(message: Message):
   await auctions.sendInvoice(message, bot)

@dp.pre_checkout_query()
async def preCheckPayment(pre_checkout_query: PreCheckoutQuery):
    await auctions.preCheckPay(pre_checkout_query, bot)

@dp.message(F.successful_payment != None)
async def successfulPayment(message:Message):
    await auctions.successPay(message, bot)





async def main():
    await dp.start_polling(bot)
if __name__ == "__main__":
    asyncio.run(main())