from aiogram import types
from my_logger import logger

async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("sessions", 'Текущие сессии')
    ])
    logger.info('Commands are set')
