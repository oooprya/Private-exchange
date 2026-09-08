#!/bin/bash
import asyncio
from aiogram.enums import ParseMode
from aiogram.client.bot import DefaultBotProperties
from functions.all_fun import status_orders
from config import db
from os import getenv
from datetime import datetime
from pytz import timezone
from allkeyboard.all_keyboard import accept_order
from aiogram import Bot
from loguru import logger


orders_url = f'{getenv("API")}/api/v1/orders/?status=new'
status_accepted = f'{getenv("API")}/api/v1/orders/?status=accepted'


logger.add("cron.log", colorize=True,
           format="{time:YYYY-MM-DD HH:mm:ss} {name} {line} {level} {message} ", 
           level="DEBUG", rotation="500 KB", compression="zip")


def get_users_data(role: str):
    """Проверяем роль"""
    res, user_data = db.exists_role(role)
    if res:
        return user_data[1]


@logger.catch
async def order_send_message():
    """ Получаем новый заказ из сайта по API и отправляю Менеджеру """
    bot = Bot(token=getenv("TOKEN"), default=DefaultBotProperties(
        parse_mode=ParseMode.HTML))

    while True:
        data_chat_id = getenv("KASSARABOTA")
        # logger.info(data_chat_id)
        now = datetime.now(timezone('Europe/Kiev'))
        # Проверяем, находится ли текущее время в пределах 8:00 - 21:00
        if now.hour >= 8 and now.hour < 23:
            isorder, order_data = db.get_orders_status(status="new")
            if isorder:
                async with bot.session:  # or `bot.context()`
                    try:
                        order = order_data[0]
                        # logger.debug(f"{order}")
                        id = f"{order[0]}".zfill(4)
                        rate = str(order[6]).rstrip('0').rstrip('.')
                        send_order = f"🛎 <b>Нове замовлення</b> {id}\n\n🏦{order[3]}\n{order[4]} \n<b>{order[5]}</b> по {rate} \nCума <b>{order[7]}</b>\n\n📲+{order[2]}"
                        # logger.debug(await bot.get_me())
                        if order[3] == 'вул. Успенська, 41':
                            data_chat_id = getenv("USPENSKAYA")

                        meg = await bot.send_message(
                            chat_id=data_chat_id,
                            text=send_order,
                            reply_markup=accept_order(id)
                        )
                        await status_orders(order[0], "ordersent")
                        logger.debug(f'{meg.text}')
                    except:
                        logger.debug(f"замовлення нема")

            # Ждем 1 минуту
            await asyncio.sleep(60)
        else:
            # Если текущее время вне диапазона, ждем 1 минуту перед следующей проверкой
            await asyncio.sleep(60)
