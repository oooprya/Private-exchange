#!/bin/bash
import asyncio
from pytz import timezone
from datetime import datetime
from functions.all_fun import update_course, parser_exchanger
import hashlib
from loguru import logger


@logger.catch
async def post_db(db):

    previous_hash = None

    tz = timezone('Europe/Kiev')

    data = parser_exchanger()
    
    await update_course(data)

    while True:
    
        now = datetime.now(tz)

        # Работаем только с 8:00 до 20:00
        if now.hour >= 8 and now.hour < 20:
            # Получаем данные и хеш
            data = parser_exchanger()

            # Вычисляем текущий хеш
            current_hash = hashlib.md5(
                f"{data}".encode('utf-8')).hexdigest()

            logger.debug(
                f"Проверка курса: "
                f"{now} "
                f"{current_hash} "
                f"{previous_hash}"
            )

            # Сравниваем с предыдущим хешем
            if (
                previous_hash is not None
                and current_hash != previous_hash
            ):
                logger.info(f"Обновление курса! Новый хеш: {current_hash}")
                await update_course(data)

            # Обновляем предыдущий хеш
            previous_hash = current_hash

            # Ждем 5 минут (300 секунд)
            await asyncio.sleep(300)
        else:

            await asyncio.sleep(60)
