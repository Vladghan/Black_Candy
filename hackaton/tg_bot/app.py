from aiogram import executor
from bot_commands import set_default_commands
from loader import bot, dp, storage, scheduler
from my_logger import logger
import handlers
# from scheduler import schedule_jobs


async def on_startup(dp):
    await set_default_commands(dp)
    # schedule_jobs()
    logger.info('Bot is started')


async def on_shutdown(dp):
    await bot.close()
    await storage.close()
    logger.info("Bot is stopped")


if __name__ == '__main__':
    scheduler.start()
    executor.start_polling(dp, on_shutdown=on_shutdown, on_startup=on_startup, skip_updates=True)
