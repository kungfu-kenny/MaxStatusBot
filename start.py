import time
import asyncio
import schedule
from aiogram import (
    Bot, 
    Dispatcher, 
    executor
)
from utilities import develop_file_string
from config import ConfigTelegram


bot = Bot(token=ConfigTelegram.token)
dp = Dispatcher(bot)

async def make_group_values_message(loop) -> set:
    """
    Function which is dedicated to get required values
    """
    groups, message = develop_file_string()
    for chat_id in groups:
        await bot.send_message(chat_id, message)
    return 

def main():
    loop = asyncio.get_event_loop()
    executor.start(dp, make_group_values_message(loop), skip_updates=True)


if __name__ == '__main__':
    schedule.every().day.at("12:30").do(main)
    while True:
        schedule.run_pending()
        time.sleep(1)