from aiogram import Bot, Dispatcher
from config import TOKEN
import asyncio
import logging
import sys


async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bye")