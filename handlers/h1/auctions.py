from aiogram import types
from aiogram.types.web_app_info import WebAppInfo
import json

import time

from . import calc

webApp_URL = 'https://isteamoor.github.io/webApp.github.io/'
click_test = '398062629:TEST:999999999_F91D8F69C042267444B74CC0B3C747757EB0E065'
payme_test = '371317599:TEST:1712560294201'




async def appButton(message):
    timestamp = str( int(time.time()) )
    uniqUrl = webApp_URL + "?timestamp=" + timestamp

    buttons = [[types.InlineKeyboardButton(text="Перейти в Mini App", web_app=WebAppInfo(url=uniqUrl) ),],]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)

    await message.reply("Веб приложение", reply_markup=keyboard)




async def sendInvoice(message, bot):
    await bot.send_invoice(message.chat.id, 
                           title = 'Тестирование оплаты',
                           description = 'Тестирование оплаты поле description',
                           payload = json.dumps({'user_id':message.chat.id}),
                           currency = 'UZS', 
                           prices=[types.LabeledPrice(label='Тестовая покупка', amount=10000000)],
                           provider_token = click_test) 



async def preCheckPay(pre_checkout_query, bot):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)

async def successPay(message, bot):
    payment_info = message.successful_payment.to_python()
    user_id = payment_info['user_id']
    amount = payment_info['total_amount']
    currency = payment_info['currency']
    invoice_payload = payment_info['invoice_payload']

    await bot.send_message(user_id, f"Спасибо за оплату в размере {amount} {currency}. Payload = {invoice_payload}!")
